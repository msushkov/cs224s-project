#! /bin/bash

THRESHOLD=0.8
THRESHOLD_COMPL=0.2

psql $DBNAME -c """
	DROP TABLE IF EXISTS results;

	CREATE TABLE results AS
		SELECT l.dateid AS dateid,
		       inf.expectation AS predicted_probability,
		       l.label AS true_label
		FROM output_labels l,
		     output_is_enjoyable_inference inf
		WHERE l.dateid = inf.dateid AND
		      l.type = 'TEST';
"""

touch $APP_HOME/results.txt

tp=`psql $DBNAME -c """
	DROP TABLE IF EXISTS true_pos;

	CREATE TABLE true_pos AS
		SELECT dateid,
		       predicted_probability,
		       true_label
		FROM results
		WHERE predicted_probability > $THRESHOLD AND
		      true_label = '1';
"""`
echo "TP = $tp"
echo $tp | awk -F' ' '{print $2}' >> $APP_HOME/results.txt

fp=`psql $DBNAME -c """
	DROP TABLE IF EXISTS false_pos;

	CREATE TABLE false_pos AS
		SELECT dateid,
		       predicted_probability,
		       true_label
		FROM results
		WHERE predicted_probability > $THRESHOLD AND
		      true_label = '-1';
"""`
echo "FP = $fp"
echo $fp | awk -F' ' '{print $2}' >> $APP_HOME/results.txt

tn=`psql $DBNAME -c """
	DROP TABLE IF EXISTS true_neg;

	CREATE TABLE true_neg AS
		SELECT dateid,
		       predicted_probability,
		       true_label
		FROM results
		WHERE predicted_probability < $THRESHOLD_COMPL AND
		      true_label = '-1';
"""`
echo "TN = $tn"
echo $tn | awk -F' ' '{print $2}' >> $APP_HOME/results.txt

fn=`psql $DBNAME -c """
	DROP TABLE IF EXISTS false_neg;

	CREATE TABLE false_neg AS
		SELECT dateid,
		       predicted_probability,
		       true_label
		FROM results
		WHERE predicted_probability < $THRESHOLD_COMPL AND
		      true_label = '1';
"""`
echo "FN = $fn"
echo $fn | awk -F' ' '{print $2}' >> $APP_HOME/results.txt

python $APP_HOME/eval.py $APP_HOME/results.txt

rm $APP_HOME/results.txt


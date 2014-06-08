#! /bin/bash

echo "Creating the database..."
dropdb $DBNAME
createdb $DBNAME
psql $DBNAME < schema.sql
echo "Done creating DB."

# echo "Copying feature files to the database..."
# for file in `find $DATA_DIR -name "*.feat"`; do 
# 	# copy data files into the original_gratures table
#     psql $DBNAME -c "COPY original_features FROM STDIN CSV DELIMITER E'\t' HEADER;" < $file
# done
# echo "Done copying feature files."

echo "Loading metadata features..."
psql $DBNAME -c "COPY person_meta_features FROM STDIN CSV HEADER;" < $METADATA
echo "Done loading metadata."


echo "Loading prosodic features..."
psql $DBNAME -c "COPY prosodic_features FROM STDIN CSV HEADER;" < $PROSODIC_FEATURES
echo "Done loading prosodic features."

echo "Loading output labels..."
psql $DBNAME -c "COPY output_labels FROM STDIN CSV HEADER;" < $OUTPUT
echo "Done loading output labels."

echo "Loading textual features..."
psql $DBNAME -c "COPY textual_features FROM STDIN CSV HEADER;" < $TEXTUAL
echo "Done loading textual features."
#! /bin/bash

echo "Creating the database..."
dropdb $DBNAME
createdb $DBNAME
psql $DBNAME < schema.sql
echo "Done creating DB."

echo "Copying feature files to the database..."
for file in `find $DATA_DIR -name "*.feat"`; do 
	# copy data files into the original_gratures table
    psql $DBNAME -c "COPY original_features FROM STDIN CSV DELIMITER E'\t' HEADER;" < $file
done
echo "Done copying feature files."

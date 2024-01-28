# Spark Iceberg Minio Trino

This setup is the same as the Spark Iceberg one, except this one includes a Trino configured so that you can run queries against the Iceberg data lake.

## Setup

To load data into iceberg, you put `parquet` files inside `load_data/data`.
Then, to change the schema that data gets loaded into, you just change the `iceberg_schema` variable in the `load_data_into_iceberg.py` script.

# Python Standard Library Imports
import pathlib

# Third Party Imports
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("Load Data").getOrCreate()

    iceberg_schema = "bootcamp"

    spark.sql(
    f"""
    CREATE DATABASE IF NOT EXISTS {iceberg_schema}
    """
    )

    path_to_data = pathlib.Path("/data")

    for path_to_data_file in path_to_data.iterdir():
        if ".gitkeep" not in path_to_data_file.as_posix():
            df = spark.read.parquet(path_to_data_file.as_posix())
            df.write.saveAsTable(f"{iceberg_schema}.{path_to_data_file.stem}")

    spark.stop()

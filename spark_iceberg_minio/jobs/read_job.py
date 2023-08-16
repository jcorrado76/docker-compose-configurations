from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder \
    .appName("Spark Iceberg MinIO") \
    .getOrCreate()

    df = spark.table("demo.nyc.taxis").show()

if __name__ == "__main__":
    main()
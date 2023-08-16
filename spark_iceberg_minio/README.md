# Spark and Apache Iceberg

The purpose of this subdirectory is to stand up:

- a spark standalone cluster
- a minio cluster running over local files
- apache iceberg

The instructions were taken from [the apache iceberg docs](https://iceberg.apache.org/spark-quickstart/).

## Usage

To stand up the spark, minio and apache iceberg, run:

```bash
make up
```

You can start Spark shells with the following:

```bash
docker exec -it spark-iceberg spark-sql
docker exec -it spark-iceberg spark-shell
docker exec -it spark-iceberg pyspark
```

You can launch a notebook on `http://localhost:8888` with :

```bash
docker exec -it spark-iceberg notebook
```

The `minio` container is configured to mount a local folder called `data` onto `/data`. After running `make up`, this folder will be created in your workspace.

### Create a table

You can create a table with the following command:

In python:

```python
from pyspark.sql.types import DoubleType, FloatType, LongType, StructType,StructField, StringType
schema = StructType([
  StructField("vendor_id", LongType(), True),
  StructField("trip_id", LongType(), True),
  StructField("trip_distance", FloatType(), True),
  StructField("fare_amount", DoubleType(), True),
  StructField("store_and_fwd_flag", StringType(), True)
])

df = spark.createDataFrame([], schema)
df.writeTo("demo.nyc.taxis").create()
```

In Scala:

```scala
import org.apache.spark.sql.types._
import org.apache.spark.sql.Row
val schema = StructType( Array(
    StructField("vendor_id", LongType,true),
    StructField("trip_id", LongType,true),
    StructField("trip_distance", FloatType,true),
    StructField("fare_amount", DoubleType,true),
    StructField("store_and_fwd_flag", StringType,true)
))
val df = spark.createDataFrame(spark.sparkContext.emptyRDD[Row],schema)
df.writeTo("demo.nyc.taxis").create()
```

In SQL:

```sql
CREATE TABLE demo.nyc.taxis
(
  vendor_id bigint,
  trip_id bigint,
  trip_distance float,
  fare_amount double,
  store_and_fwd_flag string
)
PARTITIONED BY (vendor_id);
```

### Writing Data to Table

SQL:

```sql
INSERT INTO demo.nyc.taxis
VALUES (1, 1000371, 1.8, 15.32, 'N'), (2, 1000372, 2.5, 22.15, 'N'), (2, 1000373, 0.9, 9.01, 'N'), (1, 1000374, 8.4, 42.13, 'Y');
```

Scala:

```scala
import org.apache.spark.sql.Row

val schema = spark.table("demo.nyc.taxis").schema
val data = Seq(
    Row(1: Long, 1000371: Long, 1.8f: Float, 15.32: Double, "N": String),
    Row(2: Long, 1000372: Long, 2.5f: Float, 22.15: Double, "N": String),
    Row(2: Long, 1000373: Long, 0.9f: Float, 9.01: Double, "N": String),
    Row(1: Long, 1000374: Long, 8.4f: Float, 42.13: Double, "Y": String)
)
val df = spark.createDataFrame(spark.sparkContext.parallelize(data), schema)
df.writeTo("demo.nyc.taxis").append()
```

Python:

```python
schema = spark.table("demo.nyc.taxis").schema
data = [
    (1, 1000371, 1.8, 15.32, "N"),
    (2, 1000372, 2.5, 22.15, "N"),
    (2, 1000373, 0.9, 9.01, "N"),
    (1, 1000374, 8.4, 42.13, "Y")
  ]
df = spark.createDataFrame(data, schema)
df.writeTo("demo.nyc.taxis").append()
```

### Reading Data from Table

SQL:

```sql
SELECT * FROM demo.nyc.taxis;
```

Scala:

```scala
val df = spark.table("demo.nyc.taxis").show()
```

Python:

```python
df = spark.table("demo.nyc.taxis").show()
```

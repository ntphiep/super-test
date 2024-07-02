
from pyspark.sql import SparkSession

# Tạo SparkSession
spark = SparkSession.builder \
    .appName("PostgresSparkConnect") \
    .config("spark.jars", "./libs/postgresql-42.2.2.jar") \
    .getOrCreate()


url = "jdbc:postgresql://localhost:5432/dbt"
properties = {
    "user": "dbt",
    "password": "dbt",
    "driver": "org.postgresql.Driver"
}

# Đọc dữ liệu từ PostgreSQL
df_orders = spark.read.jdbc(url=url, table="raw_layer.orders", properties=properties)
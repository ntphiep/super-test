from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
import sqlalchemy
import pandas as pd



spark = SparkSession.builder \
    .appName("GCSExample") \
    .config("spark.hadoop.fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem") \
    .config("spark.hadoop.google.cloud.auth.service.account.enable", "true") \
    .config("spark.hadoop.google.cloud.auth.service.account.json.keyfile", "../keys/hiep-develope-817847506401.json") \
    .config("spark.jars", "./libs/gcs-connector-hadoop3-2.2.5.jar") \
    .getOrCreate()




df = spark.read.csv("gs://hiep_bk_1/NASDAQ_1962-2024.csv", header=True, inferSchema=True)

df.show()


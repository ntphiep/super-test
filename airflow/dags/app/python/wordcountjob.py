from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PythonWordCountFin").getOrCreate()

text = "Hello Spark Hello Python Hello Airflow Hello Docker and Hello Hiep"

words = spark.sparkContext.parallelize(text.split(" "))

wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

for wc in wordCounts.collect():
    print(wc[0], wc[1])

spark.stop()
import sys
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession



conf = SparkConf() \
    .setAppName("Spark Hello World") \
    .setMaster("spark://spark:7077")
sc = SparkContext(conf=conf)

# Create spark context

# Get the second argument passed to spark-submit (the first is the python app)
logFile = sys.argv[1]

# Read file
logData = sc.textFile(logFile).cache()

# Get lines with A
numAs = logData.filter(lambda s: 'a' in s).count()

# Get lines with B 
numBs = logData.filter(lambda s: 'b' in s).count()

# Print result
print("Lines with a: {}, lines with b: {}".format(numAs, numBs))
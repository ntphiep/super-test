from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext


spark = SparkSession.builder \
    .appName("StreamingWordCount") \
    .getOrCreate()
sc = spark.sparkContext


# Tạo một StreamingContext với khoảng thời gian nhỏ nhất 1 giây
ssc = StreamingContext(sc, 1)

# Kết nối đến cổng localhost 9999 để nhận dữ liệu
lines = ssc.socketTextStream("localhost", 9999)

# Phân tách các từ từ dòng dữ liệu
words = lines.flatMap(lambda line: line.split(" "))

# Đếm số lượng từ
word_counts = words.map(lambda word: (word, 1)).reduceByKey(lambda x, y: x + y)

word_counts.pprint()

# Khởi động quá trình xử lý dữ liệu liên tục
ssc.start()

# Đợi quá trình kết thúc
ssc.awaitTermination()

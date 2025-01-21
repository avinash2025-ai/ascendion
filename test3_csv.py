from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

#read CSV into PySpark DataFrame
df = spark.read.csv('people_data.csv',header=True)

#view resulting DataFrame
df.show()
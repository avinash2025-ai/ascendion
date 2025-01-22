from pyspark.sql import SparkSession
from pyspark.sql.types import *

spark = SparkSession.builder.getOrCreate()

#read CSV into PySpark DataFrame
df = spark.read.csv('people_data.csv',header=True)

#view resulting DataFrame
df.show()

df.createOrReplaceTempView("peoples")
spark.sql("select email,sex from peoples").show()
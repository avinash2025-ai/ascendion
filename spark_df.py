from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("Sparksql").getOrCreate()

print(spark.version)

df = spark.read.csv("people_data.csv",header=True)
#df.select("First Name","Sex","Job Title").show()
#df.filter(col("Sex") == "Male").show()
#df.orderBy("First Name").show()
#df.groupBy("Sex").count().show()
# df = df.withColumnRenamed("Date of birth", "DOB")\
#        .withColumnRenamed("Job Title", "Position")
df.show()

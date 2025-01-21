from pyspark.sql import SparkSession
from pyspark.sql.types import *

spark = SparkSession.builder.getOrCreate()

data = [
    ("Avinash","Singh",9916636372,50000),
    ("Aviraj","Singh",9916636372,20000),
    ("Aviyanka","Singh",9916636372,40000),
    ("Avinav","Singh",9916636372,30000),
    ("Avimanyu","Singh",9916636372,70000),
]

# schema = StructType([
#    StructField("FirstName", StringType(), True),
#    StructField("LastName", IntegerType(), True),
#    StructField("Mobile", StringType(), True),
#    StructField("Salary", IntegerType(), True)
#    ])


columns = ["FirstName","LastName","Mobile","Salary"]

df = spark.createDataFrame(data=data,schema=columns)
# show table 
df.show() 

# show schema 
df.printSchema() 


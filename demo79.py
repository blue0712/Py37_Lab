import pyspark
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("python lab1").getOrCreate()
print(spark.sparkContext.getConf().getAll())
#spark.sparkContext.stop()

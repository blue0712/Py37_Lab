import os

import pyspark
from pyspark import SparkConf, SparkContext

print(pyspark.__version__)

config = SparkConf().setAppName("python lab1").setMaster("local")
sc = SparkContext(conf=config)
print(sc.getConf().getAll())
print(os.getcwd())
file1 = sc.textFile('data\\shilin.csv')
print("file line={}".format(file1.count()))
#sc.stop()

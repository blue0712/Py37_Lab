import os

import pyspark
from pyspark import SparkConf, SparkContext

print(pyspark.__version__)

config = SparkConf().setAppName("python lab1").setMaster("local")
sc = SparkContext(conf=config)
print(sc.getConf().getAll())
print(os.getcwd())
# copy from spark installation
file1 = sc.textFile('data\\README.md')
print("file total line count ={}".format(file1.count()))
print("file first line:{}".format(file1.first()))
print("file 3 lines:{}".format(file1.take(3)))
print("all lines:{}".format(file1.collect()))
print("lines contains A:{}".format(file1.filter(lambda s: "a" in s).count()))
print("sample 5 lines in file:{}".format(file1.takeSample(False, 5)))
# sc.stop()


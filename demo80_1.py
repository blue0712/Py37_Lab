from pyspark import SparkConf, SparkContext
import re

config = SparkConf().setAppName("python lab1").setMaster("local")
sc = SparkContext(conf=config)
file1 = sc.textFile('data\\README.md')

print("map file1:{}".format(file1.map(lambda s: s.split(' ')).collect()))
print('map using regular expression:{}'.format(
    file1.map(lambda s: re.compile('\\s+').split(s)).collect()))
print("flat map file1:{}".format(file1.flatMap(lambda s: s.split(' ')).collect()))
print("count file1:{}".format(file1.map(lambda s: (len(s), s)).take(5)))
result1 = file1.map(lambda s: (len(s), s)).countByKey()
print("result1=", result1)
lineLength = file1.map(lambda s: len(s))
print("total per line length:", lineLength.collect())
totalLength = lineLength.reduce(lambda a, b: a + b)
print("total length=", totalLength)
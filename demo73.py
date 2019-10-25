import pandas
from matplotlib import pyplot, rc

data = pandas.read_csv('data\\data1.csv', skiprows=4, index_col="Country Name")
print(data.shape)
print(data.head(n=10))
print(data.columns)
import pandas
from matplotlib import pyplot, rc

data = pandas.read_csv('data\\data1.csv', skiprows=4, index_col="Country Name")
print(data.shape)
print(data.head(n=10))
print(data.columns)
print(data.info())
print(data.describe())

ausData = data[data['Country Code'] == 'AUS']
print(ausData.shape)
print(ausData['1960'])
print(type(data), type(ausData))
print(pyplot.style.available)
font = {'family':"Source Code Pro"}
rc('font',**font)
pyplot.style.use('dark_background')
selected_years = ['1960','1965','1970','1975']
ausData.plot(kind='bar', y=selected_years)
pyplot.show()
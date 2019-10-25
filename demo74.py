import pandas as pd
import folium

sample_data = pd.read_csv('data\\shilin.csv', sep=',', encoding='ms950')
print(sample_data.columns)
print(sample_data.info())
print(sample_data.describe())
print(sample_data.head(n=10))
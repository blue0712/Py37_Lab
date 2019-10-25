import pandas as pd
import folium

sample_data = pd.read_csv('data\\shilin.csv', sep=',', encoding='ms950')
print(sample_data.columns)
print(sample_data.info())
print(sample_data.describe())
sample_data.columns = ['section', 'road', 'road_detail', 'lon', 'lat', 'extra']
print(sample_data.head(n=10))

center = [25.090084, 121.524956]
zoom = 17
map_osm = folium.Map(location=center, zoom_start=zoom)

map_osm.save('map\\demo74_1.html')
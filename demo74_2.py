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

for i in range(len(sample_data)):
    coordinate = [sample_data.iloc[i, 4], sample_data.iloc[i, 3]]
    icon1 = folium.Icon(color='black',icon='info-sign')
    folium.Marker(coordinate, icon=icon1, popup=None).add_to(map_osm)

map_osm.save('map\\demo74_2.html')
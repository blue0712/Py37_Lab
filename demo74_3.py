import pandas as pd
import folium

sample_data = pd.read_csv('data\\shilin.csv', sep=',', encoding='ms950')
print(sample_data.columns)
print(sample_data.info())
print(sample_data.describe())
sample_data.columns = ['section', 'road', 'road_detail', 'lon', 'lat', 'extra']
print(sample_data.head(n=10))

center = [25.090084, 121.524956]
zoom = 15
map_osm = folium.Map(location=center, zoom_start=zoom)

for i in range(len(sample_data)):
    coordinate = [sample_data.iloc[i, 4], sample_data.iloc[i, 3]]
    debugMessage = f"[{i}]{sample_data.iloc[i, 1]}{sample_data.iloc[i, 2]}"
    icon1 = folium.Icon(color='black', icon='info-sign')
    folium.Marker(coordinate, icon=icon1, popup=debugMessage).add_to(map_osm)

POI1 = [25.052232, 121.544655]

folium.CircleMarker(POI1, radius=50, popup='Brother Hotel',
                    fill_color='#C0FFEE').add_to(map_osm)

POI2 = [25.047302, 121.517270]
POI3 = [25.053099, 121.606962]
folium.Circle(POI2, radius=800, popup='Taipei Station',
              fill_color='#C0EEFF').add_to(map_osm)
folium.Circle(POI3, radius=800, popup='Nangang Station',
              fill_color='#FFC0EE').add_to(map_osm)

map_osm.save('map\\demo74_3.html')
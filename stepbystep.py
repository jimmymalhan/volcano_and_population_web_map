import folium

#S 1

map = folium.Map(location=[80, -100]) #Location for latitude longitude ranges [90 to -90 & 180 to -180]
# creates a new file as html. 
map.save("Map1.html") #random location # Go ahead open the file to see the location of your latitude and longitude

#S 2

#Create a file for your favorite location i.e Santa Monica,LA,CA.
#Go to maps.google.com and click on the location to get coordinates.
map = folium.Map(location=[34.016, -118.503], zoom_start=20) #adding zoom parameter as default view of the file
map.save("losangeles.html")

#S 3

map = folium.Map(location=[34.016, -118.503], zoom_start=20, tiles="Stamen Terrain") #adding tiles to change the view of the output
map.save("losangeles2.html")

#S 4

map = folium.Map(location=[34.016, -118.503], zoom_start=20, tiles="Stamen Terrain")
map.add_child(folium.Marker(location=[34.016, -118.503], popup="Look here, I am your Marker", icon=folium.Icon(color='green'))) #Adding marker
map.save("losangeles3.html")

#S 5

map = folium.Map(location=[34.016, -118.503], zoom_start=20, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map") #fg= feature group which helps control layer features
fg.add_child(folium.Marker(location=[34.016, -118.503], popup="Look here, I am your Marker", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("losangeles4.html")

#S 6

map = folium.Map(location=[34.016, -118.503], zoom_start=20, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for coordinates in [[34.016, -118.503],[33.016, -117.503]]: #Adding Multiple markers
    fg.add_child(folium.Marker(location=coordinates, popup="Look here, I am your Marker", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("losangeles5.html")

#S 7
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

map = folium.Map(location=[34.016, -118.503], zoom_start=20, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lt,ln in zip(lat, lon): #to iterate through list - zip is used
    fg.add_child(folium.Marker(location=[lt, ln], popup="Look here, I am your Marker", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("losangeles6.html")

#S 8
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[34.016, -118.503], zoom_start=20, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lt,ln,el in zip(lat, lon, elev): #to iterate through list - zip is used
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+"m", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("losangeles7.html")



print(map)

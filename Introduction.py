import folium

map = folium.Map(location=[80, -100]) #Location for latitude longitude ranges [90 to -90 & 180 to -180]
# create a new file as html. 
map.save("Map1.html") # Go ahead open the file to see the location of your latitude and longitude

#Create a file for your favorite location i.e Santa Monica,LA,CA.
#Go to maps.google.com and click on the location to get coordinates.
map = folium.Map(location=[34.016, -118.503], zoom_start=20) #adding zoom parameter as default view of the file
map.save("losangeles.html")

print(map)

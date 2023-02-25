import folium
import pandas as pd
import subprocess
import googlemaps

'''url = (
    "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
)
state_geo = f"{url}/us-states.json"'''

# Google Api Key
apiKey = "AIzaSyCmPfH0DVs9d2z8foYZS_TU9sSrFwQWyFM"

# Adding Google Maps
gmaps = googlemaps.Client(key= apiKey)

# Create a map centered on the United States
m = folium.Map(location=[37, -102], zoom_start=4)

# Add Markers for locations

#Add a single marker

import requests

# Geocoding an address
geocode_result = gmaps.geocode('4125 Radio Dr, Woodbury, MN 55129')
print(geocode_result)
geometry_dict = geocode_result[0].get('geometry').get('location')
print(geometry_dict)
folium.Marker(location=[geometry_dict.get('lat'), geometry_dict.get('lng')]).add_to(m)

'''
# import USHL Dates
ushlDates = pd.read_csv('ushl-tryouts.csv')
# Do something with the output
for index, row in ushlDates.iterrows():
    print(row["Team"], row["Website"], row["Tryouts"])'''

# Save the map as an HTML file
m.save('map.html')

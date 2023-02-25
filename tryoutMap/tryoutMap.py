import folium
import pandas as pd
import subprocess
import googlemaps
from configparser import ConfigParser

config = ConfigParser()

config.read('../keys_config.cfg')

apiKey = config.get('google', 'apiKey')

'''url = (
    "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
)
state_geo = f"{url}/us-states.json"'''

# Adding Google Maps
gmaps = googlemaps.Client(key= apiKey)

# Create a map centered on the United States
m = folium.Map(location=[37, -102], zoom_start=4)

# Add Markers for locations

#Add a single marker

import requests

# Geocoding an address
geocode_result = gmaps.geocode('4125 Radio Dr, Woodbury, MN 55129')
# Gathering the Geolocation data
geometry_dict = geocode_result[0].get('geometry').get('location')
# Setup the content of the popup
tooltip = "Click me!"
iframe = folium.IFrame('Tryout Information: ' + 'Cedar Rapids RoughRiders\nhttp://www.roughridershockey.com/\n Futures Camp - June 10-12\n- HealthEast Sports Center in Woodbury, Minnesota')

# Initialise the popup using the iframe
popup = folium.Popup(iframe, min_width=300, max_width=300)

folium.Marker(location=[geometry_dict.get('lat'), geometry_dict.get('lng')],
              popup = popup,
              tooltip= tooltip).add_to(m)

'''
# import USHL Dates
ushlDates = pd.read_csv('ushl-tryouts.csv')
# Do something with the output
for index, row in ushlDates.iterrows():
    print(row["Team"], row["Website"], row["Tryouts"])'''

# Save the map as an HTML file
m.save('map.html')

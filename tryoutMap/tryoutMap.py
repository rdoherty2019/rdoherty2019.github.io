import folium
import pandas as pd
import subprocess

'''url = (
    "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
)
state_geo = f"{url}/us-states.json"'''

# Create a map centered on the United States
m = folium.Map(location=[37, -102], zoom_start=4)

# Add the GeoJSON data for the US states
"""folium.GeoJson(
    state_geo
).add_to(m)"""

# Add Markers for locations

#Add a single marker

'''import requests
# Set the URL and parameters for the Geocoding API
urlGoogle = "https://maps.googleapis.com/maps/api/geocode/json"
params = {"address": "1600 Amphitheatre Parkway, Mountain View, CA", "key": "YOUR_API_KEY"}

# Send a GET request to the API
response = requests.get(url, params=params)

# Parse the JSON response and extract the latitude and longitude
data = response.json()
lat = data["results"][0]["geometry"]["location"]["lat"]
lng = data["results"][0]["geometry"]["location"]["lng"]

# Print the latitude and longitude
print("Latitude:", lat)
print("Longitude:", lng)

folium.Marker(location=[df.Latitude.mean(), df.Longitude.mean()]).add_to(map)

# import USHL Dates
ushlDates = pd.read_csv('ushl-tryouts.csv')
# Do something with the output
for index, row in ushlDates.iterrows():
    print(row["Team"], row["Website"], row["Tryouts"])'''

# Save the map as an HTML file
m.save('map.html')

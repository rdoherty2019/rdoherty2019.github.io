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

# import USHL Dates
ushlDates = pd.read_csv('ushl-tryouts.csv')
# Do something with the output


# Save the map as an HTML file
m.save('map.html')

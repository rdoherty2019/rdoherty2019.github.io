import folium

# Create a map centered on the United States
m = folium.Map(location=[37, -102], zoom_start=4)

# Add the GeoJSON data for the US states
"""folium.GeoJson(
    'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data',
    name='US States'
).add_to(m)"""

# Add Markers for locations

# Save the map as an HTML file
m.save('map.html')

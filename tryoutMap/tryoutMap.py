import folium
import pandas as pd
import subprocess
import googlemaps
from configparser import ConfigParser
import requests

# Import API Keys
config = ConfigParser()
## Read in config file
config.read('../keys_config.cfg')
## Find API Key for Google
apiKey = config.get('google', 'apiKey')

# Import Files
## import USHL Tryout Dates
ushlTryouts = pd.read_csv('ushl-tryouts.csv')
## import USHL Teams
ushlTeams = pd.read_csv('ushlTeams.csv')

## Adding Google Maps
gmaps = googlemaps.Client(key= apiKey)

# Create a map centered on the United States
m = folium.Map(location=[37, -102], zoom_start=4)

# Add Markers for locations

#Add a single marker



## Geocoding an address
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

## Multilpe Markers
### Iterate through teams
for index, row in ushlTeams.iterrows():
    # Find all the tryout dates for the specifc team
    temp = ushlTryouts[ushlTryouts["Team"]==row["Team"]]
    # Determine if there are any tryouts
    if temp.empty:
        # If there aren't tryouts return this string
        print("The", row["Team"], "has not posted any tryouts. Please check again in the future.")
    else:
        # If there are tryouts group them all together into a set of strings
        # Might want to leave as seperate rows we will see
        grouped_df = temp.groupby('Team')['Tryouts'].apply('\n'.join)
        print(grouped_df)


# Save the map as an HTML file
m.save('map.html')

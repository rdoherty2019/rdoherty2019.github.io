import folium
import pandas as pd
import subprocess
import googlemaps
from configparser import ConfigParser
from geopy.geocoders import GoogleV3
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
## Creating Geolocator
geolocator = GoogleV3(api_key=apiKey)

# Create a map centered on the United States
m = folium.Map(location=[37, -102], zoom_start=4)

# Add Markers for locations

'''#Add a single marker
## Geocoding an address
address = geolocator.geocode("Chicago Steel")
## Finding the Geocode location
geocode_result = gmaps.geocode(address)
## Indexing out the Geolocation data
geometry_dict = geocode_result[0].get('geometry').get('location')
## Setup the content of the popup
tooltip = "Click me!"
iframe = folium.IFrame('Tryout Information: ' + 'Cedar Rapids RoughRiders\nhttp://www.roughridershockey.com/\n Futures Camp - June 10-12\n- HealthEast Sports Center in Woodbury, Minnesota')

## Initialise the popup using the iframe
popup = folium.Popup(iframe, min_width=300, max_width=300)

## Adding the marker
folium.Marker(location=[geometry_dict.get('lat'), geometry_dict.get('lng')],
              popup = popup,
              tooltip= tooltip).add_to(m)'''

## Multilpe Markers
### Iterate through teams
for index, row in ushlTeams.iterrows():
    # Find the Address
    address = geolocator.geocode(row["Team"])
    if address == None:
        continue
    # Finding the Geocode location
    geocode_result = gmaps.geocode(address)
    # Indexing out the Geolocation data
    geometry_dict = geocode_result[0].get('geometry').get('location')
    # Find all the tryout dates for the specifc team
    temp = ushlTryouts[ushlTryouts["Team"]==row["Team"]]
    # Determine if there are any tryouts
    if temp.empty:
        # If there aren't tryouts return this string
        content = "The "+ row["Team"] + " has not posted any tryouts. Please check again in the future."
        # Default website for no tryout info
        website = 'https://ushl.sportngin.com/page/show/1209138-team-tryouts'
    else:
        # If there are tryouts group them all together into a set of strings
        # Might want to leave as seperate rows we will see
        content = '\n'.join(temp["Tryouts"])
        # Find Website for team.
        website = temp.iloc[0,1]
    ## Setup the content of the popup
    tooltip = "Click me!"
    iframe = folium.IFrame(
        'Tryout Information: ' + content + '\nFor more information: '+ website )

    ## Initialise the popup using the iframe
    popup = folium.Popup(iframe, min_width=300, max_width=300)

    ## Adding the marker
    folium.Marker(location=[geometry_dict.get('lat'), geometry_dict.get('lng')],
                  popup=popup,
                  tooltip=tooltip).add_to(m)

# Save the map as an HTML file
m.save('map.html')

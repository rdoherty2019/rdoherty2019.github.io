from bs4 import BeautifulSoup
import requests

# Importing the first time

# United States Hockey League Tryout URL
#url = "https://ushl.sportngin.com/page/show/1209138-team-tryouts"

# Get the HTML Data from that URL
#r = requests.get(url)

# Save File to retrieve later, less web scrapes
#with open('ushlTryouts.txt', 'w') as file:
   # file.write(r.text)

# Opening the html file. If the file
# is present in different location,
# exact location need to be mentioned
HTMLFileToBeOpened = open("ushlTryouts.txt", "r")

# Reading the file and storing in a variable
contents = HTMLFileToBeOpened.read()

# parse the HTML Data from the file variable
soup = BeautifulSoup(contents, 'html.parser')

# Get the titles of the page
title_element = soup.head.title
if title_element:
    title = title_element.string
else:
    title = None

# Get the headers and text within each `<div class="description">`
descriptions = soup.find_all("div", {"class": "description"})
# Find all the dates
dates = soup.find_all("div", {"class": "text clearfix"})
# Container to hold all of the output data
catcher = []
counter = 0
for description in descriptions:
    # Find all the team titles
    header_element = description.h3
    if header_element:
        header = header_element.string
    else:
        header = None
    # Find all the team links
    link = description.a
    # Extract the `href` attribute
    href = link.get("href")
    dateList = []
    date = dates[counter].find_all("p")
    for tag in date:
        dateList.append(tag.text)
    counter +=1
    catcher.append([header, href, dateList])
print(catcher)
#!/bin/python

import requests
import pycountry
import json
import unicodedata
from bs4 import BeautifulSoup

def unicodeNormalizeCasefold(str):
    return unicodedata.normalize("NFKD", str).casefold()

# URL to crawl, note that all data is taken straight from the wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_alternative_country_names"

# Make a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

# Initialize an empty list to store the data
data = []

# Find the table containing the data
for table in soup.find_all("table", {"class": "wikitable"}):
    # Iterate over each row in the table
    for row in table.find_all("tr")[1:]:
        # Initialize an empty list to store the data for each row
        cells = row.find_all("td")
        row_data = []

        # Only consider rows with an alpha-3 country code present
        countryCodeAlpha3 = cells[0].text.strip()
        if(countryCodeAlpha3 != ""):
            # Lookup the country using the alpha-3 code
            country = pycountry.countries.get(alpha_3=countryCodeAlpha3)

            isoAlternateNames = []
            wikiAlternateNames = []
            wikipediaName = unicodeNormalizeCasefold(cells[1].find("a").text.strip())

            # Add the official name and common name from the pycountry library if they exist
            if hasattr(country, 'official_name'):
                isoAlternateNames.append(unicodeNormalizeCasefold(country.official_name))
            if hasattr(country, 'common_name'):
                isoAlternateNames.append(unicodeNormalizeCasefold(country.common_name))

            # Add the wikipedia name if it is unique
            if wikipediaName != unicodeNormalizeCasefold(country.name) and wikipediaName not in isoAlternateNames:
                wikiAlternateNames.append(wikipediaName)    

            # Get the alternative names which are in <b> tags
            for name in cells[2].find_all("b"):
                alternateName = unicodeNormalizeCasefold(name.text.strip())
                if alternateName != unicodeNormalizeCasefold(country.name) and alternateName not in isoAlternateNames:
                    wikiAlternateNames.append(unicodeNormalizeCasefold(alternateName))

            # Add the row data to the overall data
            data.append({
                "name": country.name,
                "alpha_2": country.alpha_2,
                "alpha_3": country.alpha_3,
                "numeric": country.numeric,
                "iso_alternate": isoAlternateNames,
                "wikipedia_alternate": list(set(wikiAlternateNames))
            })

# Print the array
print(json.dumps(data, indent=2))
# Country Names Scraper

This Python script extracts alternative country names from Wikipedia and cross-references them with the `pycountry` library. It outputs a comprehensive list of countries with their standard and alternative names, considering both ISO standards and Wikipedia entries.

## Features

- **Wikipedia Parsing:** Scrapes the "List of alternative country names" page on Wikipedia.
- **ISO Name Matching:** Cross-references Wikipedia names with the `pycountry` library to obtain official and common names as per ISO standards.
- **Unicode Normalization:** Utilizes Unicode normalization and case-folding for consistency in name comparison.
- **Data Consolidation:** Outputs a JSON array with country names, ISO alpha-2, alpha-3, numeric codes, and lists of ISO and Wikipedia alternative names.

## Requirements

- Python 3
- `requests`
- `pycountry`
- `BeautifulSoup4`

## Installation

To run this script, you need to have Python 3 installed along with the required packages. You can install the required packages using pip:

````bash
pip install requests pycountry beautifulsoup4
````

## Usage

Run the script with Python:

````bash
python country-scraper.py
````

The script will output to stdout the data in JSON format, which includes the standard names and alternative names (both from ISO and Wikipedia) for each country.

## Output Format

The JSON output includes:

* `name`: Standard country name
* `alpha_2`: ISO alpha-2 code
* `alpha_3`: ISO alpha-3 code
* `numeric`: ISO numeric code
* `iso_alternate`: List of alternative names as per ISO
* `wikipedia_alternate`: List of alternative names from Wikipedia

Example:

````json
  {
    "name": "Austria",
    "alpha_2": "AT",
    "alpha_3": "AUT",
    "numeric": "040",
    "iso_alternate": [
      "republic of austria"
    ],
    "wikipedia_alternate": [
      "republik o\u0308sterreich",
      "o\u0308sterreich"
    ]
  },
````
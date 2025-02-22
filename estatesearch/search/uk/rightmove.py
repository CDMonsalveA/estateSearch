"""
This module contains the Rightmove class 
which is used to search for properties on
the Rightmove website.

rightmove.co.uk is a property search engine
that allows users to search for properties
for sale or rent in the UK.

check out the website at: https://www.rightmove.co.uk/
and the robots.txt file at: https://www.rightmove.co.uk/robots.txt
"""

import requests

class Rightmove:
    """
    The Rightmove class is used to search for properties
    on the Rightmove website using the following parameters:

    - Buy / Rent
    - Location (town, city, postcode)
    - Radius (miles)
    - Price range (min, max)
    - Number of bedrooms (min, max)
    - Type of property (
        Any, 
        Houses, 
        Flats / Apartments, 
        Bungalows, 
        Land, Commercial Property, 
        Other
        )
    - Added to site (
        24 hours, 
        3 days, 
        7 days, 
        14 days
        )
    - Include Under Offer, Sold STC (Yes / No)
    """

    def __init__(self):
        self.url = "https://www.rightmove.co.uk/"
        pass

    def connect(self):
        """
        Check if the website is reachable
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            return False
        

        
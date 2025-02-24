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

class Rightmove:
    """
    The Rightmove class is used to search for properties
    on the Rightmove website using the following parameters:

    Example URL:
    - https://www.rightmove.co.uk/property-for-sale/find.html?searchLocation=ME2&useLocationIdentifier=true&locationIdentifier=OUTCODE%5E1619&radius=0.25&minPrice=50000&maxPrice=70000&minBedrooms=1&maxBedrooms=2&propertyTypes=detached%2Csemi-detached%2Cterraced&maxDaysSinceAdded=1&_includeSSTC=on&includeSSTC=true
    - https://www.rightmove.co.uk/api/_search?locationIdentifier=POSTCODE%5E1149959&numberOfPropertiesPerPage=24&radius=0.5&sortType=2&index=0&includeSSTC=false&viewType=LIST&channel=BUY&areaSizeUnit=sqft&currencyCode=GBP&isFetching=false&viewport=


    - Buy / Rent property-for-sale, property-to-rent + /find.html?
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

    def __init__(
        self,
        buy_or_rent=None,
        location=None,
        radius=None,
        min_price=None,
        max_price=None,
        min_bedrooms=None,
        max_bedrooms=None,
        property_types=None,
        max_days_since_added=None,
        include_sstc=None,
    ):
        """
        Initialize the Rightmove class with the following parameters:

        Args:
            buy_or_rent (str): property-for-sale, property-to-rent
            location (str): The location of the property (town, city, postcode)
            radius (float): The radius in miles
            min_price (int): The minimum price of the property
            max_price (int): The maximum price of the property
            min_bedrooms (int): The minimum number of bedrooms
            max_bedrooms (int): The maximum number of bedrooms
            property_types (list): The type of property
            max_days_since_added (int): The maximum days since the property was added
            include_sstc (bool): Include properties that are under offer or sold
        """
        self.url = "https://www.rightmove.co.uk/"
        self.buy_or_rent = None  # property-for-sale, property-to-rent + /find.html?
        # https://www.rightmove.co.uk/property-for-sale/find.html?searchLocation=ME2&useLocationIdentifier=true&locationIdentifier=OUTCODE%5E1619&radius=0.25&minPrice=50000&maxPrice=70000&minBedrooms=1&maxBedrooms=2&propertyTypes=detached%2Csemi-detached%2Cterraced&maxDaysSinceAdded=1&_includeSSTC=on&includeSSTC=true
        # https://www.rightmove.co.uk/api/_search?locationIdentifier=POSTCODE%5E1149959&numberOfPropertiesPerPage=24&radius=0.5&sortType=2&index=0&includeSSTC=false&viewType=LIST&channel=BUY&areaSizeUnit=sqft&currencyCode=GBP&isFetching=false&viewport=
        self.api_url = "https://www.rightmove.co.uk/api/_search?"


    def search_properties(self):

        # create a valid URL to search for properties

        # Request URL

        # Extract properties from the response even with a second page

        # Return the properties
        pass

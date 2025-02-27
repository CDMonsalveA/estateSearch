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

    URL structure:
    - https://www.rightmove.co.uk/

        property-for-sale/||property-to-rent/

        find.html?||map.html?

        searchLocation=[postcode||town||city||train-station||county]
        &useLocationIdentifier=[true||false]
        &locationIdentifier=[type%locationId]
        &sortType=[1||2||3||4||5||6||7||8||9||10]
        &numberOfPropertiesPerPage=[int]
        &index=[int]
        &channel=[BUY||RENT]
        &areaSizeUnit=[sqft||sqm]
        &radius=[miles]
        &minPrice=[minPrice]
        &maxPrice=[maxPrice]
        &minBedrooms=[minBedrooms||studio=0]
        &maxBedrooms=[maxBedrooms||studio=0]
        &propertyTypes=[
                        bungalow
                        %2Cdetached
                        %2Cflat
                        %2Cland
                        %2Cpark-home
                        %2Csemi-detached
                        %2Cterraced
                        ]
        &maxDaysSinceAdded=[1||3||7||14]
        &_includeSSTC=[on||off]
        &includeSSTC=[true||false]
        &mustHave=[garden%2Cparking%2CnewHome%2Cretirement%2CsharedOwnership%2Cauction]
        &dontShow=[newHome%2Cretirement%2CsharedOwnership&furnishTypes]
        &furnishTypes=
        &keywords=
    """

    def __init__(
        self,
        buy_or_rent=("buy" or "rent"),
        location: str = None,
        radius: float = None,
        min_price: float = None,
        max_price: float = None,
        min_bedrooms: int = None,
        max_bedrooms: int = None,
        property_types: list = None,
        max_days_since_added: int = None,
        include_sstc: bool = False,
        must_have: list = None,
        dont_show: list = None,
    ):
        """
        Initialize the Rightmove class with the following parameters:

        :param buy_or_rent: str: The type of property to search for 
                                ('buy' or 'rent').
        :param location: str: The location to search for properties.
        :param radius: float: The radius from the location to search for 
                                properties.
        :param min_price: float: The minimum price of the property.
        :param max_price: float: The maximum price of the property.
        :param min_bedrooms: int: The minimum number of bedrooms.
        :param max_bedrooms: int: The maximum number of bedrooms.
        :param property_types: list: The type of properties to search for.
                                (bungalow, detached, flat, land, park-home,
                                semi-detached, terraced).
        :param max_days_since_added: int: The maximum number of days since 
                                the property was added.
        :param include_sstc: bool: Include properties that are sold subject
                                to contract.
        :param must_have: list: The features that the property must have.
                                (garden, parking, newHome, retirement,
                                sharedOwnership, auction).
        :param dont_show: list: The features that the property must not have.
                                (newHome, retirement, sharedOwnership).
        """

        self.url = "https://www.rightmove.co.uk/"
        self.api_url = "https://www.rightmove.co.uk/api/_search?locationIdentifier=POSTCODE%5E1149959&numberOfPropertiesPerPage=24&radius=0.5&sortType=2&index=0&includeSSTC=false&viewType=LIST&channel=BUY&areaSizeUnit=sqft&currencyCode=GBP&isFetching=false&viewport="
        self.house_prices_url = "https://www.rightmove.co.uk/house-prices/"
        self.radius = radius
        self.min_price = min_price
        self.max_price = max_price
        self.min_bedrooms = min_bedrooms
        self.max_bedrooms = max_bedrooms
        self.property_types = property_types
        self.max_days_since_added = max_days_since_added
        self.include_sstc = include_sstc
        self.must_have = must_have
        self.dont_show = dont_show

        # if location:
        #     self.location = location
        # else:
        #     raise ValueError("Invalid value for location.")

        # if buy_or_rent == "buy":
        #     self.buy_or_rent = "property-for-sale"
        # elif buy_or_rent == "rent":
        #     self.buy_or_rent = "property-to-rent"
        # else:
        #     raise ValueError("Invalid value for buy_or_rent.")
    
    def get_location_id(self):
        """
        Get the location ID from the
        rightmove.co.uk/house-prices/[location].html
        page.

        :return: str: Type of location ID.
        :return: str: The location ID.
        """

        pass

    def search_properties(self):

        # create a valid URL to search for properties

        # Request URL

        # Extract properties from the response even with a second page

        # Return the properties
        pass

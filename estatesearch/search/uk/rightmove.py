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

import json
import re

import requests


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
        &locationIdentifier=[type^locationId]
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
        &mustHave=[
                    garden
                    %2Cparking
                    %2CnewHome
                    %2Cretirement
                    %2CsharedOwnership
                    %2Cauction
                ]
        &dontShow=[newHome%2Cretirement%2CsharedOwnership&furnishTypes]
        &furnishTypes=
        &keywords=

    API structure:
    - https://www.rightmove.co.uk/api/_search?
        locationIdentifier=[type^locationId]
        &numberOfPropertiesPerPage=[int]
        &channel=BUY
        &sortType=[1||2||3||4||5||6||7||8||9||10]
        &index=[int]
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
        &mustHave=[
                    garden
                    %2Cparking
                    %2CnewHome
                    %2Cretirement
                    %2CsharedOwnership
                    %2Cauction
                ]
        &dontShow=[newHome%2Cretirement%2CsharedOwnership&furnishTypes]

        &viewType=LIST
        &areaSizeUnit=sqft
        &currencyCode=GBP
        &isFetching=false
        &viewport=
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
        self.api_url = "https://www.rightmove.co.uk/api/_search?"
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
        if location:
            self.location = location
        else:
            raise UserWarning("Please provide a location.")
        if buy_or_rent == "buy":
            self.buy_or_rent = "property-for-sale"
            self.channel = "BUY"
        elif buy_or_rent == "rent":
            self.buy_or_rent = "property-to-rent"
            self.channel = "RENT"
        else:
            self.buy_or_rent = "property-for-sale"
            self.channel = "BUY"
            raise UserWarning(
                "Please provide a valid buy or rent option.\n"
                "Options:  'buy' or 'rent'.\n"
                "Default: 'buy'."
            )

    def get_location_id_2(self):
        """
        Get the location ID from the
        rightmove.co.uk/house-prices/[location].html
        page. It is inserted into the script tag in the HTML.

        :return: str: Type of location ID.
        :return: str: The location ID.
        """
        search_url = f"{self.house_prices_url}{self.location}.html"
        response = requests.get(search_url)
        location_type = re.search(
            r'"locationType":"(\w+)"', response.text
        ).group(1)
        location_id = re.search(r'"locationId":(\d+)', response.text).group(1)
        return location_type, location_id

    def get_location_id(self):
        """
        Get the location ID from the
        https://los.rightmove.co.uk/typeahead?query=[location]
        page.

        :return: str: Type of location ID.
        :return: str: The location ID.
        """
        location_string = self.location
        for ch in [" ", ",", ".", "-", "_", "(", ")", "&"]:
            location_string = location_string.replace(ch, "+")

        search_url = (
            f"https://los.rightmove.co.uk/typeahead?query={location_string}"
        )
        response = requests.get(search_url)
        if response.status_code != 200:
            raise UserWarning(
                f"Invalid location: {self.location}", response.status_code
            )

        data = json.loads(response.text)["matches"]

        # if data is empty, raise user warning, invalid location
        if not data:
            raise UserWarning(
                f"Invalid location: {self.location}", response.status_code
            )
        data = data[0]
        location_type = data["type"]
        location_id = data["id"]
        return location_type, location_id

    @property
    def search_url(self):
        """
        Create a valid URL to search for properties.

        :return: str: The search URL.
        """
        location_ident = self.get_location_id()
        property_types = (
            "%2C".join(self.property_types) if self.property_types else None
        )
        must_have = "%2C".join(self.must_have) if self.must_have else None
        dont_show = "%2C".join(self.dont_show) if self.dont_show else None
        search_url = (
            f"{self.url}"
            f"{self.buy_or_rent}/"
            f"find.html?"
            f"searchLocation={self.location}"
            f"&useLocationIdentifier=true"
            f"&locationIdentifier={location_ident[0]}^{location_ident[1]}"
            f"&sortType=2"
            f"&numberOfPropertiesPerPage=1000"
            f"&index=0"
        )
        if self.radius:
            search_url += f"&radius={self.radius}"
        if self.min_price:
            search_url += f"&minPrice={self.min_price}"
        if self.max_price:
            search_url += f"&maxPrice={self.max_price}"
        if self.min_bedrooms:
            search_url += f"&minBedrooms={self.min_bedrooms}"
        if self.max_bedrooms:
            search_url += f"&maxBedrooms={self.max_bedrooms}"
        if self.property_types:
            search_url += f"&propertyTypes={property_types}"
        if self.max_days_since_added:
            search_url += f"&maxDaysSinceAdded={self.max_days_since_added}"
        if self.include_sstc:
            search_url += f"&includeSSTC={self.include_sstc}"
        if self.must_have:
            search_url += f"&mustHave={must_have}"
        if self.dont_show:
            search_url += f"&dontShow={dont_show}"

        search_url += "&furnishTypes=&keywords="
        search_url = search_url.replace(" ", "%20")
        return search_url

    def search_properties(self):

        # Request URL
        response = requests.get(self.search_url)
        return response
        # Extract properties from the response even with a second page

        # Return the properties
        pass

    @property
    def search_url_api(self):
        """
        Create a valid URL to search for properties using the API.

        :return: str: The search URL.
        """
        location_ident = self.get_location_id()
        property_types = (
            "%2C".join(self.property_types) if self.property_types else None
        )
        must_have = "%2C".join(self.must_have) if self.must_have else None
        dont_show = "%2C".join(self.dont_show) if self.dont_show else None
        search_url = (
            f"{self.api_url}"
            f"locationIdentifier={location_ident[0]}^{location_ident[1]}"
            f"&numberOfPropertiesPerPage=1000"
            f"&channel={self.channel}"
            f"&sortType=2"
            f"&index=0"
        )
        if self.radius:
            search_url += f"&radius={self.radius}"
        if self.min_price:
            search_url += f"&minPrice={self.min_price}"
        if self.max_price:
            search_url += f"&maxPrice={self.max_price}"
        if self.min_bedrooms:
            search_url += f"&minBedrooms={self.min_bedrooms}"
        if self.max_bedrooms:
            search_url += f"&maxBedrooms={self.max_bedrooms}"
        if self.property_types:
            search_url += f"&propertyTypes={property_types}"
        if self.max_days_since_added:
            search_url += f"&maxDaysSinceAdded={self.max_days_since_added}"
        if self.include_sstc:
            search_url += f"&includeSSTC={self.include_sstc}"
        if self.must_have:
            search_url += f"&mustHave={must_have}"
        if self.dont_show:
            search_url += f"&dontShow={dont_show}"
        search_url += "&viewType=LIST&areaSizeUnit=sqft&currencyCode=GBP&isFetching=false&viewport="
        return search_url

    def search_properties_api(self):
        """
        Search for properties using the API.

        :return: list: The properties."""

        # Request URL
        response = requests.get(self.search_url_api)
        data = json.loads(response.text)['properties']
        return response.text

    def get_properties(self):
        """
        Get the properties from the search URL.

        :return: list: The properties.
        """
        pass

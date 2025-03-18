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

import asyncio
import json
from typing import List

import jmespath
import requests
from httpx import AsyncClient, Response
from parsel import Selector

client = AsyncClient(
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,lt;q=0.8,et;q=0.7,de;q=0.6",
    },
    follow_redirects=True,
    http2=True,  # enable http2 to reduce block chance
    timeout=30,
)


class Rightmove:
    """
    The Rightmove class is used to search for properties
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
        self.properties_per_page = 499
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
        self.properties_details = None

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
        """Requests the search URL and returns the response."""
        response = requests.get(self.search_url)
        return response

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
            f"&channel={self.channel}"
            f"&sortType=2"
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

        url = f"{self.search_url_api}&index=0&numberOfPropertiesPerPage={self.properties_per_page}"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"No properties found for the search: {self.search_url_api}")
            return []
        total_results = int(
            json.loads(response.text)["resultCount"].replace(",", "")
        )
        properties = json.loads(response.text)["properties"]

        if total_results > self.properties_per_page:
            API_LIMIT = 1247
            for i in range(
                self.properties_per_page,
                total_results,
                self.properties_per_page,
            ):

                lower_limit = i
                upper_limit = self.properties_per_page
                if i > API_LIMIT:
                    break
                url = f"{self.search_url_api}&index={lower_limit}&numberOfPropertiesPerPage={upper_limit}"
                response = requests.get(url)
                properties += json.loads(response.text)["properties"]
        if total_results > len(properties):
            print(
                f"\nWarning: {total_results} total results but it was only possible to get {len(properties)} results."
            )
        return properties

    def get_urls_for_properties_in_search(self) -> List[str]:
        """
        Get the URLs for the properties in the search.

        :return: list: The URLs for the properties.
        """
        data = self.search_properties_api()
        urls = []
        for property_data in data:
            urls.append(
                f"https://www.rightmove.co.uk{property_data['propertyUrl']}"
            )
        urls = list(set(urls))
        return urls

    @staticmethod
    def parse_property(data):
        """Parse data to only necessary fields."""
        return data

    @staticmethod
    def find_json_objects(text: str, decoder=json.JSONDecoder()):
        """Find JSON objects in text, and generate decoded JSON data."""
        pos = 0
        while True:
            match = text.find("{", pos)
            if match == -1:
                break
            try:
                result, index = decoder.raw_decode(text[match:])
                yield result
                pos = match + index
            except ValueError:
                pos = match + 1

    @staticmethod
    def extract_property(response: Response) -> dict:
        """Extract property data from rightmove PAGE_MODEL javascript variable."""
        selector = Selector(response.text)
        data = selector.xpath(
            "//script[contains(.,'PAGE_MODEL = ')]/text()"
        ).get()
        if not data:
            print(f"page {response.url} is not a property listing page")
            return
        json_data = list(Rightmove.find_json_objects(data))[0]
        return json_data["propertyData"]

    async def scrape_properties(self, urls: List[str]) -> List[dict]:
        """Scrape Rightmove property listings for property data"""
        to_scrape = [client.get(url) for url in urls]
        properties = []
        for response in asyncio.as_completed(to_scrape):
            response = await response
            properties.append(
                Rightmove.parse_property(Rightmove.extract_property(response))
            )
        return properties

    def get_properties_details(self) -> List[dict]:
        """
        Get the property details for the properties in the search.

        :return: list: The property details.
        """
        urls = self.get_urls_for_properties_in_search()
        data = asyncio.run(self.scrape_properties(urls))
        return data


if __name__ == "__main__":
    rightmove = Rightmove(
        buy_or_rent="buy",
        location="kent",
        radius=0.5,
        min_price=100000,
        max_price=500000,
    )
    properties = rightmove.search_properties_api()
    print(len(properties))

import json
from urllib.parse import urlencode

import requests
import scrapy



class RightmoveSpider(scrapy.Spider):
    name = "rightmove"
    allowed_domains = ["www.rightmove.co.uk"]
    start_urls = ["https://www.rightmove.co.uk/"]

    # search attributes
    search_buy_or_rent: str = "buy"  # "buy" or "rent"
    search_location: str = "London"  # Location to search for properties
    search_radius: float = 0  # Radius of the search in miles
    search_property_type: list[str] | None = (
        ["bungalow", "detached", "flat"]  # A list of any from "bungalow", "detached", "flat", "land", "park-home", "semi-detached", "terraced".
    )
    search_min_price: int | None = None  # Minimum price of the property
    search_max_price: int | None = None  # Maximum price of the property
    search_min_bedrooms: int | None = None  # Minimum number of bedrooms
    search_max_bedrooms: int | None = (
        None  # Maximum number of bedrooms up to 5 or
    )
    search_max_days_since_added: int | None = (
        None  # Maximum number of days since added Only allows 1, 3, 7, 14
    )
    search_include_sstc: bool | None = (
        None  # Whether to include properties marked as SSTC (Sold Subject To Contract)
    )
    search_must_have: list[str] | None = (
        None  # A list of features that the property must have. Only allows any combination of the following: "garden", "parking", "newHome", "retirement", "sharedOwnership", "auction".
    )
    search_dont_show: list[str] | None = (
        None  # A list of features that the property must not have. Only allows any combination of the following: "newHome", "retirement", "sharedOwnership", "furnishTypes".
    )
    search_limit: int | None = None  # Limit of properties to return

    # API attributes
    API_BASE_URL: str = "https://www.rightmove.co.uk/api/_search?"
    API_PROPERTIES_PER_PAGE: int = (
        499  # Number of properties per page in the API response numberOfPropertiesPerPage
    )
    API_LIMIT: int = 1247  # Maximum lower index for the API request

    def parse(self, response):
        api_url = self.search_url() + f"&index=0&numberOfPropertiesPerPage={self.API_PROPERTIES_PER_PAGE}"
        response = json.loads(requests.get(api_url).text)
        total_results = int(response["resultCount"].replace(",", ""))

        properties = response["properties"]
        if total_results > self.API_PROPERTIES_PER_PAGE:
            for i in range(self.API_PROPERTIES_PER_PAGE, total_results, self.API_PROPERTIES_PER_PAGE):
                if i > self.API_LIMIT:
                    break
                lower_index = i
                offset = self.API_PROPERTIES_PER_PAGE
                api_url = self.search_url() + f"&index={lower_index}&numberOfPropertiesPerPage={offset}"
                properties += json.loads(requests.get(api_url).text)["properties"]
        
        self.log(f"Total results: {total_results}, Properties fetched: {len(properties)}")
        for property in properties:
            item = {}
            for key, value in property.items():
                item[key] = value
            yield item
                


    # ---- Functions that help with the search process ---
    def search_url(self) -> str:
        """
        Generate the search URL for the Rightmove API based on the search parameters.
        :return: The search URL for the Rightmove API"""

        search_params = {
            "locationIdentifier": self.search_location_id(),
            "channel": self.search_buy_or_rent.upper(),
            "sortType": 2,
            "radius": self.search_radius,
            "propertyTypes": self.search_property_type,
            "minPrice": self.search_min_price,
            "maxPrice": self.search_max_price,
            "minBedrooms": self.search_min_bedrooms,
            "maxBedrooms": self.search_max_bedrooms,
            "maxDaysSinceAdded": self.search_max_days_since_added,
            "includeSSTC": self.search_include_sstc,
            "mustHave": self.search_must_have,
            "dontShow": self.search_dont_show,
            "viewType": "LIST",
            "areaSizeUnit": "sqft",
            "currencyCode": "GBP",
            "isFetching": "false",
            "viewport": "",
        }
        # Remove None values from the search parameters
        search_params = {
            k: v for k, v in search_params.items() if v is not None
        }
        # Encode the search parameters
        # List are joined with %2C
        encoded_params = urlencode(search_params, doseq=True)
        # Construct the search URL
        return f"{self.API_BASE_URL}{encoded_params}"

    def search_location_id(self) -> str | None:
        """
        turn location string into a searchable string to use in the API
        e.g. "London" -> "london", ME1 1AA -> "me1+1aa
        and returns the location id in the format of "type^id"

        :param location: The location to search for
        :return: The location id
        """
        location = self.search_location
        if location != "":
            location = self.tokenize_search(location)
            url = f"https://los.rightmove.co.uk/typeahead?query={location}"
            response = requests.get(url)
            data = json.loads(response.text)["matches"]  # Parse the response
            if len(data) == 0:  # Check if there are any matches
                raise ValueError("No matches found for location")
            match = data[0]  # Get the first match
            location_id = f"{match['type']}^{match['id']}"
            return location_id
        else:
            raise ValueError("Location was not provided")

    def tokenize_search(self, location):
        special_chars = [" ", ",", ".", "-", "(", ")", "&", "-", "_"]
        for char in special_chars:
            location = location.replace(char, "+")
        location = location.lower()
        return location

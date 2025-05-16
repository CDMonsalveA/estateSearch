import json
import logging
import re
from urllib.parse import urlencode

import requests
import scrapy

from ..items import (
    PropertyFeatureItem,
    PropertyImageItem,
    PropertyItem,
    PropertyLivingCostItem,
    PropertyLocationItem,
    PropertyNearestAirportItem,
    PropertyNearestStationItem,
    PropertyRoomItem,
)


class RightmoveSpider(scrapy.Spider):
    name = "rightmove"
    allowed_domains = ["www.rightmove.co.uk"]
    start_urls = ["https://www.rightmove.co.uk/"]
    # Set the user agent to a random one
    # custom_settings = {
    #     "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    # }

    # search attributes
    search_buy_or_rent: str = "buy"  # "buy" or "rent"
    search_location: str = "London"  # Location to search for properties
    search_radius: float = 0  # Radius of the search in miles
    search_property_type: list[str] | None = (
        []
    )  # A list of any from "bungalow", "detached", "flat", "land", "park-home", "semi-detached", "terraced".
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

    def start_requests(self):
        """Start the search, and get all the search that the API can provide"""
        # Perform a first search to get the total number of results
        api_url = (
            self.search_url()
            + f"&index=0&numberOfPropertiesPerPage={self.API_PROPERTIES_PER_PAGE}"
        )
        response = scrapy.Request(url=api_url)
        # Parse the response to get the total number of results
        response = json.loads(requests.get(api_url).text)
        total_results = int(response["resultCount"].replace(",", ""))
        self.log(f"Total results: {total_results}", level=logging.INFO)

        urls = []

        for i in range(0, total_results, self.API_PROPERTIES_PER_PAGE):
            if i > self.API_LIMIT:
                break
            lower_index = i
            offset = self.API_PROPERTIES_PER_PAGE
            api_url = (
                self.search_url()
                + f"&index={lower_index}&numberOfPropertiesPerPage={offset}"
            )
            urls.append(api_url)
            self.log(f"API URL: {api_url}")
            yield scrapy.Request(url=api_url, callback=self.parse)

    async def parse(self, response):
        """Parse the response and extract the properties"""
        properties_api_data = json.loads(response.text)["properties"]
        self.log(f"Properties API data length: {len(properties_api_data)}")

        for property_data in properties_api_data:
            property_item = PropertyItem()
            image_item = PropertyImageItem()
            location_item = PropertyLocationItem()
            room_item = PropertyRoomItem()
            nearest_station_item = PropertyNearestStationItem()
            nearest_airport_item = PropertyNearestAirportItem()
            living_cost_item = PropertyLivingCostItem()
            feature_item = PropertyFeatureItem()
            self.assignBasicInfo(
                property_data,
                property_item,
                image_item,
                location_item,
                room_item,
                nearest_station_item,
                nearest_airport_item,
                living_cost_item,
                feature_item,
            )

            yield scrapy.Request(
                url=property_item["url"],
                callback=self.parse_property,
                errback=self.parse_property_error,
                meta={
                    "property_item": property_item,
                    "image_item": image_item,
                    "location_item": location_item,
                    "room_item": room_item,
                    "nearest_station_item": nearest_station_item,
                    "nearest_airport_item": nearest_airport_item,
                    "living_cost_item": living_cost_item,
                    "feature_item": feature_item,
                },
            )

    async def parse_property(self, response):
        property_item = response.meta["property_item"]
        image_item = response.meta["image_item"]
        location_item = response.meta["location_item"]
        room_item = response.meta["room_item"]
        nearest_station_item = response.meta["nearest_station_item"]
        nearest_airport_item = response.meta["nearest_airport_item"]
        living_cost_item = response.meta["living_cost_item"]
        feature_item = response.meta["feature_item"]

        data = response.xpath(
            "//script[contains(.,'PAGE_MODEL = ')]/text()"
        ).get()
        # Extract the JSON data from the script tag
        data = json.JSONDecoder().raw_decode(data[data.index("{") :])[0]
        # Assign the data to the propertyData
        self.assignAdvancedInfo(
            data,
            property_item,
            image_item,
            location_item,
            room_item,
            nearest_station_item,
            nearest_airport_item,
            living_cost_item,
            feature_item,
        )

        yield property_item
        yield image_item

    async def parse_property_error(self, failure):
        # Handle the error here
        self.logger.warning(
            f"Failed to parse property: {failure.request.url} - {failure.value}"
        )
        yield failure.request.meta["property_item"]
        yield failure.request.meta["image_item"]

    # ------ Functions to create the search URL ------
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

    # ------ Functions to improve readability ------
    def assignBasicInfo(
        self,
        property_data,
        property_item,
        image_item,
        location_item,
        room_item,
        nearest_station_item,
        nearest_airport_item,
        living_cost_item,
        feature_item,
    ):

        property_item["source"] = self.name
        property_item["url"] = (
            "https://www.rightmove.co.uk" + property_data["propertyUrl"]
        )
        property_item["id"] = property_data["id"]
        property_item["transactionType"] = property_data["transactionType"]
        property_item["bedrooms"] = property_data["bedrooms"]
        property_item["bathrooms"] = property_data["bathrooms"]
        property_item["numberOfImages"] = property_data["numberOfImages"]
        property_item["numberOfFloorplans"] = property_data[
            "numberOfFloorplans"
        ]
        property_item["displayAddress"] = property_data["displayAddress"]
        property_item["propertyType"] = property_data["propertySubType"]
        property_item["summary"] = property_data["summary"]
        property_item["listingUpdateReason"] = property_data["listingUpdate"][
            "listingUpdateReason"
        ]
        property_item["price"] = property_data["price"]["amount"]
        property_item["price_frequency"] = property_data["price"]["frequency"]
        property_item["price_currencyCode"] = property_data["price"][
            "currencyCode"
        ]

        property_item["contactTelephone"] = property_data["customer"][
            "contactTelephone"
        ]
        property_item["contact_branchDisplayName"] = property_data[
            "customer"
        ].get("contactBranchDisplayName")
        property_item["commercial"] = property_data["commercial"]
        property_item["development"] = property_data["development"]
        property_item["residential"] = property_data["residential"]
        property_item["students"] = property_data["students"]
        property_item["auction"] = property_data["auction"]
        property_item["feesApply"] = property_data["feesApply"]
        property_item["displaySize"] = property_data["displaySize"]
        property_item["firstVisibleDate"] = property_data["firstVisibleDate"]
        property_item["propertyTypeFullDescription"] = property_data[
            "propertyTypeFullDescription"
        ]
        property_item["isRecent"] = property_data["isRecent"]

        #### Assign the data to the imageItem ####

        images = property_data["propertyImages"].get("images")
        if images:
            for image in images:
                image_item["id"] = property_data["id"]
                image_item["imageUrl"] = (
                    "https://media.rightmove.co.uk/dir/" + image["url"]
                )
                image_item["caption"] = image["caption"]
                image_item["type"] = "search"

    def assignAdvancedInfo(
        self,
        data,
        property_item,
        image_item,
        location_item,
        room_item,
        nearest_station_item,
        nearest_airport_item,
        living_cost_item,
        feature_item,
    ):

        property_item["status"] = data["propertyData"].get("status")
        property_item["price_displayPriceQualifier"] = data["propertyData"][
            "prices"
        ].get("displayPriceQualifier")
        property_item["brochure_url"] = (
            data["propertyData"].get("brochures")[0].get("url")
            if data["propertyData"].get("brochures")
            else None
        )
        property_item["epcGraph"] = (
            data["propertyData"]["epcGraphs"][0].get("url")
            if data["propertyData"].get("epcGraphs")
            else None
        )
        property_item["feesApply"] = data["propertyData"].get("feesApply")
        property_item["lettings"] = data["propertyData"].get("lettings")
        property_item["tenure_type"] = data["propertyData"]["tenure"].get(
            "tenureType"
        )
        property_item["tenure_years"] = data["propertyData"]["tenure"].get(
            "yearsRemainingOnLease"
        )
        property_item["propertySubType"] = data["propertyData"].get(
            "propertySubType"
        )

        # Assign the data to the analyticsInfo
        property_item["displayAddress"] = data["analyticsInfo"][
            "analyticsBranch"
        ].get("displayAddress")
        property_item["postcode"] = data["analyticsInfo"][
            "analyticsProperty"
        ].get("postcode")
        property_item["added"] = data["analyticsInfo"]["analyticsProperty"].get(
            "added"
        )
        property_item["auctionOnly"] = data["analyticsInfo"][
            "analyticsProperty"
        ].get("auctionOnly")
        property_item["businessForSale"] = data["analyticsInfo"][
            "analyticsProperty"
        ].get("businessForSale")
        property_item["letAgreed"] = data["analyticsInfo"][
            "analyticsProperty"
        ].get("letAgreed")
        property_item["lettingType"] = data["analyticsInfo"][
            "analyticsProperty"
        ].get("lettingType")
        property_item["ownership"] = data["analyticsInfo"][
            "analyticsProperty"
        ].get("ownership")
        property_item["preOwned"] = data["analyticsInfo"][
            "analyticsProperty"
        ].get("preOwned")
        property_item["price_pageModel"] = data["analyticsInfo"][
            "analyticsProperty"
        ].get("price")
        property_item["priceQualifier"] = data["analyticsInfo"][
            "analyticsProperty"
        ].get("priceQualifier")
        property_item["propertyType"] = data["analyticsInfo"][
            "analyticsProperty"
        ].get("propertyType")
        property_item["propertySubType"] = data["analyticsInfo"][
            "analyticsProperty"
        ].get("propertySubType")
        property_item["retirement"] = data["analyticsInfo"][
            "analyticsProperty"
        ].get("retirement")
        property_item["soldSTC"] = data["analyticsInfo"][
            "analyticsProperty"
        ].get("soldSTC")

        #### Assign the date to the imageItem ####
        images = data["propertyData"].get("images")
        if images:
            for image in images:
                image_item["id"] = data["propertyData"]["id"]
                image_item["imageUrl"] = image.get("url")
                image_item["caption"] = image.get("caption")
                image_item["type"] = "image"
        floorplans = data["propertyData"].get("floorplans")
        if floorplans:
            for floorplan in floorplans:
                image_item["id"] = data["propertyData"]["id"]
                image_item["imageUrl"] = floorplan.get("url")
                image_item["caption"] = floorplan.get("caption")
                image_item["type"] = "floorplan"
        virtualTours = data["propertyData"].get("virtualTours")
        if virtualTours:
            for virtualTour in virtualTours:
                image_item["id"] = data["propertyData"]["id"]
                image_item["imageUrl"] = virtualTour.get("url")
                image_item["caption"] = virtualTour.get("caption")
                image_item["type"] = "virtualTour"

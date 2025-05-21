import json
import logging
import re
from urllib.parse import urlencode

import requests
import scrapy

from ..items import (
    PropertyImageItem,
    PropertyInterestPointItem,
    PropertyItem,
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
    search_max_bedrooms: int | None = None  # Maximum number of bedrooms up to 5 or
    search_max_days_since_added: int | None = None  # Maximum number of days since added Only allows 1, 3, 7, 14
    search_include_sstc: bool | None = None  # Whether to include properties marked as SSTC (Sold Subject To Contract)
    search_must_have: list[str] | None = (
        None  # A list of features that the property must have. Only allows any combination of the following: "garden", "parking", "newHome", "retirement", "sharedOwnership", "auction".
    )
    search_dont_show: list[str] | None = (
        None  # A list of features that the property must not have. Only allows any combination of the following: "newHome", "retirement", "sharedOwnership", "furnishTypes".
    )
    search_limit: int | None = None  # Limit of properties to return

    # API attributes
    API_BASE_URL: str = "https://www.rightmove.co.uk/api/_search?"
    API_PROPERTIES_PER_PAGE: int = 499  # Number of properties per page in the API response numberOfPropertiesPerPage
    API_LIMIT: int = 1247  # Maximum lower index for the API request

    def start_requests(self):
        """Start the search, and get all the search that the API can provide"""
        # Perform a first search to get the total number of results
        api_url = self.search_url() + f"&index=0&numberOfPropertiesPerPage={self.API_PROPERTIES_PER_PAGE}"
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
            api_url = self.search_url() + f"&index={lower_index}&numberOfPropertiesPerPage={offset}"
            urls.append(api_url)
            self.log(f"API URL: {api_url}")
            yield scrapy.Request(url=api_url, callback=self.parse)

    async def parse(self, response):
        """Parse the response and extract the properties"""
        properties_api_data = json.loads(response.text)["properties"]
        self.log(f"Properties API data length: {len(properties_api_data)}")

        for property_data in properties_api_data:
            property_item = PropertyItem()

            self.assignBasicPropertyInfo(property_data, property_item)

            images = property_data.get("propertyImages").get("images")
            if images:
                for image in images:
                    image_item = PropertyImageItem()
                    image_item["id"] = property_item["id"]
                    image_item["url"] = "https://media.rightmove.co.uk/dir/" + image.get("url")
                    image_item["caption"] = image.get("caption")
                    image_item["type"] = "search_image"
                    yield image_item

            yield scrapy.Request(
                url=property_item["url"],
                callback=self.parse_property,
                errback=self.parse_property_error,
                meta={"property_item": property_item},
            )

    async def parse_property(self, response):
        property_item = response.meta["property_item"]

        data = response.xpath("//script[contains(.,'PAGE_MODEL = ')]/text()").get()
        # Extract the JSON data from the script tag
        data = json.JSONDecoder().raw_decode(data[data.index("{") :])[0]

        # Assign the data to the propertyData
        self.assignAdvancedPropertyInfo(
            data,
            property_item,
        )
        yield property_item

        # yield images
        images = data.get("propertyData").get("images")
        if images:
            for image in images:
                image_item = PropertyImageItem()
                image_item["id"] = property_item["id"]
                image_item["url"] = image.get("url")
                image_item["caption"] = image.get("caption")
                image_item["type"] = "property_image"
                yield image_item
        del images
        floorplans = data.get("propertyData").get("floorPlans")
        if floorplans:
            for floorplan in floorplans:
                image_item = PropertyImageItem()
                image_item["id"] = property_item["id"]
                image_item["url"] = floorplan.get("url")
                image_item["caption"] = floorplan.get("caption")
                image_item["type"] = "floorplan_image"
                yield image_item
        del floorplans

        # yield rooms
        rooms = data.get("propertyData").get("rooms")
        if rooms:
            for room in rooms:
                room_item = PropertyRoomItem()
                room_item["id"] = property_item["id"]
                room_item["name"] = room.get("name")
                room_item["description"] = room.get("description")
                room_item["width"] = room.get("width")
                room_item["length"] = room.get("length")
                room_item["unit"] = room.get("unit")
                room_item["dimension"] = room.get("dimension")
                yield room_item
        del rooms

        # yield interest points
        nearest_airports = data.get("propertyData").get("nearestAirports")
        if nearest_airports:
            for airport in nearest_airports:
                interest_point_item = PropertyInterestPointItem()
                interest_point_item["id"] = property_item["id"]
                interest_point_item["type"] = "nearestAirports"
                interest_point_item["name"] = airport.get("name")
                interest_point_item["distance"] = airport.get("distance")
                interest_point_item["unit"] = airport.get("unit")
                yield interest_point_item
        del nearest_airports
        nearest_stations = data.get("propertyData").get("nearestStations")
        if nearest_stations:
            for station in nearest_stations:
                interest_point_item = PropertyInterestPointItem()
                interest_point_item["id"] = property_item["id"]
                interest_point_item["type"] = "nearestStations"
                interest_point_item["name"] = station.get("name")
                interest_point_item["distance"] = station.get("distance")
                interest_point_item["unit"] = station.get("unit")
                yield interest_point_item
        del nearest_stations

    async def parse_property_error(self, failure):
        # Handle the error here
        self.logger.warning(f"Failed to parse property: {failure.request.url} - {failure.value}")
        yield failure.request.meta["property_item"]

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
        search_params = {k: v for k, v in search_params.items() if v is not None}
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
    def assignBasicPropertyInfo(self, data, property_item):
        # Assign the data to the propertyItem using the structure from items.PropertyItem
        property_item["source"] = self.name
        property_item["url"] = "https://www.rightmove.co.uk" + data.get("propertyUrl")
        property_item["id"] = data.get("id")
        property_item["transactionType"] = data.get("transactionType")
        property_item["bedrooms"] = data.get("bedrooms")
        property_item["bathrooms"] = data.get("bathrooms")
        property_item["numberOfImages"] = data.get("numberOfImages")
        property_item["numberOfFloorplans"] = data.get("numberOfFloorplans")
        property_item["displayAddress"] = data.get("displayAddress").strip()
        property_item["propertyType"] = data.get("propertySubType")
        property_item["summary"] = data.get("summary")
        property_item["listingUpdateReason"] = data.get("listingUpdate").get("listingUpdateReason")
        property_item["listingUpdateDate"] = data.get("listingUpdate").get("listingUpdateDate")
        property_item["price"] = data.get("price").get("amount")
        property_item["price_frequency"] = data.get("price").get("frequency")
        property_item["price_currencyCode"] = data.get("price").get("currencyCode")
        property_item["contactTelephone"] = data.get("customer").get("contactTelephone")
        property_item["contact_branchDisplayName"] = data.get("customer").get("contactBranchDisplayName")
        property_item["commercial"] = data.get("commercial")
        property_item["development"] = data.get("development")
        property_item["residential"] = data.get("residential")
        property_item["students"] = data.get("students")
        property_item["auction"] = data.get("auction")
        property_item["feesApply"] = data.get("feesApply")
        property_item["displaySize"] = data.get("displaySize")
        property_item["firstVisibleDate"] = data.get("firstVisibleDate")
        property_item["propertyTypeFullDescription"] = data.get("propertyTypeFullDescription")
        property_item["isRecent"] = data.get("isRecent")
        property_item["latitude"] = data.get("location").get("latitude")
        property_item["longitude"] = data.get("location").get("longitude")

    def assignAdvancedPropertyInfo(self, data, property_item):
        # Assign the data from the propertyData
        propertyData = data.get("propertyData")
        property_item["status"] = propertyData.get("status")
        property_item["price_displayPriceQualifier"] = propertyData.get("prices").get("displayPriceQualifier")
        property_item["brochure_url"] = (
            propertyData.get("brochures")[0].get("url") if propertyData.get("brochures") else None
        )
        property_item["epcGraph"] = (
            propertyData.get("epcGraphs")[0].get("url") if propertyData.get("epcGraphs") else None
        )
        property_item["feesApply"] = propertyData.get("feesApply")
        property_item["lettings"] = propertyData.get("lettings")
        property_item["tenure_type"] = propertyData.get("tenure").get("tenureType")
        property_item["tenure_years"] = propertyData.get("tenure").get("yearsRemainingOnLease")
        property_item["propertySubType"] = propertyData.get("propertySubType")
        property_item["pinType"] = propertyData.get("location").get("pinType")
        property_item["displayAddress"] = propertyData.get("address").get("displayAddress")
        property_item["countryCode"] = propertyData.get("address").get("countryCode")
        property_item["ukCountry"] = propertyData.get("address").get("ukCountry")
        property_item["outcode"] = propertyData.get("address").get("outcode")
        property_item["incode"] = propertyData.get("address").get("incode")

        # Assign the data related to livingCosts
        livingCosts = propertyData.get("livingCosts")

        property_item["councilTaxExempt"] = livingCosts.get("councilTaxExempt")
        property_item["councilTaxIncluded"] = livingCosts.get("councilTaxIncluded")
        property_item["annualGroundRent"] = livingCosts.get("annualGroundRent")
        property_item["groundRentReviewPeriodInYears"] = livingCosts.get("groundRentReviewPeriodInYears")
        property_item["groundRentPercentageIncrease"] = livingCosts.get("groundRentPercentageIncrease")
        property_item["annualServiceCharge"] = livingCosts.get("annualServiceCharge")
        property_item["councilTaxBand"] = livingCosts.get("councilTaxBand")
        property_item["domesticRates"] = livingCosts.get("domesticRates")
        del livingCosts

        # Assign the data related to features
        features = propertyData.get("features")
        property_item["electricity"] = features.get("electricity")
        property_item["broadband"] = features.get("broadband")
        property_item["water"] = features.get("water")
        property_item["sewarage"] = features.get("sewage")
        property_item["heating"] = features.get("heating")
        property_item["accessibility"] = features.get("accessibility")
        property_item["parking"] = features.get("parking")
        property_item["garden"] = features.get("garden")
        property_item["risks"] = features.get("risks")
        property_item["obligations"] = features.get("obligations")
        del features

        del propertyData

        property_item["isAuthenticated"] = data.get("isAuthenticated")

        # Assign the data from the analyticsInfo
        analyticsproperty = data.get("analyticsInfo").get("analyticsProperty")
        property_item["postcode"] = analyticsproperty.get("postcode")
        property_item["added"] = analyticsproperty.get("added")
        property_item["auctionOnly"] = analyticsproperty.get("auctionOnly")
        property_item["businessForSale"] = analyticsproperty.get("businessForSale")
        property_item["letAgreed"] = analyticsproperty.get("letAgreed")
        property_item["lettingType"] = analyticsproperty.get("lettingType")
        property_item["ownership"] = analyticsproperty.get("ownership")
        property_item["preOwned"] = analyticsproperty.get("preOwned")
        property_item["price_pageModel"] = analyticsproperty.get("price")
        property_item["priceQualifier"] = analyticsproperty.get("priceQualifier")
        property_item["propertyType"] = analyticsproperty.get("propertyType")
        property_item["propertySubType"] = analyticsproperty.get("propertySubType")
        property_item["retirement"] = analyticsproperty.get("retirement")
        property_item["soldSTC"] = analyticsproperty.get("soldSTC")
        del analyticsproperty

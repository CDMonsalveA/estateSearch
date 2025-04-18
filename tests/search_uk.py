import json
import unittest
from random import sample

import requests

from estatesearch import Rightmove
from estatesearch.search.searchConfig import SearchParams
from data.rightmove_samples import location_ids_examples

# Number of test samples
n_samples = 1
# test samples
samples = [
    # POSTCODE
    ("SY3 9EB", "POSTCODE", "4203018"),
    ("sy3-9eb", "POSTCODE", "4203018"),
    ("W1A 1AA", "POSTCODE", "912358"),
    ("w1a-1aa", "POSTCODE", "912358"),
    ("B1 1AA", "POSTCODE", "4183557"),
    ("CR0 5NS", "POSTCODE", "184365"),
    ("CR0-5NS", "POSTCODE", "184365"),
    # AREA
    ("london", "REGION", "87490"),  # 93917 for greater london
    ("birmingham", "REGION", "162"),
    ("manchester", "REGION", "904"),
    ("liverpool", "REGION", "813"),
    ("leeds", "REGION", "787"),
    ("bristol", "REGION", "219"),
    ("edinburgh", "REGION", "475"),
    ("glasgow", "REGION", "550"),
    ("cardiff", "REGION", "281"),
    ("swansea", "REGION", "1305"),
    # TRAIN STATION
    ("paddington", "REGION", "70403"),
]

rightmove_api_keys = [
    "id",
    "bedrooms",
    "bathrooms",
    "numberOfImages",
    "numberOfFloorplans",
    "numberOfVirtualTours",
    "summary",
    "displayAddress",
    "countryCode",
    "location",
    "propertyImages",
    "propertySubType",
    "listingUpdate",
    "premiumListing",
    "featuredProperty",
    "price",
    "customer",
    "distance",
    "transactionType",
    "productLabel",
    "commercial",
    "development",
    "residential",
    "students",
    "auction",
    "feesApply",
    "feesApplyText",
    "displaySize",
    "showOnMap",
    "propertyUrl",
    "contactUrl",
    "staticMapUrl",
    "channel",
    "firstVisibleDate",
    "keywords",
    "keywordMatchType",
    "saved",
    "hidden",
    "onlineViewingsAvailable",
    "lozengeModel",
    "hasBrandPlus",
    "displayStatus",
    "enquiredTimestamp",
    "enquiryAddedTimestamp",
    "enquiryCalledTimestamp",
    "heading",
    "addedOrReduced",
    "formattedBranchName",
    "formattedDistance",
    "propertyTypeFullDescription",
    "isRecent",
    "enhancedListing",
]
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


search_samples = [
    SearchParams(
        location="london",
        buy_rent="buy",
        radius=1,
        property_type=["flat"],
        min_price=0,
        max_price=1000000,
        min_bedrooms=1,
        max_bedrooms=5,
        max_days_since_added=7,
        include_sstc=False,
        must_have=[],
        dont_show=[],
        verbose=0,
    ),
]


class TestRightmove(unittest.TestCase):
    """
    Test the Rightmove class
    """

    def test_init(self):
        pass

    def test_init_UserWarning_no_location(self):
        pass

    def test_init_UserWarning_no_buy_or_rent(self):
        pass

    def test_get_location_id_with_special_characters(self):
        pass

    def test_get_location_id_for_empty_location(self):
        pass

    def test_search_url_for_unknown_parameters(self):
        pass

    def test_search_url_api_for_unknown_parameters(self):
        pass

    def test_search_bar_presence(self):
        """
        Evaluate if the search bar is present on the website.
        """
        rightmove = Rightmove()
        website_content = requests.get(rightmove.url).text
        self.assertIn("ta_searchInput", website_content)

    def test_for_sale_button_presence(self):
        """
        Evaluate if the 'for sale' button is present on the website.
        """
        rightmove = Rightmove()
        website_content = requests.get(rightmove.url).text
        self.assertIn("dsrm_button_content", website_content)

    def test_house_prices_connection(self):
        """
        Test the connection to the Rightmove house prices website.
        """
        places = list(set([place[0] for place in samples]))
        places = sample(places, n_samples)
        for place in places:
            rightmove = Rightmove(SearchParams(location=place))
            status_code = requests.get(rightmove.house_prices_url).status_code
            self.assertEqual(status_code, 200)

    def test_get_location_id(self):
        """
        Test the get_location_id method.
        """
        locations = sample(samples, n_samples)
        for location, location_type, location_id in locations:
            rightmove = Rightmove(SearchParams(location=location))
            self.assertEqual(
                rightmove.get_location_id(), (location_type, location_id)
            )

    def test_search_url_connection(self):
        """
        Test the connection to the Rightmove regular search.
        """
        places = list(set([place[0] for place in samples]))
        places = sample(places, n_samples)
        for place in places:
            rightmove = Rightmove(SearchParams(location=place))
            status_code = requests.get(rightmove.search_url).status_code
            self.assertEqual(status_code, 200)

    def test_search_url_api_connection(self):
        """
        Test the connection to the Rightmove API search.
        """
        places = list(set([place[0] for place in samples]))
        places = sample(places, n_samples)
        for place in places:
            rightmove = Rightmove(SearchParams(location=place))
            # print(rightmove.search_url_api)
            status_code = requests.get(rightmove.search_url_api).status_code
            self.assertEqual(status_code, 200)

    def test_search_properties_api(self):
        """
        Test the search_properties_api method.
        """
        places = list(set([place[0] for place in samples]))
        places = sample(places, n_samples)
        for place in places:
            rightmove = Rightmove(SearchParams(location=place, radius=1))
            properties = rightmove.search_properties_api()
            print(len(properties))
            self.assertTrue(len(properties) > 0)

    def test_search_url_api_properties_attributes(self):
        """
        check the attributes 'keys' of the properties returned
        by fetching the API
        """
        places = list(set([place[0] for place in samples]))
        places = sample(places, n_samples)
        for place in places:
            rightmove = Rightmove(SearchParams(location=place, radius=1))
            response = requests.get(rightmove.search_url_api)
            properties = json.loads(response.text)["properties"]
            # assert all the keys are present even if the order is different
            self.assertEqual(
                sorted(list(properties[0].keys())), sorted(rightmove_api_keys)
            )

    def test_search_properties_api_with_full_search(self):
        """
        Test the search_properties_api method with a full search.
        """
        searches = sample(search_samples, n_samples)
        for search in searches:
            rightmove = Rightmove(search)
            properties = rightmove.search_properties_api()
            self.assertTrue(len(properties) > 0)

    def test_httpx_agent_connection(self):
        pass

    def test_find_json_objects(self):
        pass

    def test_extract_property(self):
        pass

    def test_scrape_properties(self):
        pass

    def test_get_properties_details(self):
        pass

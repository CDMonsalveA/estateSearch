import unittest
from random import shuffle

import requests

from estatesearch import Rightmove

unittest.TestLoader.sortTestMethodsUsing = None

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
    ("london", "REGION", "93917"),
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


class TestRightmove(unittest.TestCase):
    """
    Test the Rightmove class
    """

    # test for warnings with no location
    # test for warnings with no buy_or_rent
    # test for warnings with no location and no buy_or_rent
    def test_connection(self):
        """
        Test the connection to the Rightmove website.
        """
        rightmove = Rightmove(location="london")
        status_code = requests.get(rightmove.url).status_code
        self.assertEqual(status_code, 200)

    def test_api_connection(self):
        """
        Test the connection to the Rightmove API.
        """
        rightmove = Rightmove(location="london")
        status_code = requests.get(rightmove.api_url).status_code
        self.assertEqual(status_code, 200)

    def test_search_bar_presence(self):
        """
        Evaluate if the search bar is present on the website.
        """
        rightmove = Rightmove(location="london")
        website_content = requests.get(rightmove.url).text
        self.assertIn("ta_searchInput", website_content)

    def test_for_sale_button_presence(self):
        """
        Evaluate if the 'for sale' button is present on the website.
        """
        rightmove = Rightmove(location="london")
        website_content = requests.get(rightmove.url).text
        self.assertIn("dsrm_button_content", website_content)

    def test_house_prices_connection(self):
        """
        Test the connection to the Rightmove house prices website.
        """
        places = list(set([place[0] for place in samples]))
        shuffle(places)

        for place in places:
            rightmove = Rightmove(location=place)
            status_code = requests.get(rightmove.house_prices_url).status_code
            self.assertEqual(status_code, 200)

    def test_get_location_id(self):
        """
        Test the get_location_id method.
        """
        locations = samples
        shuffle(locations)
        for location, location_type, location_id in locations:
            rightmove = Rightmove(location=location)
            self.assertEqual(rightmove.get_location_id(), (location_type, location_id))

import unittest

import requests
from random import shuffle

import asyncio

from estatesearch import Rightmove


class TestRightmove(unittest.TestCase):
    """
    Test the Rightmove class
    """

    def test_connection(self):
        """
        Test the connection to the Rightmove website.
        """
        rightmove = Rightmove()
        status_code = requests.get(rightmove.url).status_code
        self.assertEqual(status_code, 200)
        

    def test_api_connection(self):
        """
        Test the connection to the Rightmove API.
        """
        rightmove = Rightmove()
        status_code = requests.get(rightmove.api_url).status_code
        self.assertEqual(status_code, 200)

    def test_house_prices_connection(self):
        """
        Test the connection to the Rightmove house prices website.
        """
        places = ["london", "me2", "paddington", "w1", "sy3-9eb",
                  "birmingham", "manchester", "liverpool", "leeds",
                  "bristol", "edinburgh", "glasgow", "cardiff", "swansea",
                #  Postcodes
                  "ME2-4JZ", "W1A-1AA", "SY3-9EB", "B1-1AA", "M1-1AA",]
        # shuffle(places)
        shuffle(places)
        
        for place in places:
            rightmove = Rightmove(location=place)
            status_code = requests.get(rightmove.house_prices_url).status_code
            self.assertEqual(status_code, 200)

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

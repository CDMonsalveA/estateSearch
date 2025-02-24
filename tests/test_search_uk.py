import unittest

import requests

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

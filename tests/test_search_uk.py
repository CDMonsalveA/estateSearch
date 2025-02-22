import unittest

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
        status_code = rightmove.check_basic_request_connection()
        self.assertEqual(status_code, 200)

    def test_search_bar_presence(self):
        """
        Evaluate if the search bar is present on the website.
        """
        rightmove = Rightmove()
        website_content = rightmove.check_website_content()
        self.assertIn("ta_searchInput", website_content)

    def test_for_sale_button_presence(self):
        """
        Evaluate if the 'for sale' button is present on the website.
        """
        rightmove = Rightmove()
        website_content = rightmove.check_website_content()
        self.assertIn("dsrm_button_content", website_content)

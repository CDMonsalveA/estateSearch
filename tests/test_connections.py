"""Test API connections, Web pages availability, and other connections."""

import logging
import unittest

import requests

from estatesearch.search.searchConfig import SearchParams
from estatesearch.search.uk.rightmove import Rightmove

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


# Testing
class UKSearchEngines(unittest.TestCase):
    """Test case for UK search engines connections."""

    SearchEngines = {
        "Rightmove": Rightmove(SearchParams()),
    }

    def test_search_engines(self):
        """Test the search engines connections."""
        # check for self.url connection
        logger.info("Testing search engines connections...")
        for engine in self.SearchEngines:
            logger.info(f"Testing {engine} connection...")
            # Create an instance of the search engine
            engine_instance = self.SearchEngines[engine]
            # Check if the URL is reachable
            response = requests.get(engine_instance.url)
            self.assertEqual(
                response.status_code, 200, f"{engine} is not reachable."
            )

    def test_rightmove_api_connection(self):
        """
        Test the connection to the Rightmove API.
        """
        rightmove = Rightmove()
        status_code = requests.get(
            "https://www.rightmove.co.uk/api/_search?locationIdentifier=POSTCODE%5E1149959&channel=BUY"
        ).status_code
        self.assertEqual(status_code, 200)

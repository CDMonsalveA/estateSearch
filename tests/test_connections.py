"""Test API connections, Web pages availability, and other connections."""

import json
import logging
import random
import time
import unittest
from typing import Any

import requests
from data.rightmove_samples import (
    location_ids_examples,
    rightmove_api_keys,
    searches,
)

from estatesearch.search.search import SearchManager
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

    def test_rightmove_get_location_id(self):
        """
        Test the get_location_id method.
        """
        for location in location_ids_examples:
            rightmove = Rightmove(
                SearchParams(location=location.searchText, radius=2)
            )
            self.assertEqual(
                rightmove.get_location_id(),
                (location.locationType, location.locationID),
                "Location ID mismatch.",
            )

    def test_rightmove_api_keys(self):
        """
        Test the API keys for Rightmove.
        """
        for search in searches:
            logger.debug(f"Testing location: {search.location}")
            rightmove = Rightmove(search)
            response = requests.get(rightmove.search_url_api)
            self.assertEqual(
                response.status_code, 200, "API keys not reachable."
            )
            properties = json.loads(response.text)["properties"]
            self.assertEqual(
                sorted(list(properties[0].keys())),
                sorted(rightmove_api_keys),
                "API keys mismatch.",
            )

    def test_SearchManager(self):
        """
        Test the SearchManager function.
        """
        search = SearchParams(location="London", limit=10)
        search_manager = SearchManager(search)
        search_results = search_manager.search()
        self.assertIsInstance(
            search_results, str, "SearchManager is not a string."
        )
        search_results = json.loads(search_results)
        self.assertIn(
            "SearchResults", search_results, "SearchResults not found."
        )
        self.assertIn("SearchParams", search_results, "SearchParams not found.")
        self.assertIn("SearchDate", search_results, "SearchDate not found.")
        self.assertIn("Version", search_results, "Version not found.")
        self.assertTrue(
            len(search_results["SearchResults"]) > 0, "SearchResults is empty."
        )

        # search = SearchParams(location="London", limit=10)
        # search_manager = SearchManager(search)
        # self.assertIsInstance(search_manager, str, "SearchManager is not a string.")
        # search_results = json.loads(search_manager)
        # self.assertIn("SearchResults", search_results, "SearchResults not found.")
        # self.assertIn("SearchParams", search_results, "SearchParams not found.")
        # self.assertIn("SearchDate", search_results, "SearchDate not found.")
        # self.assertIn("Version", search_results, "Version not found.")
        # self.assertTrue(
        #     len(search_results["SearchResults"]) > 0, "SearchResults is empty."
        # )

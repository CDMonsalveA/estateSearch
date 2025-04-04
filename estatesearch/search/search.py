"""Search manager for the estate search application."""

import datetime
import json
import logging
from typing import Any, Dict, List, Optional

from estatesearch.search.searchConfig import SearchParams
from estatesearch.search.uk.rightmove import Rightmove

# Set up logging
# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s",
# )
logger = logging.getLogger(__name__)


class SearchManager:
    """
    Search manager for the estate search application.

    This class manages the search process and stores the results.
    It is responsible for coordinating the various search engines and aggregating the results.
    """

    def __init__(
        self, params: SearchParams, engines: Optional[List[str]] = None
    ) -> None:
        """
        Initialize the SearchManager with search parameters.

        Args:
            params (SearchParams): The search parameters for the search.
            engines (List[str]): List of search engines to use. 'Rightmove' is the only one implemented so far.
        """
        self.params: SearchParams = params
        search_engines: Dict[str, Any] = {
            "Rightmove": Rightmove(params),
            # Add other search engines here
        }
        if not engines:
            engines = list(search_engines.keys())
        self.search_engines: Dict[str, Any] = {
            engine: search_engines[engine]
            for engine in engines
            if engine in search_engines
        }

    def search(self) -> str:
        """
        Perform the search using the configured search engines.

        Returns:
            str: The search results as a JSON object.
        """
        results: Dict[str, Any] = {}
        # Loop through each search engine and get the properties details
        for engine in self.search_engines:
            logger.info(f"Searching for properties on {engine}...")
            # Create an instance of the search engine
            engine_instance = self.search_engines[engine]
            # Perform the search
            search_results = engine_instance.get_properties_details()
            # Check if the search was successful
            if not search_results:
                logger.warning(f"No properties found on {engine}.")
                continue
            else:
                logger.info(
                    f"Found {len(search_results)} properties on {engine}."
                )
            # Store the search results with the engine name and the date of search
            results[engine] = {
                "properties": search_results,
            }
        # Add additional information to the search [e.g. country, dateOfSearch, etc.]
        search_results = {
            "Version": "1.0",
            "SearchResults": results,
            "SearchParams": self.params._asdict(),
            "SearchDate": datetime.datetime.now().isoformat(),
        }
        # Return the search results as a JSON object
        return json.dumps(search_results, indent=4)

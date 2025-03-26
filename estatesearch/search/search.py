"""Search manager for the estate search application."""

import datetime
import json
import logging
from typing import Dict, List

from estatesearch.search.searchConfig import SearchParams
from estatesearch.search.uk.rightmove import Rightmove

# Set up logging
# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s",
# )
logger = logging.getLogger(__name__)


def SearchManager(
    params: SearchParams,
) -> str:
    """
    Search manager for the estate search application.

    This function manages the search process
    """
    # Make a new search
    SearchEngines = {
        "Rightmove": Rightmove(params),
    }
    results = {}
    # Loop through each search engine and get the properties details
    for engine in SearchEngines:
        logger.info(f"Searching for properties on {engine}...")
        # Create an instance of the search engine
        engine_instance = SearchEngines[engine]
        # Perform the search
        search_results = engine_instance.get_properties_details()
        # Check if the search was successful
        if not search_results:
            logger.warning(f"No properties found on {engine}.")
            continue
        else:
            logger.info(f"Found {len(search_results)} properties on {engine}.")
        # Store the search results with the engine name and the date of search
        results[engine] = {
            "properties": search_results,
        }
    # Add addional information to the search [e.g. country, dateOfSearch, etc.]
    search_results = {
        "Version": "1.0",
        "SearchResults": results,
        "SearchParams": params._asdict(),
        "SearchDate": datetime.datetime.now().isoformat(),
    }
    # Return the search results as a JSON object
    return json.dumps(search_results, indent=4)

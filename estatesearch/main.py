"""
Main Module for the Estate Search application.
This module controls the flow of the application, including loading configuration,
searching for properties, and saving results.
It serves as the entry point for the application and coordinates the various components.
"""

import datetime
import json
import logging
import pathlib

from estatesearch.search.search import SearchManager
from estatesearch.search.searchConfig import SearchParams

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename=pathlib.Path("logs") / f"app_{datetime.datetime.now().date()}.log",
    filemode="a",
    datefmt="%Y-%m-%d %H:%M:%S",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    # handlers=[
    #     logging.FileHandler(
    #         pathlib.Path("logs") / f"app_{datetime.datetime.now().date()}.log"
    #     ),
    #     logging.StreamHandler(),
    # ],
)

logger = logging.getLogger(__name__)


def main():
    """
    Main function to execute the Estate Search application.
    This function will orchestrate the various components of the application,
    including loading configuration, searching for properties, and saving results.
    """
    # Search / Fetch the data
    params = SearchParams(
        location="London",
        buy_rent="rent",
        max_days_since_added=1,
        radius=0,
    )
    logger.info(f"Searching for properties in {params.location}...")
    logger.info(f"Search parameters: {params}")
    search_results = json.loads(SearchManager(params))
    logger.info(
        f"Search completed. Found {sum(len(v['properties']) for v in search_results['SearchResults'].values())} properties."
    )
    # Download / Save the data

    logger.info("Saving search results to JSON...")
    file_name = f"search_results_{params.location}_{params.buy_rent}_{datetime.datetime.now().date()}.json"
    logger.info(f"Saving results to {file_name}...")
    pathlib.Path("results").mkdir(parents=True, exist_ok=True)
    with open(pathlib.Path("results") / file_name, "w") as f:
        json.dump(search_results, f, indent=4)
    logger.info(f"results saved at results/{file_name}")

    # Process / Clean, Filter, Transform
    # Analyze / Visualize, Report, Statistics, Machine Learning, etc.
    # Present / UI, Web, API, etc.
    # Select / Filter, Sort, Rank, etc.
    # Export / Save, Share, Publish, etc.

    logger.info("Processing completed.")
    logger.info("Exiting the application.")

    pass


if __name__ == "__main__":
    main()

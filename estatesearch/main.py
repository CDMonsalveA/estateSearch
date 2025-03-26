"""
Main Module for the Estate Search application.
This module controls the flow of the application, including loading configuration,
searching for properties, and saving results.
It serves as the entry point for the application and coordinates the various components.
"""
import json
from estatesearch.search.searchConfig import SearchParams
from estatesearch.search.search import SearchManager

def main():
    """
    Main function to execute the Estate Search application.
    This function will orchestrate the various components of the application,
    including loading configuration, searching for properties, and saving results.
    """
    # Search / Fetch the data
    params = SearchParams(location="London", buy_rent="buy", max_days_since_added=1,
                          max_price=500000,)
    search_results = SearchManager(params)

    # Download / Save the data
    # Save the search results to a JSON file
    json_results = json.loads(search_results)
    with open("search_results.json", "w") as f:
        json.dump(json_results, f, indent=4)
    # Process / Clean, Filter, Transform
    # Analyze / Visualize, Report, Statistics, Machine Learning, etc.
    # Present / UI, Web, API, etc.
    # Select / Filter, Sort, Rank, etc.
    # Export / Save, Share, Publish, etc.

    pass


if __name__ == "__main__":
    main()

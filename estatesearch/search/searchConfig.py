"""Configuration for the estate search application.
This module defines the parameters and settings used for searching properties.
"""

from typing import Any, NamedTuple


class SearchParams(NamedTuple):
    """
    Search parameters for the estate search application.

    Attributes:
        country (str): The country to search in (e.g., "uk", "co")
        buy_rent (str): Indicates whether the search is for buying or renting.
        location (str): The location to search for properties.
        radius (float): The search radius in miles.
        property_type (str): The type of property (e.g., house, flat).
        min_price (int): The minimum price of the property.
        max_price (int): The maximum price of the property.
        min_bedrooms (int): The minimum number of bedrooms.
        max_bedrooms (int): The maximum number of bedrooms.
        min_bathrooms (int): The minimum number of bathrooms.
        max_bathrooms (int): The maximum number of bathrooms.
        max_days_since_added (int): The maximum number of days since added.
        include_sstc (bool): Whether to include properties marked as SSTC (Sold Subject To Contract).
        must_have (str): A list of features that the property must have.
        dont_show (str): A list of features that the property must not have.
        verbose (int): Verbosity level for logging (0: no output, 1: some output, 2: detailed output).
    """

    country = "uk"  # str of a country, (e.g. "uk", "co")
    location: str = "London"  # str of a location, postcode, or train station
    buy_rent: str = "buy"  # "buy" or "rent"
    radius: float = 1  # in miles
    property_type: list = []
    # [] || any combination of only these:
    # bungalow, detached, flat, land, park-home, semi-detached, terraced
    min_price: int = 0  # int(0,inf)<max_price||None
    max_price: int = 10000000  # int(0,inf)>min_price||None
    min_bedrooms: int = 0  # int(0,5)<max_bedrooms||studio=0 || None
    max_bedrooms: int = 10  # int(0,5)>min_bedrooms||studio=0 || None
    max_days_since_added: int = 14  # 1, 3, 7, 14 and only theese
    include_sstc: bool = True  # True or False
    must_have: list = []  # [] || any combination of only these:
    # garden, parking, newHome, retirement, sharedOwnership, auction
    dont_show: list = []  # [] || any combination of only these:
    # newHome, retirement, sharedOwnership, furnishTypes
    # keywords: str = ""  # str of keywords, separated by commas
    verbose: int = 0
    # 0: no output, 1: some output, 2: detailed output, 3: debug output

    def __str__(self):
        """Return a string representation of the search parameters."""
        return f"Search properties in {self.country} for {self.buy_rent}\n \
                in {self.location}"

"""Configuration for the estate search application.
This module defines the parameters and settings used for searching properties.
"""

from typing import NamedTuple, Optional


class SearchParams(NamedTuple):
    """
    Search parameters for the estate search application.

    Attributes:
        country (str): The country code from the following list: "uk", "co".
        buy_rent (str): If searching for "buy" or "rent" properties.
        location (str): The location to search for properties.
        radius (float): The search radius in miles.
        property_type (list[str]): A list of property types to search for.
            Any combination of the following:
            "bungalow", "detached", "flat", "land", "park-home", "semi-detached", "terraced".
        min_price (int): The minimum price of the property. allows 0, inf or None, always 0<=min_price<=max_price.
        max_price (int): The maximum price of the property. allows 0, inf or None, always 0<=min_price<=max_price.
        min_bedrooms (int): The minimum number of bedrooms. allows from 0 (studio) to 5 or None, always 0<=min_bedrooms<=max_bedrooms.
        max_bedrooms (int): The maximum number of bedrooms. allows from 0 (studio) to 5 or None, always 0<=min_bedrooms<=max_bedrooms.
        max_days_since_added (int): The maximum number of days since added. Only allows 1, 3, 7, 14.
        include_sstc (bool): Whether to include properties marked as SSTC (Sold Subject To Contract).
        must_have (list[str]): A list of features that the property must have. Only allows any combination of the following:
            "garden", "parking", "newHome", "retirement", "sharedOwnership", "auction".
        dont_show (list[str]): A list of features that the property must not have. Only allows any combination of the following:
            "newHome", "retirement", "sharedOwnership", "furnishTypes".
        verbose (int): Verbosity level for logging (0: no output, 1: some output, 2: detailed output).
    """

    country = "uk"  # str of a country, (e.g. "uk", "co")
    location: str = "London"  # str of a location, postcode, or train station
    buy_rent: str = "buy"  # "buy" or "rent"
    radius: Optional[float] = None  # in miles
    property_type: Optional[list[str]] = None
    # [] || any combination of only these:
    # bungalow, detached, flat, land, park-home, semi-detached, terraced
    min_price: Optional[int] = None  # int(0,inf)<=max_price||None
    max_price: Optional[int] = None  # int(0,inf)>=min_price||None
    min_bedrooms: Optional[int] = (
        None  # int(0,5)<=max_bedrooms||studio=0 || None
    )
    max_bedrooms: Optional[int] = (
        None  # int(0,5)>=min_bedrooms||studio=0 || None
    )
    max_days_since_added: Optional[int] = None  # 1, 3, 7, 14 and only theese
    include_sstc: Optional[bool] = None  # True or False
    must_have: Optional[list[str]] = (
        None  # [] || any combination of only these:
    )
    # garden, parking, newHome, retirement, sharedOwnership, auction
    dont_show: Optional[list[str]] = (
        None  # [] || any combination of only these:
    )
    # newHome, retirement, sharedOwnership, furnishTypes
    # keywords: str = ""  # str of keywords, separated by commas
    verbose: Optional[int] = 0  # int(0,3) verbosity level
    # 0: no output, 1: some output, 2: detailed output, 3: debug output

    def __str__(self):
        """Return a string representation of the search parameters."""
        return f"Search properties in {self.country} for {self.buy_rent}\n \
                in {self.location}"

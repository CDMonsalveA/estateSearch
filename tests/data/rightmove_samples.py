"""Rightmove.com related sample data."""

from typing import List, NamedTuple

from estatesearch.search.searchConfig import SearchParams


class RMLocationID(NamedTuple):
    """Rightmove location ID.

    Attributes:
        searchText (str): The search text for the location.
        location_type (str): The type of location.
        location_id (str): The ID of the location.
    """

    searchText: str
    locationType: str
    locationID: str


# Example of locations with id an type
location_ids_examples: List[RMLocationID] = [
    # Using Postcode
    RMLocationID("SY3 9EB", "POSTCODE", "4203018"),
    RMLocationID("sy3-9eb", "POSTCODE", "4203018"),
    RMLocationID("W1A 1AA", "POSTCODE", "912358"),
    RMLocationID("w1a-1aa", "POSTCODE", "912358"),
    RMLocationID("B1 1AA", "POSTCODE", "4183557"),
    RMLocationID("CR0 5NS", "POSTCODE", "184365"),
    RMLocationID("CR0-5NS", "POSTCODE", "184365"),
    # Using Area
    RMLocationID("london", "REGION", "87490"),  # 93917 for greater london
    RMLocationID("birmingham", "REGION", "162"),
    RMLocationID("manchester", "REGION", "904"),
    RMLocationID("liverpool", "REGION", "813"),
    RMLocationID("leeds", "REGION", "787"),
    RMLocationID("bristol", "REGION", "219"),
    RMLocationID("edinburgh", "REGION", "475"),
    RMLocationID("glasgow", "REGION", "550"),
    RMLocationID("cardiff", "REGION", "281"),
    RMLocationID("swansea", "REGION", "1305"),
    # Using Train Station
    RMLocationID("paddington", "REGION", "70403"),
]

# Key attributes to be used in the Rightmove API
rightmove_api_keys = [
    "id",
    "bedrooms",
    "bathrooms",
    "numberOfImages",
    "numberOfFloorplans",
    "numberOfVirtualTours",
    "summary",
    "displayAddress",
    "countryCode",
    "location",
    "propertyImages",
    "propertySubType",
    "listingUpdate",
    "premiumListing",
    "featuredProperty",
    "price",
    "customer",
    "distance",
    "transactionType",
    "productLabel",
    "commercial",
    "development",
    "residential",
    "students",
    "auction",
    "feesApply",
    "feesApplyText",
    "displaySize",
    "showOnMap",
    "propertyUrl",
    "contactUrl",
    "staticMapUrl",
    "channel",
    "firstVisibleDate",
    "keywords",
    "keywordMatchType",
    "saved",
    "hidden",
    "onlineViewingsAvailable",
    "lozengeModel",
    "hasBrandPlus",
    "displayStatus",
    "enquiredTimestamp",
    "enquiryAddedTimestamp",
    "enquiryCalledTimestamp",
    "heading",
    "addedOrReduced",
    "formattedBranchName",
    "formattedDistance",
    "propertyTypeFullDescription",
    "isRecent",
    "enhancedListing",
]

# Example of searches with different parameters

searches: List[SearchParams] = [
    SearchParams(location="london", buy_rent="buy", radius=1.0, limit=10),
    SearchParams(location="london", buy_rent="rent", radius=1.0, limit=10),
    SearchParams(
        location="kent",
        buy_rent="buy",
        radius=1.0,
        min_price=100000,
        max_price=500000,
        min_bedrooms=2,
        max_bedrooms=4,
        max_days_since_added=7,
        include_sstc=True,
        must_have=["garden", "parking"],
        dont_show=["newHome", "retirement"],
        verbose=1,
        limit=10,
    ),
    SearchParams(
        location="birmingham",
        buy_rent="rent",
        radius=5.0,
        min_price=500,
        max_price=2000,
        min_bedrooms=1,
        max_bedrooms=3,
        max_days_since_added=3,
        include_sstc=False,
        must_have=["garden"],
        dont_show=["sharedOwnership"],
        verbose=2,
        limit=10,
    ),
]

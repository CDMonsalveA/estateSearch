"""
Definition of the parameters to be obtained from the web portals.
"""

from typing import NamedTuple


class property_details(NamedTuple):
    """
    Named tuple to store the details of the property.
    """

    origin: str
    url: str
    id: str
    published: bool
    archived: bool
    phone: str
    bedrooms: int
    bathrooms: int
    type: str
    property_type: str
    tags: list
    description: str
    title: str
    price: str
    priceType: str
    price_currency: str
    price_sqft: float
    address: str
    postcode: str
    country: str
    latitude: float
    longitude: float
    tenureType: str
    yearsRemainingOnLease: int
    comercial: bool
    buildToRent: bool
    furnished: bool
    features: dict
    history: dict
    photos: list
    floorplans: list
    agency: dict
    industryAffiliations: list
    nearest_airports: list
    nearest_stations: list
    sizings: list
    brochures: list
    transactionType: str
    feesApply: bool
    lettings: bool
    livingCosts: dict

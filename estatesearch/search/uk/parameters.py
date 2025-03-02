"""
Definition of the parameters to be obtained from the web portals.
"""

from typing import NamedTuple


class RightmoveParameters(NamedTuple):
    buy_or_rent: str
    location: str
    radius: float
    min_price: float
    max_price: float
    min_bedrooms: int
    max_bedrooms: int
    property_types: list
    max_days_since_added: int
    include_sstc: bool
    must_have: list
    dont_show: list

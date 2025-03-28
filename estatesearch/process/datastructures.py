"""Collection of data structures used in the estate search application."""

from typing import Any, Dict, List, NamedTuple, Optional


class Media(NamedTuple):
    """
    Media information about a property.
    """

    images: List[str]
    floorPlans: Optional[List[str]]
    videos: Optional[List[str]]
    virtualTours: Optional[List[str]]
    _3DModels: Optional[List[str]]
    epc: Optional[List[str]]
    brochures: Optional[List[str]]
    maps: Optional[List[str]]


class MarketData(NamedTuple):
    """
    Market data information about a property.
    """

    marketComparables: List[Dict[str, Any]]
    rightmoveEstimate: Optional[float]
    soldPrices: Optional[List[Dict[str, int]]]


class PropertyInfo(NamedTuple):
    """
    Basic information about a property.
    """

    id: str
    origin: str
    url: str
    dateOfExtraction: str
    latitude: float
    longitude: float
    propertyName: str
    propertyType: str
    price: float
    priceType: str
    address: str
    postcode: str
    description: str
    bedrooms: int
    bathrooms: int
    tenure: Optional[str]
    yearsRemainingOnLease: Optional[int]
    size: Optional[float]
    sizeUnit: Optional[str]
    commercial: Optional[bool]
    newHome: Optional[bool]
    retirement: Optional[bool]
    nonStandardConstruction: Optional[bool]
    councilState: Optional[bool]

    pointOfReference: Optional[bool]
    distanceToSearchPoint: Optional[float]
    distanceUnit: Optional[str]

    media: Optional[Media]

    marketData: Optional[MarketData]

    # Cost related information
    purchasePrice: Optional[float]
    comparablePrice: Optional[float]
    comparablePriceType: Optional[str]
    bridgeOrFinanceCosts: Optional[float]
    stampDutyCosts: Optional[float]
    legalCosts: Optional[float]
    mortgageCosts: Optional[float]

    ## fees

    financeFees: Optional[float]
    financingCosts: Optional[float]
    auctioneerFees: Optional[float]
    sellersFees: Optional[float]
    solicitorFees: Optional[float]
    otherFees: Optional[float]

    ## Other costs

    councilTax: Optional[float]
    serviceCharge: Optional[float]
    groundRent: Optional[float]
    insuranceCosts: Optional[float]
    maintenanceCosts: Optional[float]
    managementCosts: Optional[float]

    ## Other costs to add value

    renovationCosts: Optional[float]
    refurbishmentCosts: Optional[float]

    ## Income related information

    rentalIncome: Optional[float]
    rentalIncomeType: Optional[str]

    isGoodDeal: Optional[bool]

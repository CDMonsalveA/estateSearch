"""
Definition of the parameters to be obtained from the web portals.
"""

from typing import NamedTuple


class PropertyDetails(NamedTuple):
    """
    Named tuple to store the details of the property.
    """

    origin: str
    url: str
    id: str
    published: bool
    archived: bool
    propertyPhrase: str
    description: str
    pageTitle: str
    text: dict  # description, PropertyPhrase, disclaimer, auctionFeesDisclaimer, auctionFeesDisclaimer, guidePriceDisclaimer, reservePriceDisclaimer, newHomesBrochure, pageTitle, shortDescription
    primaryPrice: str
    secondaryPrice: str
    displayPriceQualifier: str
    pricePerSqFt: str
    address: str  # displayAddress
    postcode: str
    keyFeatures: list
    images: dict  # imageUrls, caption
    broschures: dict
    floorplans: str  # url
    video: str  # url
    sellerInfo: dict  # customer
    rooms: dict
    latitude: str
    longitude: str
    pinType: str
    nearestAirports: list
    nearestStations: list
    sizings: dict

    epcGraphs: dict
    bedrooms: int
    bathrooms: int
    transactionType: str
    tags: list
    listingHistory: dict

    feesApply: bool

    contactInfo: dict

    lettings: dict

    tenureType: str
    yearsRemainingOnLease: int

    propertyType: str
    propertySubType: str
    businessForSale: bool
    comercial: bool
    affordableBuyingScheme: bool
    sharedOwnership: dict
    retirement: bool

    councilTaxExempt: bool
    councilTaxIncluded: bool
    annualGroundRent: str
    groundRentReviewPeriodInYears: int
    groundRentPercentageIncrease: str
    annualServiceCharge: str
    councilTaxBand: str
    domesticRates: str

    features: dict  # electricity, broadband, water, sewerage, heating, accessibility, parking, garde, risks, obligations

    EPC: str

    isAuthenticated: bool

    added: str
    auctionOnly: bool
    preOwned: str

"""
Definition of the parameters to be obtained from the web portals.
"""

from typing import NamedTuple


class propertiesParameters(NamedTuple):
    """
    Parameters for the properties to be obtained from the web portals.

    The Literal information from Rightmove search:
    'id', 'bedrooms', 'bathrooms', 'numberOfImages', 'numberOfFloorplans', 'numberOfVirtualTours', 'summary', 'displayAddress', 'countryCode', 'location', 'propertyImages', 'propertySubType', 'listingUpdate', 'premiumListing', 'featuredProperty', 'price', 'customer', 'distance', 'transactionType', 'productLabel', 'commercial', 'development', 'residential', 'students', 'auction', 'feesApply', 'feesApplyText', 'displaySize', 'showOnMap', 'propertyUrl', 'contactUrl', 'staticMapUrl', 'channel', 'firstVisibleDate', 'keywords', 'keywordMatchType', 'saved', 'hidden', 'onlineViewingsAvailable', 'lozengeModel', 'hasBrandPlus', 'displayStatus', 'enquiredTimestamp', 'enquiryAddedTimestamp', 'enquiryCalledTimestamp', 'heading', 'addedOrReduced', 'formattedBranchName', 'formattedDistance', 'propertyTypeFullDescription', 'isRecent', 'enhancedListing'
    """

    id: str
    bedrooms: int
    bathrooms: int
    numberOfImages: int
    numberOfFloorplans: int
    numberOfVirtualTours: int
    summary: str
    displayAddress: str
    countryCode: str
    location: str
    propertyImages: str
    propertySubType: str
    listingUpdate: str
    premiumListing: str
    featuredProperty: str
    price: str
    customer: str
    distance: str
    transactionType: str
    productLabel: str
    commercial: str
    development: str
    residential: str
    students: str
    auction: str
    feesApply: str
    feesApplyText: str
    displaySize: str
    showOnMap: str
    propertyUrl: str
    contactUrl: str
    staticMapUrl: str
    channel: str
    firstVisibleDate: str
    keywords: str
    keywordMatchType: str
    saved: str
    hidden: str
    onlineViewingsAvailable: str
    lozengeModel: str
    hasBrandPlus: str
    displayStatus: str
    enquiredTimestamp: str
    enquiryAddedTimestamp: str
    enquiryCalledTimestamp: str
    heading: str
    addedOrReduced: str
    formattedBranchName: str
    formattedDistance: str
    propertyTypeFullDescription: str
    isRecent: str
    enhancedListing: str

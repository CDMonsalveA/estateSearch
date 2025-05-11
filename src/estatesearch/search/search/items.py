# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SearchItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class PropertyItem(scrapy.Item):

    source = scrapy.Field()
    id = scrapy.Field()
    transactionType = scrapy.Field()  # transactionType
    bedrooms = scrapy.Field()
    bathrooms = scrapy.Field()
    numberOfImages = scrapy.Field()
    numberOfFloorplans = scrapy.Field()
    displayAddress = scrapy.Field()
    propertyType = scrapy.Field()  # propertySubType
    summary = scrapy.Field()
    listingUpdateReason = scrapy.Field()  # listingUpdate > listingUpdateReason
    price = scrapy.Field()
    price_frequency = scrapy.Field()
    price_currencyCode = scrapy.Field()
    contactTelephone = scrapy.Field() # customer > contactTelephone
    contact_branchDisplayName = scrapy.Field() # customer > contactBranchDisplayName
    commercial = scrapy.Field() # commercial
    development = scrapy.Field() # development
    residential = scrapy.Field() # residential
    students = scrapy.Field() # students
    auction = scrapy.Field() # auction
    feesApply = scrapy.Field() # feesApply
    displaySize = scrapy.Field() # displaySize
    propertyUrl = scrapy.Field()  # propertyUrl
    firstVisibleDate = scrapy.Field()  # firstVisibleDate
    propertyTypeFullDescription = scrapy.Field()  # propertyTypeFullDescription
    isRecent = scrapy.Field()  # isRecent


class PropertyImageItem(scrapy.Item):
    id = scrapy.Field()
    imageUrl = scrapy.Field()
    order = scrapy.Field()
    isPrimary = scrapy.Field()
    isFloorplan = scrapy.Field()
    isVideo = scrapy.Field()
    isVirtualTour = scrapy.Field()
    isInteractiveFloorplan = scrapy.Field()
    pass


class PropertyLocationItem(scrapy.Item):
    id = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    displayAddress = scrapy.Field()
    countryCode = scrapy.Field()
    countryName = scrapy.Field()
    regionName = scrapy.Field()
    districtName = scrapy.Field()
    subDistrictName = scrapy.Field()
    pass

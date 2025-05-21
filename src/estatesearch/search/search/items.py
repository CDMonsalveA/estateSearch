# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PropertyItem(scrapy.Item):

    source = scrapy.Field()
    url = scrapy.Field()  # propertyUrl
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
    listingUpdateDate = scrapy.Field()  # listingUpdate > listingUpdateDate
    price = scrapy.Field()
    price_frequency = scrapy.Field()
    price_currencyCode = scrapy.Field()
    contactTelephone = scrapy.Field()  # customer > contactTelephone
    contact_branchDisplayName = scrapy.Field()  # customer > contactBranchDisplayName
    commercial = scrapy.Field()  # commercial
    development = scrapy.Field()  # development
    residential = scrapy.Field()  # residential
    students = scrapy.Field()  # students
    auction = scrapy.Field()  # auction
    feesApply = scrapy.Field()  # feesApply
    displaySize = scrapy.Field()  # displaySize
    firstVisibleDate = scrapy.Field()  # firstVisibleDate
    propertyTypeFullDescription = scrapy.Field()  # propertyTypeFullDescription
    isRecent = scrapy.Field()  # isRecent
    # Location related fields
    latitude = scrapy.Field()
    longitude = scrapy.Field()

    # ----- FROM pageMODEL propertyData Per each property page-----
    status = scrapy.Field()  # .status .published
    price_displayPriceQualifier = scrapy.Field()
    brochure_url = scrapy.Field()  # brochures > url -- first
    epcGraph = scrapy.Field()  # epcGraph
    feesApply = scrapy.Field()  # feesApply
    lettings = scrapy.Field()  # lettings
    tenure_type = scrapy.Field()  # tenure > ternureType
    tenure_years = scrapy.Field()  # tenure > yearsRemainingOnLease
    propertySubType = scrapy.Field()  # propertySubType
    pinType = scrapy.Field()  # location > pinType

    # ----- FROM pageMODEL address Per each property page-----
    displayAddress = scrapy.Field()
    countryCode = scrapy.Field()
    ukCountry = scrapy.Field()
    outcode = scrapy.Field()
    incode = scrapy.Field()

    isAuthenticated = scrapy.Field()
    # ----- FROM pageMODEL analyticsInfo Per each property page-----
    postcode = scrapy.Field()  # analyticsProperty .postcode
    added = scrapy.Field()  # analyticsProperty .added
    auctionOnly = scrapy.Field()  # analyticsProperty .auctionOnly
    businessForSale = scrapy.Field()  # analyticsProperty .businessForSale
    letAgreed = scrapy.Field()  # analyticsProperty .letAgreed
    lettingType = scrapy.Field()  # analyticsProperty .lettingType
    ownership = scrapy.Field()  # analyticsProperty .ownership
    preOwned = scrapy.Field()  # analyticsProperty .preOwned
    price_pageModel = scrapy.Field()  # analyticsProperty .price
    priceQualifier = scrapy.Field()  # analyticsProperty .priceQualifier
    propertyType = scrapy.Field()  # analyticsProperty .propertyType
    propertySubType = scrapy.Field()  # analyticsProperty .propertySubType
    retirement = scrapy.Field()  # analyticsProperty .retirement
    soldSTC = scrapy.Field()  # analyticsProperty .soldSTC

    # Related to living costs
    # FROM pageMODEL propertyData Per each property page
    councilTaxExempt = scrapy.Field()  # livingCosts > councilTaxExempt
    councilTaxIncluded = scrapy.Field()  # livingCosts > councilTaxIncluded
    annualGroundRent = scrapy.Field()  # livingCosts > annualGroundRent
    groundRentReviewPeriodInYears = scrapy.Field()  # livingCosts > groundRentReviewPeriodInYears
    groundRentPercentageIncrease = scrapy.Field()  # livingCosts > groundRentPercentageIncrease
    annualServiceCharge = scrapy.Field()  # livingCosts > annualServiceCharge
    councilTaxBand = scrapy.Field()  # livingCosts > councilTaxBand
    domesticRates = scrapy.Field()  # livingCosts > domesticRates
    # Features related fields
    electricity = scrapy.Field()  # features > electricity
    broadband = scrapy.Field()  # features > broadband
    water = scrapy.Field()  # features > water
    sewarage = scrapy.Field()  # features > sewage
    heating = scrapy.Field()  # features > heating
    accessibility = scrapy.Field()  # features > accessibility
    parking = scrapy.Field()  # features > parking
    garden = scrapy.Field()  # features > garden
    risks = scrapy.Field()  # features > risks
    obligations = scrapy.Field()  # features > obligations


class PropertyImageItem(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    caption = scrapy.Field()
    type = scrapy.Field()


class PropertyRoomItem(scrapy.Item):
    # FROM pageMODEL propertyData Per each property page
    id = scrapy.Field()
    name = scrapy.Field()  # rooms > name
    description = scrapy.Field()  # rooms > description
    width = scrapy.Field()  # rooms > width
    length = scrapy.Field()  # rooms > length
    unit = scrapy.Field()  # rooms > unit
    dimension = scrapy.Field()  # rooms > dimension


class PropertyInterestPointItem(scrapy.Item):
    # summary of nearest points of interest
    id = scrapy.Field()
    type = scrapy.Field()  # manually added from nearestAirports or nearestStations
    name = scrapy.Field()  # nearestAirports > name or nearestStations > name
    distance = scrapy.Field()  # nearestAirports > distance or nearestStations > distance
    unit = scrapy.Field()  # nearestAirports > unit or nearestStations > unit

# Rightmove UK

The Rightmove class is used to search for properties
on the Rightmove website using the following parameters:

URL structure:

- <https://www.rightmove.co.uk/>

    property-for-sale/||property-to-rent/

    find.html?||map.html?

    searchLocation=[postcode||town||city||train-station||county]
    &useLocationIdentifier=[true||false]
    &locationIdentifier=[type^locationId]
    &sortType=[1||2||3||4||5||6||7||8||9||10]
    &numberOfPropertiesPerPage=[int]
    &index=[int]
    &channel=[BUY||RENT]
    &areaSizeUnit=[sqft||sqm]
    &radius=[miles]
    &minPrice=[minPrice]
    &maxPrice=[maxPrice]
    &minBedrooms=[minBedrooms||studio=0]
    &maxBedrooms=[maxBedrooms||studio=0]
    &propertyTypes=[
                    bungalow
                    %2Cdetached
                    %2Cflat
                    %2Cland
                    %2Cpark-home
                    %2Csemi-detached
                    %2Cterraced
                    ]
    &maxDaysSinceAdded=[1||3||7||14]
    &_includeSSTC=[on||off]
    &includeSSTC=[true||false]
    &mustHave=[
                garden
                %2Cparking
                %2CnewHome
                %2Cretirement
                %2CsharedOwnership
                %2Cauction
            ]
    &dontShow=[newHome%2Cretirement%2CsharedOwnership&furnishTypes]
    &furnishTypes=
    &keywords=

API structure:

- <https://www.rightmove.co.uk/api/_search>?
    locationIdentifier=[type^locationId]
    &numberOfPropertiesPerPage=[int]
    &channel=BUY
    &sortType=[1||2||3||4||5||6||7||8||9||10]
    &index=[int]
    &radius=[miles]
    &minPrice=[minPrice]
    &maxPrice=[maxPrice]
    &minBedrooms=[minBedrooms||studio=0]
    &maxBedrooms=[maxBedrooms||studio=0]
    &propertyTypes=[
                    bungalow
                    %2Cdetached
                    %2Cflat
                    %2Cland
                    %2Cpark-home
                    %2Csemi-detached
                    %2Cterraced
                    ]
    &maxDaysSinceAdded=[1||3||7||14]
    &_includeSSTC=[on||off]
    &includeSSTC=[true||false]
    &mustHave=[
                garden
                %2Cparking
                %2CnewHome
                %2Cretirement
                %2CsharedOwnership
                %2Cauction
            ]
    &dontShow=[newHome%2Cretirement%2CsharedOwnership&furnishTypes]

    &viewType=LIST
    &areaSizeUnit=sqft
    &currencyCode=GBP
    &isFetching=false
    &viewport=

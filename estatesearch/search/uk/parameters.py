"""
Definition of the parameters to be obtained from the web portals.
"""

from typing import NamedTuple


"""
Parameters for the properties to be obtained from the web portals.

The Literal information from Rightmove search:
"id": 158844158,
"bedrooms": 2,
"bathrooms": 1,
"numberOfImages": 7,
"numberOfFloorplans": 1,
"numberOfVirtualTours": 1,
"summary": "Escape to the Kew Gardens: Your Blank Canvas Awaits!This rare two-bedroom ground floor flat, moments from the world-renowned Kew Gardens, offers a unique opportunity to create your dream home. Boasting a spacious layout with two double bedrooms, a generous reception, private garden and garage.",
"displayAddress": "Kew Road, London, TW9",
"countryCode": "GB",
"location": {
    "latitude": 51.47724,
    "longitude": -0.29045
},
"propertyImages": {
    "images": [
        {
            "srcUrl": "https://media.rightmove.co.uk:443/dir/crop/10:9-16:9/278k/277739/158844158/277739_28022025_IMG_07_0001_max_476x317.jpeg",
            "url": "278k/277739/158844158/277739_28022025_IMG_07_0001.jpeg",
            "caption": null
        },
        {
            "srcUrl": "https://media.rightmove.co.uk:443/dir/crop/10:9-16:9/278k/277739/158844158/277739_28022025_IMG_01_0000_max_476x317.jpeg",
            "url": "278k/277739/158844158/277739_28022025_IMG_01_0000.jpeg",
            "caption": null
        },
        {
            "srcUrl": "https://media.rightmove.co.uk:443/dir/crop/10:9-16:9/278k/277739/158844158/277739_28022025_IMG_02_0000_max_476x317.jpeg",
            "url": "278k/277739/158844158/277739_28022025_IMG_02_0000.jpeg",
            "caption": null
        },
        {
            "srcUrl": "https://media.rightmove.co.uk:443/dir/crop/10:9-16:9/278k/277739/158844158/277739_28022025_IMG_03_0000_max_476x317.jpeg",
            "url": "278k/277739/158844158/277739_28022025_IMG_03_0000.jpeg",
            "caption": null
        },
        {
            "srcUrl": "https://media.rightmove.co.uk:443/dir/crop/10:9-16:9/278k/277739/158844158/277739_28022025_IMG_04_0000_max_476x317.jpeg",
            "url": "278k/277739/158844158/277739_28022025_IMG_04_0000.jpeg",
            "caption": null
        },
        {
            "srcUrl": "https://media.rightmove.co.uk:443/dir/crop/10:9-16:9/278k/277739/158844158/277739_28022025_IMG_06_0000_max_476x317.jpeg",
            "url": "278k/277739/158844158/277739_28022025_IMG_06_0000.jpeg",
            "caption": null
        },
        {
            "srcUrl": "https://media.rightmove.co.uk:443/dir/crop/10:9-16:9/278k/277739/158844158/277739_28022025_IMG_05_0000_max_476x317.jpeg",
            "url": "278k/277739/158844158/277739_28022025_IMG_05_0000.jpeg",
            "caption": null
        }
    ],
    "mainImageSrc": "https://media.rightmove.co.uk:443/dir/crop/10:9-16:9/278k/277739/158844158/277739_28022025_IMG_07_0001_max_476x317.jpeg",
    "mainMapImageSrc": "https://media.rightmove.co.uk:443/dir/crop/10:9-16:9/278k/277739/158844158/277739_28022025_IMG_07_0001_max_296x197.jpeg"
},
"propertySubType": "Ground Flat",
"listingUpdate": {
    "listingUpdateReason": "new",
    "listingUpdateDate": "2025-03-01T17:42:01Z"
},
"premiumListing": false,
"featuredProperty": true,
"price": {
    "amount": 480000,
    "frequency": "not specified",
    "currencyCode": "GBP",
    "displayPrices": [
        {
            "displayPrice": "\u00a3480,000",
            "displayPriceQualifier": "Offers in Region of"
        }
    ]
},
"customer": {
    "branchId": 277739,
    "brandPlusLogoURI": "/278k/277739/branch_rmchoice_logo_277739_0000.png",
    "contactTelephone": "020 8629 9603",
    "branchDisplayName": "Gooms, Richmond",
    "branchName": "Richmond",
    "brandTradingName": "Gooms",
    "branchLandingPageUrl": "/estate-agents/agent/Gooms/Richmond-277739.html",
    "development": false,
    "showReducedProperties": true,
    "commercial": false,
    "showOnMap": true,
    "enhancedListing": false,
    "developmentContent": null,
    "buildToRent": false,
    "buildToRentBenefits": [],
    "brandPlusLogoUrl": "https://media.rightmove.co.uk:443/278k/277739/branch_rmchoice_logo_277739_0000.png"
},
"distance": null,
"transactionType": "buy",
"productLabel": {
    "productLabelText": null,
    "spotlightLabel": false
},
"commercial": false,
"development": false,
"residential": true,
"students": false,
"auction": false,
"feesApply": false,
"feesApplyText": null,
"displaySize": "797 sq. ft.",
"showOnMap": true,
"propertyUrl": "/properties/158844158#/?channel=RES_BUY",
"contactUrl": "/property-for-sale/contactBranch.html?propertyId=158844158",
"staticMapUrl": null,
"channel": "BUY",
"firstVisibleDate": "2025-03-01T17:36:16Z",
"keywords": [],
"keywordMatchType": "no_keyword",
"saved": false,
"hidden": false,
"onlineViewingsAvailable": false,
"lozengeModel": {
    "matchingLozenges": []
},
"hasBrandPlus": true,
"displayStatus": "",
"enquiredTimestamp": null,
"enquiryAddedTimestamp": null,
"enquiryCalledTimestamp": null,
"heading": "Featured Property",
"addedOrReduced": "Added on 01/03/2025",
"formattedBranchName": " by Gooms, Richmond",
"formattedDistance": "",
"propertyTypeFullDescription": "2 bedroom ground floor flat for sale",
"isRecent": false,
"enhancedListing": false
"""

    
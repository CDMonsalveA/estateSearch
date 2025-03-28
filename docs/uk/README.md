# UNITED KINGDOM

[Home Professionals Docs](https://mirror-painter-56a.notion.site/20af153f59ff4fa5aa0afcfb0d6d05ce?v=f29c02a3f9df4338b4f69704a0611248)

<!-- TODO: #2 Add main strategy for properties in the uk -->

The following document outlines the main strategy for properties in the UK. It is a work in progress and will be updated as we refine our approach. The strategy is based on the estateSearch algorithm, which is designed to identify high-quality real estate opportunities in the UK market.

## Step 1: Data Collection

Collect data from various sources, including property listings, market trends, and demographic information.

Here are some of the sources we will be using:

- Property Portals:

  - [ ] [Rightmove](https://www.rightmove.co.uk/)
  - [ ] [Zoopla](https://www.zoopla.co.uk/)
  - [ ] [OnTheMarket](https://www.onthemarket.com/)
  - [ ] [PrimeLocation](https://www.primelocation.com/)
  - [ ] [PropertyPal](https://www.propertypal.com/)
  - [ ] [PropertyNews](https://www.propertynews.com/)
  - [ ] [Nestoria](https://www.nestoria.co.uk/)

- Auction Houses Websites:

  - [ ] [Savills](https://www.savills.co.uk/auctions)
  - [ ] [Allsop](https://www.allsop.co.uk/auctions)
  - [ ] [Pugh & Co](https://www.pugh-auctions.com/)
  - [ ] [BidX1](https://bidx1.com/)
  - [ ] [Auction House](https://www.auctionhouse.co.uk/)
  - [ ] [SVA Property Auctions](https://www.svaprop.com/)
  - [ ] [Barnard Marcus](https://www.barnardmarcusauctions.co.uk/)
  - [ ] [Clive Emson](https://www.cliveemson.co.uk/)
  - [ ] [McHugh & Co](https://www.mchughandco.com/)
  - [ ] [SDL Property Auctions](https://www.sdlauctions.co.uk/)
  - [ ] [Auction House London](https://www.auctionhouselondon.co.uk/)
  - [ ] [Auction House Scotland](https://www.auctionhousescotland.co.uk/)
  - [ ] [Auction House Wales](https://www.auctionhousewales.co.uk/)
  - [ ] [Auction House Northern Ireland](https://www.auctionhouseni.com/)
  - [ ] [Auction House Ireland](https://www.auctionhouseireland.com/)

- Market Data:

  - [ ] [Land Registry](https://www.gov.uk/government/organisations/land-registry)
  - [ ] [Office for National Statistics (ONS)](https://www.ons.gov.uk/)
  - [ ] [UK House Price Index](https://www.gov.uk/government/collections/uk-house-price-index-reports)

- Demographic Data:

  - [ ] [UK Census Data](https://www.ons.gov.uk/census)
  - [ ] [Local Authority Data](https://data.london.gov.uk/dataset/local-authority-data)

The data will be collected using web scraping techniques and APIs where available. The data will be stored in a database for further analysis.

## Step 2: Data Downloading

The data will be downloaded from the sources listed above. The data will be stored in a database for further analysis.

Proposed data management system:

|Pros vs. Cons|JSON|SQLite|PostgreSQL|MongoDB|
|---|---|---|---|---|
|Pros|Easy to read and write, lightweight, no setup required|Lightweight, easy to set up, no external dependencies|Powerful, supports complex queries, good for large datasets|Flexible schema, good for unstructured data|
|Cons|Not suitable for large datasets, no support for complex queries|Limited to small datasets, not suitable for complex queries|Requires setup and maintenance, more complex to use|Requires setup and maintenance, more complex to use|

- [ ] JSON: Data will be stored in JSON format for easy readability and portability.
- [ ] SQLite: Data will be stored in SQLite format for lightweight storage and easy setup. This is suitable for small datasets and simple queries.
- [ ] PostgreSQL: Data will be stored in PostgreSQL format for powerful querying and support for large datasets. This is suitable for complex queries and large datasets.
- [ ] MongoDB: Data will be stored in MongoDB format for flexible schema and support for unstructured data. This is suitable for large datasets and complex queries.
- [ ] CSV: Data will be stored in CSV format for easy readability and portability. This is suitable for small datasets and simple queries.

## Step 3: Data Processing

Once the data is collected, it will be processed to extract relevant information. The basic information needed for a property analysis includes:

- Search Related Data: Used to determine duplicates and filter out irrelevant data or fraudulent listings.

  - [ ] origin: The source of the data (e.g., Rightmove, Zoopla, etc.)
  - [ ] dateOfExtraction: The date the data was extracted
  - [ ] latitude: The latitude of the property location
  - [ ] longitude: The longitude of the property location
  - [ ] propertyId: The unique identifier for the property
  - [ ] propertyName: The name of the property (e.g., "3 bedroom flat")
  - [ ] metaData: Additional metadata about the property (e.g., number of bedrooms, bathrooms, etc.)

- Property Related Data: Used to caracterize the property.

  - [ ] propertyType: The type of property (e.g., flat, house, etc.)
  - [ ] price: The price of the property
  - [ ] address: The address of the property
  - [ ] postcode: The postcode of the property
  - [ ] description: The description of the property
  - [ ] bedrooms: The number of bedrooms in the property
  - [ ] bathrooms: The number of bathrooms in the property
  - [ ] tenure: The tenure of the property (e.g., freehold, leasehold, etc.)
  - [ ] yearsRemainingOnLease: The number of years remaining on the lease
  - [ ] size: The size of the property (e.g., square feet, square meters, etc.)
  - [ ] commercial: Whether the property is commercial or residential
  - [ ] overATrade: Whether the property is over a trade
  - [ ] newBuild: Whether the property is a new build
  - [ ] retirement: Whether the property is for retirement
  - [ ] nonStandardConstruction: Whether the property is of non-standard construction (e.g., timber frame, steel frame, concrete, etc.)
  - [ ] councilState: whether the property is a council state
  - [ ] distanceToSearchPoint: The distance of the property to the search point.

- Media Related Data: Used to show the property and use computer vision.

  - [ ] images: The images of the property
  - [ ] floorPlan: The floor plan of the property
  - [ ] video: The video of the property
  - [ ] virtualTour: The virtual tour of the property
  - [ ] 3DModel: The 3D model of the property
  - [ ] EPC: The Energy Performance Certificate of the property

- Market Related Data: Used to determine the market value of the property.

  - [ ] marketComparables: List of comparable properties in the market
  - [ ] marketPrices: Estimated market prices for the property
  - [ ] marketTrends: Market trends for the property
  - [ ] marketRentals: Rental prices for the property or similar properties
  - [ ] marketForecast: Forecasted market trends for the property
  - [ ] marketAnalysis: Analysis of the market for the property

- Costs Related Data: Used to determine the costs of the property.

  - [ ] purchasePrice: The purchase price of the property.
  - [ ] comparablePrice: The comparable price of the property.
  - [ ] bridgeOrFinanceCosts: The bridge or finance costs of the property.
  - [ ] stampDutyCost: The stamp duty of the property.
  - [ ] legalCosts: The legal costs of the property.
  - [ ] mortgageCost: The mortgage cost of the property.
  <!-- Fees -->
  - [ ] financeFee: The finance fee of the property.
  - [ ] financingCost: The financing cost of the property.
  - [ ] auctioneerFee: The auctioneer fee of the property.
  - [ ] sellersFee: The sellers fee of the property.
  - [ ] solicitorFee: The solicitor fee of the property.
  - [ ] otherFees: The other fees of the property.
  <!-- Other Costs -->
  - [ ] councilTax: The council tax of the property.
  - [ ] ServiceCharge: The service charge of the property.
  - [ ] groundRent: The ground rent of the property.
  - [ ] insuranceCost: The insurance cost of the property.
  - [ ] maintenanceCost: The maintenance cost of the property.
  - [ ] managementCost: The management cost of the property.
  <!-- Other Costs to Add Value -->
  - [ ] renovationCost: The renovation cost of the property.
  - [ ] leaseExtensionCost: The lease extension cost of the property.
  <!-- Income -->
  - [ ] rentalIncome: The rental income of the property.

### Extra Step: Legal Pack Analysis

The legal pack analysis is a crucial step in the property analysis process. It involves reviewing the legal documents related to the property, including the title deeds, lease agreements, and any other relevant documents. This step is essential to ensure that there are no legal issues or complications associated with the property.

At the moment, we are not able to automate this step. However, we will be working on automating this step in the future. In the meantime, we recommend that you review the legal documents carefully and seek legal advice if necessary.

## Step 4: Data Analysis

Several strategies can be used to analyze the data and identify high-quality real estate opportunities. The strategies will be based on the data collected in Step 1 and processed in Step 3.

### Filtering and Sorting

In order to identify high-quality real estate opportunities, we will filter and sort the data based on various criteria. This will include filtering by property type, price range, location, and other relevant factors. The filtered data will then be sorted based on the criteria that are most important to the investor.

### Basic Cost Analysis

A basic cost analysis will be performed to determine the costs associated with the property. This analysis will include the purchase price, comparable price, bridge or finance costs, stamp duty, legal costs, mortgage costs, and other fees. The analysis will also include the council tax, service charge, ground rent, insurance cost, maintenance cost, management cost, renovation cost, lease extension cost, and rental income.

At the end of the analysis, we will have a clear understanding of the costs associated with the property and whether it is a good investment opportunity based on the return on investment (ROI) and cash flow.

### Advanced Cost Analysis

Addition to the basic cost analysis, we will also perform an advanced cost analysis using machine learning algorithms. This analysis will include the use of regression models, clustering algorithms, and other advanced techniques to identify patterns and trends in the data.

- [ ] Use of regression models to predict the future value of the property based on historical data and market trends.
- [ ] Use of clustering algorithms to group similar properties together and identify patterns in the data.
- [ ] Use of classification algorithms to classify properties based on their characteristics and identify high-quality investment opportunities.
- [ ] Use of natural language processing (NLP) techniques to analyze the text data in the property descriptions and identify key features and trends.
- [ ] Use of computer vision techniques to analyze the images and videos of the properties and identify key features and trends.
- [ ] Use of computer vision techniques to identify the refurbishment potential of the property and estimate the costs associated with the refurbishment.
- [ ] Use of Optical Character Recognition (OCR) techniques to extract text from images and documents and analyze the legal documents related to the property.
- [ ] Use of Large Language Models (LLMs) to analyze the text data in the property descriptions and identify key features and trends.
- [ ] Use of LLMs and RAG (Retrieval-Augmented Generation) to answer questions related to the property and provide insights based on the data collected.

### Step 5: Data Visualization

Once the data has been analyzed, it will be visualized using various techniques. This will include the use of charts, graphs, and maps to present the data in a clear and concise manner. The visualizations will help to identify trends and patterns in the data and provide insights into the real estate market.

- [ ] Provide a dashboard with key metrics and visualizations to help investors make informed decisions and select the best investment opportunities to be exported as a PDF report.

### Step 6: Data Export

The final step in the process is to export the data and visualizations. This will include exporting the data in various formats, including CSV, JSON, and PDF. The exported data will be used to create reports and presentations for investors.

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

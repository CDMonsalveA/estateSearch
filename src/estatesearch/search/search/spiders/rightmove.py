import scrapy


class RightmoveSpider(scrapy.Spider):
    name = "rightmove"
    allowed_domains = ["www.rightmove.co.uk"]
    start_urls = ["https://www.rightmove.co.uk/"]

    # search attributes
    search_buy_or_rent: str = None  # "buy" or "rent"
    search_location: str = None  # Location to search for properties
    search_radius: float = None  # Radius of the search in miles
    search_property_type: list[str] = None # A list of any from "bungalow", "detached", "flat", "land", "park-home", "semi-detached", "terraced".
    search_min_price: int = None  # Minimum price of the property
    search_min_price: int = None  # Maximum price of the property
    search_min_bedrooms: int = None  # Minimum number of bedrooms
    search_max_days_since_added: int = None  # Maximum number of days since added Only allows 1, 3, 7, 14
    search_include_sstc: bool = None  # Whether to include properties marked as SSTC (Sold Subject To Contract)
    search_must_have: list[str] = None  # A list of features that the property must have. Only allows any combination of the following: "garden", "parking", "newHome", "retirement", "sharedOwnership", "auction".
    search_dont_show: list[str] = None  # A list of features that the property must not have. Only allows any combination of the following: "newHome", "retirement", "sharedOwnership", "furnishTypes".
    search_limit: int = None  # Limit of properties to return

    API_PROPERTIES_PER_PAGE: int = 499 # Number of properties per page in the API response
    API_LIMIT: int = 1247 # Maximum lower index for the API request

    def parse(self, response):
        pass

    # Functions that help with the search process
    def api_url(self):
        pass

    def search_location_id(self, location):
        pass
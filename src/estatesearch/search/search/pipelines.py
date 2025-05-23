# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from .items import (
    PropertyImageItem,
    PropertyInterestPointItem,
    PropertyItem,
    PropertyRoomItem,
)


class SearchPipeline:
    """
    This pipeline is used to process the scraped items. It is responsible for
    cleaning, validating, and storing the data. The pipeline can be configured
    to perform different actions based on the item type.
    """

    def __init__(self):

        pass

    def open_spider(self, spider):
        """This method is called when the spider is opened. It can be used to
        initialize resources or perform setup tasks.
        """
        pass

    def close_spider(self, spider):
        """This method is called when the spider is closed. It can be used to
        clean up resources or perform final tasks.
        """
        pass

    def process_item(self, item, spider):
        """There are 4 items and each type represemts a table in the database."""
        return item
"""Data processing module for estate search."""


class DataProcessor:
    """Manager of the long-term data management system.
    Functions:
        - Turn the data in the sort-term data base into long-term data base (in small chunks to avoid memory issues).
            - Load the short-term data base.
            - Parse the short-term data base.
            - Save the long-term data base into a file.
            - Update the long-term data base with the short-term data base.
        - Eliminate duplicates in the long-term data base.
        - Format the long-term data base for saving.
        - Ensure the long-term data base is in a consistent format.
        - Save the long-term data base into a file.
    """


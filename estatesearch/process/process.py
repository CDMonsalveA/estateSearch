"""Data processing module for estate search."""

import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


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

    def __init__(self, stm_dir, stm_type: str, ltm_dir, ltm_type: str):
        """Initialize the data processor with the short-term and long-term data base directories and types."""
        self.stm_dir = stm_dir
        self.stm_type = stm_type
        self.ltm_dir = ltm_dir
        self.ltm_type = ltm_type

        self.register_path = Path(self.stm_dir) / "registered_files.txt"
        self.registered_files = []

        self.stm_data = None
        self.ltm_data = None

    def read_json(self, file_path) -> dict:
        """Read a JSON file and return the data."""
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def to_json(self, data, file_path) -> None:
        """Write data to a JSON file."""
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def read_registered_files(self) -> list:
        """Read the registered files from the .txt file that contains the list of registered files."""
        if not self.register_path.exists():
            return []

        with open(self.register_path, "r", encoding="utf-8") as file:
            registered_files = [line.strip() for line in file.readlines()]
        return registered_files

    def write_registered_files(self, registered_files: list[str]) -> None:
        """Write/Update  the registered files to the .txt file.
        and create the file if it doesn't exist."""
        if not self.register_path.exists():
            self.register_path.touch()

        with open(self.register_path, "w", encoding="utf-8") as file:
            for filename in registered_files:
                file.write(f"{filename}\n")

    def stm_files_list(self) -> list:
        """Get the list of short-term data base files."""
        stm_files = [
            file for file in Path(self.stm_dir).glob(f"*.{self.stm_type}")
        ]
        return stm_files

    def ltm_files_list(self) -> list:
        """Get the list of long-term data base files."""
        ltm_files = [
            file for file in Path(self.ltm_dir).glob(f"*.{self.ltm_type}")
        ]
        return ltm_files

    def stm_unread_files_list(self) -> list:
        """Get the list of unread files."""
        stm_files = self.stm_files_list()
        registered_files = self.read_registered_files()
        unread_files = [
            file for file in stm_files if file.name not in registered_files
        ]
        return unread_files
    
    def ltm_unread_files_list(self) -> list:
        """Get the list of unread files."""
        ltm_files = self.ltm_files_list()
        registered_files = self.read_registered_files()
        unread_files = [
            file for file in ltm_files if file.name not in registered_files
        ]
        return unread_files
    
    

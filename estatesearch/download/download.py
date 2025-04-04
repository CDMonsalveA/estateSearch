"""Data download module for the estate search application."""

import json
import logging
import pathlib
from datetime import datetime
from typing import Any, Optional

logger = logging.getLogger(__name__)


class DownloadManager:
    """
    Download manager for the estate search application.

    This class manages the download process for the estate search application.
    """

    def __init__(
        self,
        search_results: dict,
        filename: str = f"{datetime.now().date}.json",
        filepath: str = "results",
    ) -> None:
        """
        Initialize the download manager.

        Args:
            search_results (dict): The search results to be downloaded.
        """
        logger.info("Initializing DownloadManager...")
        self.search_results = search_results
        self.filename = filename
        self.results_dir = pathlib.Path(filepath)
        self.results_dir.mkdir(parents=True, exist_ok=True)

    def to_json(self) -> None:
        """
        Save the search results to a JSON file.

        Args:
            filename (str): The name of the file to save the results to.
            If not provided, the default filename will be used.
        """
        file_path = self.results_dir / self.filename
        logger.info(f"Saving search results to {file_path}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w") as f:
            json.dump(self.search_results, f, indent=4)
        logger.info(f"Search results saved to {file_path}.")

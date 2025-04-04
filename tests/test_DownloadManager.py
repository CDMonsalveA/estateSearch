import json
import pathlib
import unittest
from unittest.mock import mock_open, patch

from estatesearch.download.download import DownloadManager


class TestDownloadManager(unittest.TestCase):
    def setUp(self):
        self.search_results = {
            "Version": "1.0",
            "SearchResults": {
                "Rightmove": {
                    "properties": [
                        {"id": 1, "name": "Property 1"},
                        {"id": 2, "name": "Property 2"},
                    ]
                }
            },
            "SearchParams": {
                "location": "London",
                "buy_rent": "rent",
                "radius": 0,
            },
            "SearchDate": "2023-10-01T12:00:00",
        }
        self.filename = "test_results.json"
        self.filepath = "results"

    def tearDown(self):
        # Clean up the test file after each test
        test_file = pathlib.Path(self.filepath) / self.filename
        if test_file.exists():
            test_file.unlink()

    def test_init(self):
        # Test initialization of DownloadManager
        download_manager = DownloadManager(
            self.search_results, self.filename, self.filepath
        )
        self.assertEqual(download_manager.search_results, self.search_results)
        self.assertEqual(download_manager.filename, self.filename)
        self.assertEqual(
            download_manager.results_dir, pathlib.Path(self.filepath)
        )
        self.assertTrue(download_manager.results_dir.exists())
        self.assertTrue(download_manager.results_dir.is_dir())

    # @patch("builtins.open", new_callable=mock_open, create=True)
    def test_to_json(self):
        # Test saving search results to JSON file
        download_manager = DownloadManager(
            self.search_results, self.filename, self.filepath
        )
        download_manager.to_json()
        # Check if the file was created

        test_file = pathlib.Path(self.filepath) / self.filename
        self.assertTrue(test_file.exists())
        self.assertTrue(test_file.is_file())
        # Check if the content is correct
        with open(test_file, "r") as f:
            content = json.load(f)
            self.assertEqual(content, self.search_results)
        # Clean up the test file after the test
        test_file.unlink()


if __name__ == "__main__":
    unittest.main()

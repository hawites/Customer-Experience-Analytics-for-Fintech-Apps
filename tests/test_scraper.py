import unittest
import os
import pandas as pd
from src.scraper import GoogleScraper

class TestGoogleScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = GoogleScraper()
        self.bank_name = "TestCBE"
        self.package_name = "com.combanketh.mobilebanking"

    def test_scrapeBankData_creates_csv(self):
        self.scraper.scrapeBankData(self.bank_name, self.package_name)
        file_path = f"data/{self.bank_name}_reviews.csv"
        self.assertTrue(os.path.exists(file_path), "CSV file was not created.")

        # Optionally check the content
        df = pd.read_csv(file_path)
        self.assertIn("app_name", df.columns)
        self.assertIn("content", df.columns)
        self.assertGreater(len(df), 0, "CSV file is empty.")

    def tearDown(self):
        # Clean up the file
        file_path = f"data/{self.bank_name}_reviews.csv"
        if os.path.exists(file_path):
            os.remove(file_path)


import unittest
import os
import pandas as pd
from src.preprocess import PreProcessData

TEST_INPUT_PATH = "tests/sample_data.csv"
TEST_OUTPUT_PATH = "tests/cleaned_sample.csv"

class TestPreprocessor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a small sample CSV
        sample_data = pd.DataFrame({
            'content': ['great app', 'great app',  None],
            'score': [5, 5, 4, None],
            'at': ['2024-05-01', '2024-05-01', '2024-05-01', ''],
            'app_name': ['Bank A'] * 4
        })
        os.makedirs("tests", exist_ok=True)
        sample_data.to_csv(TEST_INPUT_PATH, index=False)

    def test_clean_pipeline(self):
        pre = Preprocessor(TEST_INPUT_PATH)
        pre.load_data()
        pre.clean()

   
        self.assertEqual(len(pre.df), 1)
        self.assertIn('review', pre.df.columns)
        self.assertIn('rating', pre.df.columns)

    def test_save_cleaned(self):
        pre = Preprocessor(TEST_INPUT_PATH)
        pre.load_data()
        pre.clean()
        pre.save_cleaned(TEST_OUTPUT_PATH)

        self.assertTrue(os.path.exists(TEST_OUTPUT_PATH))

    @classmethod
    def tearDownClass(cls):
        # Clean up test files
        if os.path.exists(TEST_INPUT_PATH):
            os.remove(TEST_INPUT_PATH)
        if os.path.exists(TEST_OUTPUT_PATH):
            os.remove(TEST_OUTPUT_PATH)


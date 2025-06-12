import unittest
import pandas as pd
import os
from src.utils.insight_analyzer import InsightAnalyzer

class TestInsightAnalyzer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create test CSV
        cls.test_csv = "test_sentiment.csv"
        data = {
            'review': ["Good service", "Bad app", "Okay experience", "Excellent UI", "Terrible crash"],
            'rating': [5, 1, 3, 5, 1],
            'date': pd.date_range(start='2023-01-01', periods=5),
            'bank': ["CBE", "BOA", "DB", "CBE", "BOA"],
            'bert_sentiment': ["POSITIVE", "NEGATIVE", "NEUTRAL", "POSITIVE", "NEGATIVE"],
            'bert_score': [0.95, 0.2, 0.6, 0.97, 0.1],
            'theme': ["UI", "Crashes", "UX", "UI", "Crashes"]
        }
        df = pd.DataFrame(data)
        df.to_csv(cls.test_csv, index=False)
        cls.analyzer = InsightAnalyzer(cls.test_csv)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_csv):
            os.remove(cls.test_csv)

    def test_theme_distribution_runs(self):
        try:
            self.analyzer.theme_distribution()
        except Exception as e:
            self.fail(f"theme_distribution() raised an exception: {e}")

    def test_theme_ratio_by_bank_runs(self):
        try:
            self.analyzer.theme_ratio_by_bank()
        except Exception as e:
            self.fail(f"theme_ratio_by_bank() raised an exception: {e}")


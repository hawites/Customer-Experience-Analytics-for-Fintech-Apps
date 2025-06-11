import pandas as pd
from src.sentiment import SentimentAnalyzer

def test_sentiment_analysis():
    df = pd.DataFrame({"review": ["Great app!", "Terrible experience."]})
    analyzer = SentimentAnalyzer()
    result_df = analyzer.analyze(df)
    assert "sentiment" in result_df.columns
    assert "sentiment_score" in result_df.columns
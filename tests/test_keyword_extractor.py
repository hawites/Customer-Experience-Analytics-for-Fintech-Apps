import pandas as pd
from src.utils.keyword_extractor import KeywordExtractor

def test_keyword_extraction():
    df = pd.DataFrame({"review": ["Login failed", "Transfer too slow", "App crashes often"]})
    extractor = KeywordExtractor()
    keywords = extractor.extract_keywords(df["review"].tolist())
    assert isinstance(keywords, list)
    assert len(keywords) > 0
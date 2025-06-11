import pandas as pd

class SentimentAggregator:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def aggregate_by_bank_and_rating(self):
        
        if "bert_score" not in self.df.columns or "bank" not in self.df.columns or "rating" not in self.df.columns:
            raise ValueError("Required columns missing from DataFrame")
        
        return (
            self.df.groupby(["bank", "rating"])
            .agg(
                avg_bert_score=("bert_score", "mean"),
                review_count=("bert_score", "count")
            )
            .reset_index()
        )

    def aggregate_sentiment_counts(self):
        
        if "bert_sentiment" not in self.df.columns:
            raise ValueError("Sentiment label column is missing.")
        
        return (
            self.df.groupby(["bank", "bert_sentiment"])
            .size()
            .reset_index(name="count")
        )

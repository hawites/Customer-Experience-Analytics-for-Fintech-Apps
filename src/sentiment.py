import pandas as pd
from src.sentiment_model import SentimentModel
from src.utils.text_utils import apply_sentiment

class SentimentAnalyzer:
    def __init__(self):
        self.bert_model = SentimentModel(model_type="distilbert")
        self.vader_model = SentimentModel(model_type="vader")

    def analyze_single(self, text, method="bert"):
        if method == "vader":
            return self.vader_model.analyze(str(text))
        else:
            return self.bert_model.analyze(str(text))

    def analyze_dataframe(self, df, text_column='review'):
        sentiments = []
        scores = []

        for text in df[text_column]:
            label, score = self.bert_model.analyze(str(text))
            sentiments.append(label)
            scores.append(score)

        df['sentiment'] = sentiments
        df['sentiment_score'] = scores
        return df


import pandas as pd
from transformers import pipeline
from tqdm import tqdm

class SentimentAnalyzer:
    def __init__(self):
        self.model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

    def analyze_sentiment(self, df, text_col='review'):
        sentiments = []
        scores = []

        tqdm.pandas(desc="Running sentiment analysis")
        results = df[text_col].progress_apply(lambda x: self.model(x[:512])[0] if isinstance(x, str) else {'label': 'NEUTRAL', 'score': 0.0})
        
        for r in results:
            label = r['label']
            score = r['score']
            if label == 'POSITIVE':
                sentiments.append('positive')
            elif label == 'NEGATIVE':
                sentiments.append('negative')
            else:
                sentiments.append('neutral')
            scores.append(score)

        df['sentiment'] = sentiments
        df['sentiment_score'] = scores
        return df

from transformers import pipeline
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class SentimentModel:
    def __init__(self, model_type="distilbert"):
        self.model_type = model_type
        if model_type == "distilbert":
            self.model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
        elif model_type == "vader":
            self.model = SentimentIntensityAnalyzer()
        else:
            raise ValueError("Choose 'distilbert' or 'vader'")

    def analyze(self, text):
        if self.model_type == "distilbert":
            result = self.model(text[:512])[0]
            return result['label'], float(result['score'])
        else:
            score = self.model.polarity_scores(text)
            compound = score['compound']
            if compound >= 0.05:
                return "POSITIVE", compound
            elif compound <= -0.05:
                return "NEGATIVE", compound
            else:
                return "NEUTRAL", compound

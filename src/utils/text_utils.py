import pandas as pd

def apply_sentiment(model, df):
    df['sentiment'], df['confidence'] = zip(*df['review_text'].astype(str).map(model.analyze))
    return df
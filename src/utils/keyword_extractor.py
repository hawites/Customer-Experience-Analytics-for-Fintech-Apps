from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import re

class KeywordExtractor:
    def __init__(self, max_features=100, ngram_range=(1, 2)):
        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            max_features=max_features,
            ngram_range=ngram_range,
            token_pattern=r"(?u)\b\w\w+\b"
        )

    def clean_texts(self, texts):
        cleaned = []
        for text in texts:
            # remove digits, emojis, special characters
            text = re.sub(r"[^A-Za-z\s]", "", str(text))
            text = re.sub(r"\s+", " ", text).strip().lower()
            cleaned.append(text)
        return cleaned

    def extract_keywords(self, texts):
        cleaned_texts = self.clean_texts(texts)
        tfidf_matrix = self.vectorizer.fit_transform(cleaned_texts)
        feature_array = np.array(self.vectorizer.get_feature_names_out())
        tfidf_scores = tfidf_matrix.sum(axis=0).A1
        top_indices = tfidf_scores.argsort()[::-1]
        keywords = feature_array[top_indices]
        return keywords.tolist()

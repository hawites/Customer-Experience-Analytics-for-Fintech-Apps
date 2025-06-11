
# 🏦 Customer Experience Analytics for Fintech Apps

## 📌 Project Overview

This project simulates the role of a Data Analyst at Omega Consultancy. It focuses on analyzing customer satisfaction with three major Ethiopian banks' mobile apps:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank (DB)

The goal is to scrape, clean, analyze, and visualize app review data from the Google Play Store.

---

## 📁 Folder Structure

```
Customer-Experience-Analytics-for-Fintech-Apps/
├── data/                          # Raw, cleaned, and labeled review data
│   ├── *_reviews.csv
│   ├── sentiment_themes_labeled.csv
│   └── clean/
│       ├── cleaned_*.csv
│
├── notebooks/                    # Jupyter notebooks 
│   ├── Scraping_Insights.ipynb
│   └── Sentiment_Thematic_Analysis.ipynb
│
├── src/                          # Core logic modules
│   ├── scraper.py                # Task 1 - Scraping logic
│   ├── preprocess.py             # Task 1 - Data cleaning
│   ├── sentiment.py              # Task 2 - Sentiment interface (BERT/VADER)
│   ├── sentiment_model.py        # Task 2 - Actual model implementation
│   ├── __init__.py
│   └── utils/                    # Task 2 - Supporting components
│       ├── keyword_extractor.py     # Extract keywords from review text
│       ├── text_utils.py            # Tokenization, filtering utilities
│       ├── theme_grouper.py         # Rule-based theme classification
│       └── aggregator.py            # Bank-wise sentiment aggregations
│
├── tests/                        # Unit tests for all modules
│   ├── test_keyword_extractor.py
│   ├── test_preprocess.py
│   ├── test_scraper.py
│   ├── test_sentiment.py
│   ├── test_theme_grouper.py
│   └── run_tests.py              # CLI runner for all tests
│
├── requirements.txt              # All package dependencies
└── README.md                     # Project documentation
```

---

## ✅ Task 1: Data Collection & Preprocessing

### 🕷️ Step 1: Scrape Reviews

**Location:** `src/scraper.py`  
Used `google-play-scraper` to scrape 600 reviews per app.

### 🧹 Step 2: Preprocess Data

**Location:** `src/preprocess.py`  
Handles:
- Removing duplicates
- Dropping missing values
- Normalizing date formats
- Filtering non-English reviews
- Renaming and standardizing columns

Example:
```python
from src.preprocess import PreProcessData

pp = PreProcessData("data/cbe_reviews.csv")
pp.load_data()
pp.clean()
pp.save_cleaned("data/clean/cleaned_cbe_reviews.csv")
```

### 🧪 Step 3: Run Tests

Run `python tests/run_tests.py` to test modules.

---

## 📊 Task 2: Sentiment & Thematic Analysis

### 🧠 Sentiment Analysis
**Location:** `src/sentiment.py` + `sentiment_model.py`  
Uses:
- DistilBERT (HuggingFace)
- VADER (for comparison)

### 🧵 Thematic Analysis
**Location:** `src/utils/`  
Components:
- `keyword_extractor.py`: TF-IDF & spaCy extraction
- `theme_grouper.py`: Rule-based grouping into 3–5 business themes
- `aggregator.py`: Summary stats by bank

### 📒 Notebook Execution

Main analysis notebook:
- `notebooks/Sentiment_Thematic_Analysis.ipynb`

---

## 📦 Setup & Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🚀 Outputs

- Sentiment & themes labeled: `data/sentiment_themes_labeled.csv`
- Analysis artifacts in `notebooks/`

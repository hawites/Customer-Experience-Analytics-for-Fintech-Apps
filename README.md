
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
│   ├── Sentiment_Thematic_Analysis.ipynb
│   └── Upload_to_Database.ipynb
│
├── src/                          # Core logic modules
│   ├── scraper.py                # Task 1 - Scraping logic
│   ├── preprocess.py             # Task 1 - Data cleaning
│   ├── sentiment.py              # Task 2 - Sentiment interface (BERT/VADER)
│   ├── sentiment_model.py        # Task 2 - Actual model implementation
│   ├── database.py              # Task 3 - Insert banks/reviews into Oracle
│   ├── __init__.py
│   └── utils/
│       ├── keyword_extractor.py     # TF-IDF / spaCy keyword extraction
│       ├── text_utils.py            # Tokenization, filtering
│       ├── theme_grouper.py         # Rule-based theme classification
│       ├── aggregator.py            # Sentiment aggregations
│       ├── db_config.py             # Task 3 - Loads Oracle DB credentials
│       
│
├── tests/                        # Unit tests for all modules
│   ├── test_keyword_extractor.py
│   ├── test_preprocess.py
│   ├── test_scraper.py
│   ├── test_sentiment.py
│   ├── test_theme_grouper.py
│   ├── test_database.py
│   └── run_tests.py              # CLI runner
│
├── db/                          # SQL dump of populated tables
│   └── bank_reviews.sql
│
├── .env                          # Oracle DB connection (excluded from Git)
├── requirements.txt              # All dependencies
└── README.md                     # Project documentation
```

---

## ✅ Task 1: Data Collection & Preprocessing

### 🕷️ Step 1: Scrape Reviews

**Location:** `src/scraper.py`  
Used `google-play-scraper` to collect reviews per app.

### 🧹 Step 2: Preprocess Data

**Location:** `src/preprocess.py`  
Functions:
- Remove duplicates
- Normalize dates
- Drop missing/non-English rows
- Rename and clean columns

```python
from src.preprocess import PreProcessData

pp = PreProcessData("data/cbe_reviews.csv")
pp.load_data()
pp.clean()
pp.save_cleaned("data/clean/cleaned_cbe_reviews.csv")
```

---

## 📊 Task 2: Sentiment & Thematic Analysis

### 🧠 Sentiment Analysis
**Files:** `src/sentiment.py`, `src/sentiment_model.py`  
Implements:
- DistilBERT from HuggingFace Transformers
- VADER (lexicon-based)

### 📌 Thematic Analysis
**Files:** `src/utils/theme_grouper.py`, `keyword_extractor.py`  
Extracts keywords (TF-IDF/spaCy), and classifies themes:
- Account Access Issues
- Transaction Performance
- UI/UX Feedback
- Customer Support
- Feature Requests

### 📊 Aggregation
Bank-wise and rating-wise aggregation done via `aggregator.py`

### 📒 Notebook
Executed in:  
`notebooks/Sentiment_Thematic_Analysis.ipynb`  
Final result:  
`data/sentiment_themes_labeled.csv`

---

## 🗃️ Task 3: Oracle Database Integration

### 🏛️ Objective:
Simulate enterprise-level data warehousing by storing cleaned and processed review data in an Oracle XE database.

### ⚙️ Oracle Setup
- Used Oracle XE (Express Edition)
- Connected via `cx_Oracle` and credentials stored in `.env`

### 🧱 Schema
Two main tables created:
- `banks (bank_id PK, bank_name)`
- `reviews (review_id PK, review_text, rating, date, sentiment_label, sentiment_score, theme, bank_id FK)`

### 📥 Data Upload
**Files:**
- `src/utils/db_config.py`: Loads DB credentials from `.env`
- `src/database.py`: Class-based uploader

### 💻 Sample Usage:
```python
from src.utils.database import OracleUploader

uploader = OracleUploader()
uploader.connect()
uploader.insert_banks(csv)
uploader.insert_reviews_from_csv(csv)
uploader.close()
```

### 📒 Notebook
Executed in:  
`notebooks/Upload_to_Database.ipynb`

### 📤 SQL Dump
Exported `banks` and `reviews` tables:  
`db/bank_reviews.sql`

---

## 📦 Setup & Installation

```bash
pip install -r requirements.txt
```

You also need:
- Oracle Instant Client
- `.env` file with:
  ```
  ORACLE_USERNAME=your_user
  ORACLE_PASSWORD=your_pass
  ORACLE_HOST=localhost
  ORACLE_PORT=1521
  ORACLE_SID=XE
  ```

---

## ✅ Outputs

- `data/sentiment_themes_labeled.csv`: Sentiment + theme-labeled data
- `db/bank_reviews.sql`: Oracle-ready SQL dump
- Uploaded data into Oracle XE via Python

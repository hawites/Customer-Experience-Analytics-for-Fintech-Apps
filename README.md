# 🏦 Customer Experience Analytics for Fintech Apps

## 📌 Project Overview

This project simulates the role of a Data Analyst at Omega Consultancy. It focuses on analyzing customer satisfaction with three major Ethiopian banks' mobile apps:

* Commercial Bank of Ethiopia (CBE)
* Bank of Abyssinia (BOA)
* Dashen Bank (DB)

The goal is to scrape, clean, analyze, and visualize app review data from the Google Play Store.

---

## 📁 Folder Structure

```
BankReviewAnalysis/
├── data/                   # Raw and cleaned datasets
├── notebooks/              # Jupyter notebooks per task
│   └── Scraping_Insights.ipynb
├── src/                    # Core modules
│   ├── __init__.py
│   ├── scraper.py          # Google Play review scraping
│   ├── preprocess.py       # Cleaning module
├── tests/                  # Unit tests
│   └── test_preprocessor.py
├── README.md               # Project documentation
└── requirements.txt        # Package dependencies
```

---

## ✅ Task 1: Data Collection & Preprocessing

### 🕷️ Step 1: Scrape Reviews

**Location:** `src/scraper.py`

 used `google-play-scraper` to scrape 600 reviews per app.


### 🧹 Step 2: Preprocess Data

**Location:** `src/preprocess.py`

The `PreProcessData` class handles:

* Removing duplicates
* Dropping missing values
* Normalizing date formats
* Filtering out non-English reviews (Amharic/Afaan Oromo)
* Renaming and standardizing columns

Example usage:

```python
from src.preprocess import PreProcessData

pp = PreProcessData("../data/boa_reviews.csv")
pp.load_data()
pp.clean()
pp.save_cleaned("../data/boa_cleaned.csv")
```

### 🧪 Step 3: Test

Test scripts are provided in the `tests/` folder to verify cleaning logic.

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📈 Next Step

Proceed to **Task 2**: Sentiment and Thematic Analysis

> Make sure all cleaned files are stored in `data/` before continuing.

---

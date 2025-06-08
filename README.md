# Task 1: Data Collection and Preprocessing

## Overview

This repository contains the implementation of **Task 1** of the Customer Experience Analytics for Fintech Apps challenge. The objective of this task is to scrape, clean, and preprocess user reviews from the Google Play Store for three major Ethiopian banks:

* Commercial Bank of Ethiopia (CBE)
* Bank of Abyssinia (BOA)
* Dashen Bank (DB)

The final output is a cleaned CSV dataset for each bank containing relevant fields for downstream sentiment and thematic analysis.

---

## Project Structure

```bash
.
├── data/                   # Raw and cleaned datasets
│   ├── cbe_reviews.csv
│   ├── boa_reviews.csv
│   └── db_reviews.csv
├── notebooks/              # Jupyter notebooks for exploration and insights
│   └── BankInsights.ipynb
├── src/                    # Core package source code
│   ├── __init__.py
│   └── preprocess.py       # Preprocessing class
├── tests/                  # Unit tests for preprocessing
│   ├── test_preprocessor.py
│   └── run_tests.py
├── README.md               # Task 1 documentation
└── requirements.txt        # Required Python packages
```

---

## Preprocessing Steps

The `PreProcessData` class performs the following transformations:

1. **Load CSV file with error handling**
2. **Explore data structure**
3. **Remove duplicate reviews**
4. **Drop rows with missing essential fields**
5. **Normalize review dates to YYYY-MM-DD**
6. **Remove reviews with Amharic characters** (non-English filter)
7. **Standardize column names and format**

Final columns in the cleaned output:

* `review`: The review text
* `rating`: Star rating (1–5)
* `date`: Date of review (normalized)
* `bank`: Bank name
* `source`: Source of data (Google Play)

---

## How to Use

### Run Preprocessing

```python
from src.preprocess import Preprocessor

pre = Preprocessor("data/cbe_reviews.csv")
pre.load_data()
pre.clean()
pre.save_cleaned("data/cbe_cleaned.csv")
```

### Run Unit Tests

```bash
python tests/run_tests.py
```

---

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

Required packages include:

* pandas
* numpy
* pytest

---

## Outputs

Cleaned CSVs saved to:

* `data/cbe_cleaned.csv`
* `data/boa_cleaned.csv`
* `data/db_cleaned.csv`

Each file is ready for sentiment and thematic analysis in Task 2.

---

## Next Steps

Proceed to Task 2:

* Sentiment labeling using `distilbert-base-uncased-finetuned-sst-2-english`
* TF-IDF keyword extraction and thematic clustering

---

## Author

Hawi Tesfaye

---

## License

MIT License

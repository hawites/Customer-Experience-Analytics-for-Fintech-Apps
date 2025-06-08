import pandas as pd
import re
import os

class PreProcessData:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None
    def load_data(self):
        try:
            self.df = pd.read_csv(self.filepath)
            print(f"✅ Data loaded successfully with shape: {self.df.shape}")
        except Exception as e:
            print(f"❌ Error loading data: {e}")
    def observe_data(self):
        try:
            print(f"📊 Data loaded with shape: {self.df.shape}\n")

            print("🔍 Data Types:")
            print(self.df.dtypes, "\n")

            print("🔍 Missing Values:")
            print(self.df.isna().sum(), "\n")

            print("🔍 Descriptive Statistics (Numerical):")
            print(self.df.describe(include=[int, float]), "\n")

            print("🔍 Descriptive Statistics (Textual):")
            print(self.df.describe(include=[object]), "\n")

            print("🔍 Unique Values per Column:")
            for col in self.df.columns:
                print(f"- {col}: {self.df[col].nunique()} unique values")
            
            print("\n🔍 Sample Rows:")
            print(self.df.sample(5))
            
        except Exception as e:
            print(f"Observation error: {e}")
    def remove_duplicates(self):
        self.df.drop_duplicates(subset='content', inplace=True)

    def drop_missing(self):
        self.df.dropna(subset=['content', 'score', 'at'], inplace=True)

    def normalize_dates(self):
        self.df['at'] = pd.to_datetime(self.df['at'], errors='coerce')
        self.df.dropna(subset=['at'], inplace=True)
        self.df['at'] = self.df['at'].dt.date

    def remove_amharic_reviews(self):
        # Regex pattern to match Amharic (Ethiopic) Unicode characters
        amharic_pattern = re.compile(r'[\u1200-\u137F]+')

        def is_english_only(text):
            if not isinstance(text, str):
                return False
            return not amharic_pattern.search(text)

        self.df = self.df[self.df['content'].apply(is_english_only)]

    def standardize_columns(self):
        self.df = self.df.rename(columns={
            'content': 'review',
            'score': 'rating',
            'at': 'date',
            'app_name': 'bank'
        })
        self.df['source'] = 'Google Play'
        self.df = self.df[['review', 'rating', 'date', 'bank', 'source']]

    def clean(self):
        try:
            self.remove_duplicates()
            self.drop_missing()
            self.normalize_dates()
            self.remove_amharic_reviews()
            self.standardize_columns()
        except Exception as e:
            print(f"Cleaning error: {e}")

    def save_cleaned(self, output_path):
        try:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            self.df.to_csv(output_path, index=False)
            print(f"✅ Cleaned data saved to: {output_path}")
        except Exception as e:
            print(f"Save error: {e}")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

class InsightAnalyzer:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.df['date'] = pd.to_datetime(self.df['date'])

    def sentiment_distribution(self):
        plt.figure(figsize=(10, 6))
        sns.countplot(data=self.df, x='bank', hue='bert_sentiment', palette='Set2')
        plt.title('Sentiment Distribution by Bank')
        plt.xlabel('Bank')
        plt.ylabel('Count')
        plt.legend(title='Sentiment')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def sentiment_score_by_rating(self):
        plt.figure(figsize=(10, 6))
        sns.barplot(data=self.df, x='rating', y='bert_score', hue='bank')
        plt.title('Average Sentiment Score by Rating')
        plt.xlabel('Rating')
        plt.ylabel('BERT Sentiment Score')
        plt.tight_layout()
        plt.show()

    def wordcloud_per_bank(self):
        for bank in self.df['bank'].unique():
            text = " ".join(self.df[self.df['bank'] == bank]['review'].astype(str))
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis("off")
            plt.title(f"WordCloud for {bank}")
            plt.tight_layout(pad=0)
            plt.show()

    def theme_distribution(self):
        plt.figure(figsize=(12, 6))
        theme_order = self.df['theme'].value_counts().index  # Ensures descending order
        sns.countplot(data=self.df, x='theme', hue='bank', palette='pastel', order=theme_order)
        plt.title('Theme Frequency by Bank')
        plt.xlabel('Theme')
        plt.ylabel('Count')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    def theme_ratio_by_bank(self):
        # Count total themes per bank
        theme_counts = self.df.groupby(['bank', 'theme']).size().reset_index(name='count')
        
        # Total reviews per bank for normalization
        total_counts = self.df.groupby('bank').size().reset_index(name='total')

        # Merge total counts into theme counts
        merged = theme_counts.merge(total_counts, on='bank')

        # Calculate percentage
        merged['percentage'] = (merged['count'] / merged['total']) * 100

        # Plot
        plt.figure(figsize=(14, 6))
        sns.barplot(data=merged, x='theme', y='percentage', hue='bank')
        plt.title('Theme Distribution as Percentage per Bank')
        plt.ylabel('Percentage (%)')
        plt.xlabel('Theme')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

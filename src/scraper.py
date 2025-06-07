from google_play_scraper import app, Sort, reviews
import pandas as pd
from urllib.error import URLError
import time


class GoogleScraper:
    def __init__(self):
        pass
    def scrapeBankData (self, bankname, packagename):
        try:
            app_info = app(packagename,lang='en', country='ET')
            
            # Get reviews
            review_list, _ = reviews(
                packagename,  
                country='ET',
                count=800  
            )

            # Organize reviews into DataFrame
            df = pd.DataFrame(review_list)

            # Add app name ( for labeling)
            df['app_name'] = app_info['title']
            # Save to CSV
            df.to_csv(f'../data/{bankname}_reviews.csv', index=False, encoding='utf-8')

            print(f"{bankname} reviews saved to CSV.")
        except URLError as e:
            print(f"Network error: {e.reason} — check your internet or try again later.")
        except Exception as e:
            print(f"Something went wrong: {e}")

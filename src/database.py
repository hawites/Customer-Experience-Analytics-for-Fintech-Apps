import cx_Oracle
import pandas as pd
from src.utils.db_config import OracleDBConfig

class OracleUploader:
    def __init__(self):
        self.config = OracleDBConfig()
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            username, password, dsn = self.config.get_credentials()
            self.conn = cx_Oracle.connect(username, password, dsn)
            self.cur = self.conn.cursor()
            print("✅ Successfully connected to Oracle DB.")
        except Exception as e:
            print("❌ Connection failed:", e)
            raise

    def insert_banks_from_csv(self, filepath):
        df = pd.read_csv(filepath)
        bank_names = df["bank"].unique()

        for name in bank_names:
            self.cur.execute("SELECT COUNT(*) FROM banks WHERE bank_name = :name", {'name': name})
            exists = self.cur.fetchone()[0]
            if not exists:
                self.cur.execute("INSERT INTO banks (bank_name) VALUES (:name)", {'name': name})

        self.conn.commit()
        print("✅ Banks inserted/verified from CSV.")

    def insert_reviews_from_csv(self, filepath):
        df = pd.read_csv(filepath)
        df['date'] = pd.to_datetime(df['date']).dt.date

        self.cur.execute("SELECT bank_id, bank_name FROM banks")
        bank_map = {name: id for id, name in self.cur.fetchall()}

        for _, row in df.iterrows():
            self.cur.execute("""
                INSERT INTO reviews (
                    review_text, rating, review_date, sentiment_label,
                    sentiment_score, theme, bank_id
                ) VALUES (
                    :1, :2, :3, :4, :5, :6, :7
                )
            """, (
                row["review"],
                int(row["rating"]),
                row["date"],
                row["bert_sentiment"],
                float(row["bert_score"]),
                row["theme"],
                bank_map[row["bank"]]
            ))

        self.conn.commit()
        print("📥 Reviews successfully inserted.")

    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
            print("🔒 Oracle connection closed.")

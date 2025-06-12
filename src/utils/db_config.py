import os
from dotenv import load_dotenv
import cx_Oracle

load_dotenv()

class OracleDBConfig:
    def __init__(self):
        self.username = os.getenv("ORACLE_USERNAME")
        self.password = os.getenv("ORACLE_PASSWORD")
        self.host = os.getenv("ORACLE_HOST", "localhost")
        self.port = os.getenv("ORACLE_PORT", "1521")
        self.sid = os.getenv("ORACLE_SID", "XE")

    def get_credentials(self):
        dsn = cx_Oracle.makedsn(self.host, self.port, sid=self.sid)
        return self.username, self.password, dsn

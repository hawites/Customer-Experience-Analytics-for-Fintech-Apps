import unittest
from unittest.mock import MagicMock, patch
from src.database import OracleUploader

class TestOracleUploader(unittest.TestCase):
    @patch("src.database.OracleDBConfig")
    @patch("cx_Oracle.connect")
    def test_connect_success(self, mock_connect, mock_config):
        mock_config_instance = mock_config.return_value
        mock_config_instance.get_credentials.return_value = ("user", "pass", "dsn")

        uploader = OracleUploader()
        uploader.connect()

        mock_connect.assert_called_with("user", "pass", "dsn")
        self.assertIsNotNone(uploader.conn)
        self.assertIsNotNone(uploader.cur)

    def test_insert_banks(self):
        uploader = OracleUploader()
        uploader.cur = MagicMock()
        uploader.conn = MagicMock()

        uploader.cur.fetchone.return_value = [0]  # Simulate bank does not exist

        uploader.insert_banks(["Test Bank"])
        uploader.cur.execute.assert_any_call("SELECT COUNT(*) FROM banks WHERE bank_name = :name", {'name': 'Test Bank'})
        uploader.cur.execute.assert_any_call("INSERT INTO banks (bank_name) VALUES (:name)", {'name': 'Test Bank'})
        uploader.conn.commit.assert_called_once()


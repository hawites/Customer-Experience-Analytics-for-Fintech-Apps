import unittest
import os
from src.utils.db_config import OracleDBConfig

class TestOracleDBConfig(unittest.TestCase):
    def setUp(self):
        os.environ["ORACLE_USERNAME"] = "test_user"
        os.environ["ORACLE_PASSWORD"] = "test_pass"
        os.environ["ORACLE_HOST"] = "localhost"
        os.environ["ORACLE_PORT"] = "1521"
        os.environ["ORACLE_SID"] = "XE"

    def test_get_credentials(self):
        config = OracleDBConfig()
        username, password, dsn = config.get_credentials()

        self.assertEqual(username, "test_user")
        self.assertEqual(password, "test_pass")
        self.assertIn("localhost", dsn)
        self.assertIn("1521", dsn)
        self.assertIn("XE", dsn)



import psycopg2
import unittest

class TestDatabaseConnection(unittest.TestCase):
    def test_connection(self):
        try:
            connection = psycopg2.connect(
                "postgresql://neondb_owner:npg_MNlxuciR51ZS@ep-round-star-a8saecy2.eastus2.azure.neon.tech/demo?sslmode=require"
            )
            self.assertIsNotNone(connection)
            connection.close()
        except Exception as e:
            self.fail(f"Database connection failed: {e}")

if __name__ == '__main__':
    unittest.main()

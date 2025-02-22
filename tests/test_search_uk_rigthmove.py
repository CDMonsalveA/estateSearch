import unittest

from estatesearch import Rightmove


class TestRightmove(unittest.TestCase):
    """
    Test the Rightmove class
    """

    def test_connect(self):
        """
        Test the connect method
        """
        rightmove = Rightmove()
        status_code = rightmove.check_basic_request_connection()
        self.assertEqual(status_code, 200)


if __name__ == "__main__":
    unittest.main()

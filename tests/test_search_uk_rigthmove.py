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
        self.assertTrue(rightmove.connect())


if __name__ == "__main__":
    unittest.main(verbosity=2)

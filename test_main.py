import unittest
from main import phi, p_numbers, public_key


class MyTestCase(unittest.TestCase):
    def test_phi_function(self):
        # Test case for phi() function
        self.assertEqual(phi(1), 1)  # phi(1) should return 1
        self.assertEqual(phi(10), 4)  # phi(10) should return 4
        self.assertEqual(phi(13), 12)  # phi(13) should return 12


if __name__ == '__main__':
    unittest.main()

import unittest
from main import phi, p_numbers, public_key


class MyTestCase(unittest.TestCase):
    def test_phi_function(self):
        # Test case for phi() function
        self.assertEqual(phi(1), 1)  # phi(1) should return 1
        self.assertEqual(phi(10), 4)  # phi(10) should return 4
        self.assertEqual(phi(13), 12)  # phi(13) should return 12

    def test_p_numbers_function(self):
        # Test case for p_numbers() function
        n, prime_list_1_10 = p_numbers(1, 10)
        self.assertEqual(len(prime_list_1_10), 4)  # There are 4 prime numbers in the range [1, 10]

        n, prime_list_20_30 = p_numbers(20, 30)
        self.assertEqual(len(prime_list_20_30), 2)  # There are 2 prime numbers in the range [20, 30]

        n, prime_list_50_60 = p_numbers(50, 60)
        self.assertEqual(len(prime_list_50_60), 2)  # There are 2 prime numbers in the range [50, 60]
    def test_public_key_function(self):
        # Test case for public_key() function
        n = 91  # Assuming n is 91
        m = 5  # Assuming message m is 5
        e, n, c = public_key(n, m)
        self.assertIsInstance(e, int)  # e should be an integer
        self.assertGreater(e, 1)  # e should be greater than 1
        self.assertGreater(n, 1)  # n should be greater than 1


if __name__ == '__main__':
    unittest.main()

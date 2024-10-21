from django.test import TestCase

from loans.helpers import is_prime

class IsPrimeTestCase(TestCase):
    def test_1_is_not_prime(self):
        actual_result = is_prime(1)
        self.assertFalse(actual_result)

    def test_2_is_prime(self):
        actual_result = is_prime(2)
        self.assertTrue(actual_result)

    def test_3_is_prime(self):
        actual_result = is_prime(3)
        self.assertTrue(actual_result)
    
    def test_4_is_not_prime(self):
        actual_result = is_prime(4)
        self.assertFalse(actual_result)

    def test_5_is_prime(self):
        actual_result = is_prime(5)
        self.assertTrue(actual_result)

    def test_2017_is_prime(self):
        actual_result = is_prime(2017)
        self.assertTrue(actual_result)

    def test_2117_is_not_prime(self):
        actual_result = is_prime(2117)
        self.assertFalse(actual_result)

    #Exceptions and errors
    def test_is_prime_negative_integer(self):
        with self.assertRaises(ValueError):
            is_prime(-5)

    def test_is_prime_zero(self):
        with self.assertRaises(ValueError):
            is_prime(0)

    def test_is_prime_non_integer(self):
        with self.assertRaises(ValueError):
            is_prime(4.5)

    def test_is_prime_string(self):
        with self.assertRaises(ValueError):
            is_prime("ten")

    def test_is_prime_none(self):
        with self.assertRaises(ValueError):
            is_prime(None)
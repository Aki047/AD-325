import unittest
import numpy as np
from Financial_Growth_Trends import financialGrowthTrends

class TestFinancialGrowthTrends(unittest.TestCase):
    
    # Test 1: Empty input
    def test_empty_input(self):
        with self.assertRaises(ValueError) as context:
            financialGrowthTrends([])
        self.assertTrue("The input array is empty. Please provide a non-empty array." in str(context.exception))
    
    # Test 2: Non-numeric values
    def test_non_numeric_values(self):
        with self.assertRaises(ValueError) as context:
            financialGrowthTrends(['a', 'b', 'c'])
        self.assertTrue("The input array should contain only numeric values (int or float)." in str(context.exception))
    
    # Test 3: Single value
    def test_single_value(self):
        result = financialGrowthTrends([2])
        expected = np.array([4])
        np.testing.assert_array_equal(result, expected)
    
    # Test 4: All positive values
    def test_all_positive_values(self):
        result = financialGrowthTrends([1, 2, 3])
        expected = np.array([1, 4, 9])
        np.testing.assert_array_equal(result, expected)
    
    # Test 5: All negative values
    def test_all_negative_values(self):
        result = financialGrowthTrends([-1, -2, -3])
        expected = np.array([1, 4, 9])
        np.testing.assert_array_equal(result, expected)
    
    # Test 6: Mixed positive and negative values
    def test_mixed_values(self):
        result = financialGrowthTrends([-2, -1, 0, 1, 2])
        expected = np.array([0, 1, 1, 4, 4])
        np.testing.assert_array_equal(result, expected)
    
    # Test 7: Contains zero
    def test_contains_zero(self):
        result = financialGrowthTrends([0, 1, 2])
        expected = np.array([0, 1, 4])
        np.testing.assert_array_equal(result, expected)
    
    # Test 8: Duplicates in input
    def test_duplicates_in_input(self):
        result = financialGrowthTrends([2, 2, -2, -2])
        expected = np.array([4, 4, 4, 4])
        np.testing.assert_array_equal(result, expected)
    
    # Test 9: Large values
    def test_large_values(self):
        result = financialGrowthTrends([1000, -1000])
        expected = np.array([1000000, 1000000])
        np.testing.assert_array_equal(result, expected)
    
    # Test 10: Float values
    def test_float_values(self):
        result = financialGrowthTrends([1.5, -1.5, 2.5])
        expected = np.array([2.25, 2.25, 6.25])
        np.testing.assert_array_equal(result, expected)

if __name__ == '__main__':
    unittest.main()

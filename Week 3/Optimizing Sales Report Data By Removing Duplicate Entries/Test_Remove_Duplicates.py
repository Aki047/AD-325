import unittest

from Removing_Duplicates import removeDuplicatesFromSalesData
class TestRemoveDuplicatesFromSalesData(unittest.TestCase):

    def test_case_1(self):
        # Test case 1
        salesData = [200, 200, 300]
        expected_count = 2
        expected_data = [200, 300]
        self.assertEqual(removeDuplicatesFromSalesData(salesData), expected_count)
        self.assertEqual(salesData[:expected_count], expected_data)

    def test_case_2(self):
        # Test case 2
        salesData = [150, 150, 200, 200, 200, 250, 250, 300, 300, 350]
        expected_count = 5
        expected_data = [150, 200, 250, 300, 350]
        self.assertEqual(removeDuplicatesFromSalesData(salesData), expected_count)
        self.assertEqual(salesData[:expected_count], expected_data)

    def test_case_3(self):
        # Test case 3: No duplicates
        salesData = [100, 200, 300, 400, 500]
        expected_count = 5
        expected_data = [100, 200, 300, 400, 500]
        self.assertEqual(removeDuplicatesFromSalesData(salesData), expected_count)
        self.assertEqual(salesData[:expected_count], expected_data)

    def test_case_4(self):
        # Test case 4: All elements are duplicates
        salesData = [400, 400, 400, 400]
        expected_count = 1
        expected_data = [400]
        self.assertEqual(removeDuplicatesFromSalesData(salesData), expected_count)
        self.assertEqual(salesData[:expected_count], expected_data)

    def test_case_5(self):
        # Test case 5: Empty list
        salesData = []
        expected_count = 0
        expected_data = []
        self.assertEqual(removeDuplicatesFromSalesData(salesData), expected_count)
        self.assertEqual(salesData, expected_data)

    def test_case_6(self):
        # Test case 6: Single element
        salesData = [500]
        expected_count = 1
        expected_data = [500]
        self.assertEqual(removeDuplicatesFromSalesData(salesData), expected_count)
        self.assertEqual(salesData, expected_data)

    def test_case_7(self):
        # Test case 7: Large list with duplicates
        salesData = [1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5]
        expected_count = 5
        expected_data = [1, 2, 3, 4, 5]
        self.assertEqual(removeDuplicatesFromSalesData(salesData), expected_count)
        self.assertEqual(salesData[:expected_count], expected_data)

    def test_case_8(self):
        # Test case 8: Alternating duplicates
        salesData = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        expected_count = 5
        expected_data = [1, 2, 3, 4, 5]
        self.assertEqual(removeDuplicatesFromSalesData(salesData), expected_count)
        self.assertEqual(salesData[:expected_count], expected_data)

    def test_case_9(self):
        # Test case 9: Increasing sequence with a few duplicates
        salesData = [10, 20, 20, 30, 40, 40, 50]
        expected_count = 5
        expected_data = [10, 20, 30, 40, 50]
        self.assertEqual(removeDuplicatesFromSalesData(salesData), expected_count)
        self.assertEqual(salesData[:expected_count], expected_data)

    def test_case_10(self):
        # Test case 10: All identical elements
        salesData = [999, 999, 999, 999, 999]
        expected_count = 1
        expected_data = [999]
        self.assertEqual(removeDuplicatesFromSalesData(salesData), expected_count)
        self.assertEqual(salesData[:expected_count], expected_data)


if __name__ == "__main__":
    unittest.main()

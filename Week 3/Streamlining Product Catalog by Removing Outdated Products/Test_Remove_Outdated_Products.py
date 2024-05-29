import unittest
from Remove_Outdated_Products import Discontinued_Products


class TestDiscontinuedProducts(unittest.TestCase):

    # Test 1: Basic functionality test
    def test_case_1(self):
        catalog = [1003, 1002, 1002, 1003]
        result = Discontinued_Products(catalog, 1003)
        self.assertEqual(result, 2)
        self.assertEqual(catalog, [1002, 1002, None, None])

    # Test 2: No discontinuedID present
    def test_case_2(self):
        catalog = [1001, 1002, 1004]
        result = Discontinued_Products(catalog, 1003)
        self.assertEqual(result, 3)
        self.assertEqual(catalog, [1001, 1002, 1004])

    # Test 3: All elements are discontinuedID
    def test_case_3(self):
        catalog = [1003, 1003, 1003]
        result = Discontinued_Products(catalog, 1003)
        self.assertEqual(result, 0)
        self.assertEqual(catalog, [None, None, None])

    # Test 4: Empty catalog
    def test_case_4(self):
        catalog = []
        result = Discontinued_Products(catalog, 1003)
        self.assertEqual(result, 0)
        self.assertEqual(catalog, [])

    # Test 5: DiscontinuedID at the start
    def test_case_5(self):
        catalog = [1003, 1001, 1002, 1004]
        result = Discontinued_Products(catalog, 1003)
        self.assertEqual(result, 3)
        self.assertEqual(catalog, [1001, 1002, 1004, None])

    # Test 6: DiscontinuedID at the end
    def test_case_6(self):
        catalog = [1001, 1002, 1004, 1003]
        result = Discontinued_Products(catalog, 1003)
        self.assertEqual(result, 3)
        self.assertEqual(catalog, [1001, 1002, 1004, None])

    # Test 7: Alternating discontinuedID
    def test_case_7(self):
        catalog = [1003, 1001, 1003, 1002, 1003, 1004]
        result = Discontinued_Products(catalog, 1003)
        self.assertEqual(result, 3)
        self.assertEqual(catalog, [1001, 1002, 1004, None, None, None])

    # Test 8: Large catalog with no discontinuedID
    def test_case_8(self):
        catalog = list(range(1000, 2000))
        result = Discontinued_Products(catalog, 2000)
        self.assertEqual(result, 1000)
        self.assertEqual(catalog, list(range(1000, 2000)))

    # Test 9: Large catalog with discontinuedID
    # Test 9: Large catalog with discontinuedID
    def test_case_9(self):
        catalog = [1003]
        result = Discontinued_Products(catalog, 1003)
        self.assertEqual(result, 0)
        self.assertEqual(catalog, [None])

    # Test 10: Non-integer discontinuedID
    def test_case_10(self):
        catalog = [1001, 1002, 1004]
        result = Discontinued_Products(catalog, '1003')
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()

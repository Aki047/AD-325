import unittest
from Health_Record_Symmetry_Analysis import ListNode, isHealthRecordSymmetric

class TestSymmetryAnalysis(unittest.TestCase):

    def create_linked_list(self, values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    # Test 1: Even symmetric list (heart rates: 70, 80, 80, 70)
    def test_even_symmetric(self):
        head = self.create_linked_list([70, 80, 80, 70])
        self.assertTrue(isHealthRecordSymmetric(head))

    # Test 2: Odd symmetric list (blood sugar levels: 90, 100, 110, 100, 90)
    def test_odd_symmetric(self):
        head = self.create_linked_list([90, 100, 110, 100, 90])
        self.assertTrue(isHealthRecordSymmetric(head))

    # Test 3: Not symmetric list (blood pressure readings: 120, 130, 125)
    def test_not_symmetric(self):
        head = self.create_linked_list([120, 130, 125])
        self.assertFalse(isHealthRecordSymmetric(head))

    # Test 4: Single element list
    def test_single_element(self):
        head = self.create_linked_list([50])
        self.assertTrue(isHealthRecordSymmetric(head))

    # Test 5: Empty list
    def test_empty_list(self):
        head = self.create_linked_list([])
        self.assertTrue(isHealthRecordSymmetric(head))

    # Test 6: Two elements symmetric
    def test_two_elements_symmetric(self):
        head = self.create_linked_list([10, 10])
        self.assertTrue(isHealthRecordSymmetric(head))

    # Test 7: Two elements not symmetric
    def test_two_elements_not_symmetric(self):
        head = self.create_linked_list([10, 20])
        self.assertFalse(isHealthRecordSymmetric(head))

    # Test 8: Long symmetric list
    def test_long_symmetric(self):
        head = self.create_linked_list([1, 2, 3, 4, 3, 2, 1])
        self.assertTrue(isHealthRecordSymmetric(head))

    # Test 9: Long not symmetric list
    def test_long_not_symmetric(self):
        head = self.create_linked_list([1, 2, 3, 4, 5, 2, 1])
        self.assertFalse(isHealthRecordSymmetric(head))

    # Test 10: Palindrome with negative values
    def test_palindrome_with_negatives(self):
        head = self.create_linked_list([-1, -2, -1])
        self.assertTrue(isHealthRecordSymmetric(head))

    # Test 11: Non-palindrome with negative values
    def test_non_palindrome_with_negatives(self):
        head = self.create_linked_list([-1, -2, -3])
        self.assertFalse(isHealthRecordSymmetric(head))

    # Test 12: Even number of elements, symmetric with different values
    def test_even_symmetric_different_values(self):
        head = self.create_linked_list([1, 2, 2, 1])
        self.assertTrue(isHealthRecordSymmetric(head))

    # Test 13: Odd number of elements, symmetric with different values
    def test_odd_symmetric_different_values(self):
        head = self.create_linked_list([1, 3, 1])
        self.assertTrue(isHealthRecordSymmetric(head))

    # Test 14: Long not symmetric list with varying values
    def test_long_not_symmetric_varying_values(self):
        head = self.create_linked_list([1, 3, 5, 7, 9])
        self.assertFalse(isHealthRecordSymmetric(head))

    # Test 15: Symmetric list with zeroes
    def test_symmetric_with_zeroes(self):
        head = self.create_linked_list([0, 1, 0])
        self.assertTrue(isHealthRecordSymmetric(head))

    # Test 16: Non-symmetric list with zeroes
    def test_non_symmetric_with_zeroes(self):
        head = self.create_linked_list([0, 1, 2])
        self.assertFalse(isHealthRecordSymmetric(head))

    # Test 17: Long symmetric list with mixed values
    def test_long_symmetric_mixed_values(self):
        head = self.create_linked_list([3, 5, 7, 7, 5, 3])
        self.assertTrue(isHealthRecordSymmetric(head))

    # Test 18: Symmetric list with repeated values
    def test_symmetric_repeated_values(self):
        head = self.create_linked_list([4, 4, 4, 4])
        self.assertTrue(isHealthRecordSymmetric(head))

    # Test 19: Non-symmetric list with repeated values
    def test_non_symmetric_repeated_values(self):
        head = self.create_linked_list([4, 4, 4, 5])
        self.assertFalse(isHealthRecordSymmetric(head))

    # Test 20: Large symmetric list
    def test_large_symmetric_list(self):
        head = self.create_linked_list(list(range(1000)) + list(range(1000)[::-1]))
        self.assertTrue(isHealthRecordSymmetric(head))

    # Test 21: Invalid input (not a ListNode or None)
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            isHealthRecordSymmetric("invalid input")

if __name__ == '__main__':
    unittest.main()

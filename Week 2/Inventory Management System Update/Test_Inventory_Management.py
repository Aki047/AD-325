import unittest
from Inventory_Management_System_Update import duplicateZeros

class TestDuplicateZeros(unittest.TestCase):

    # Test 1: Basic functionality with multiple zeros
    def test_duplicate_zeros(self):
        inventory = [4, 0, 1, 3, 0, 2, 5, 0]
        modified_inventory, original_inventory = duplicateZeros(inventory)
        self.assertEqual(modified_inventory, [4, 0, 0, 1, 3, 0, 0, 2, 5, 0, 0])
        self.assertEqual(original_inventory, inventory)
        # Expected outcome: [4, 0, 0, 1, 3, 0, 0, 2, 5, 0, 0]

    # Test 2: No zeros in the array
    def test_no_zeros(self):
        inventory = [1, 2, 3, 4, 5]
        modified_inventory, original_inventory = duplicateZeros(inventory)
        self.assertEqual(modified_inventory, inventory)
        self.assertEqual(original_inventory, inventory)
        # Expected outcome: [1, 2, 3, 4, 5]

    # Test 3: All elements are zeros
    def test_all_zeros(self):
        inventory = [0, 0, 0, 0]
        modified_inventory, original_inventory = duplicateZeros(inventory)
        self.assertEqual(modified_inventory, [0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(original_inventory, inventory)
        # Expected outcome: [0, 0, 0, 0, 0, 0, 0, 0]

    # Test 4: Single zero in the array
    def test_single_zero(self):
        inventory = [1, 0, 2, 3]
        modified_inventory, original_inventory = duplicateZeros(inventory)
        self.assertEqual(modified_inventory, [1, 0, 0, 2, 3])
        self.assertEqual(original_inventory, inventory)
        # Expected outcome: [1, 0, 0, 2, 3]

    # Test 5: Zero at the end of the array
    def test_zero_at_end(self):
        inventory = [1, 2, 3, 0]
        modified_inventory, original_inventory = duplicateZeros(inventory)
        self.assertEqual(modified_inventory, [1, 2, 3, 0, 0])
        self.assertEqual(original_inventory, inventory)
        # Expected outcome: [1, 2, 3, 0, 0]

    # Test 6: Empty array
    def test_empty_array(self):
        inventory = []
        modified_inventory, original_inventory = duplicateZeros(inventory)
        self.assertEqual(modified_inventory, [])
        self.assertEqual(original_inventory, inventory)
        # Expected outcome: []

    # Test 7: No duplication needed (no zeros)
    def test_no_duplicate_needed(self):
        inventory = [1, 2, 3, 4]
        modified_inventory, original_inventory = duplicateZeros(inventory)
        self.assertEqual(modified_inventory, inventory)
        self.assertEqual(original_inventory, inventory)
        # Expected outcome: [1, 2, 3, 4]

    # Test 8: Zeros with consecutive non-zeros
    def test_zeros_with_consecutive_non_zeros(self):
        inventory = [1, 0, 2, 0, 3]
        modified_inventory, original_inventory = duplicateZeros(inventory)
        self.assertEqual(modified_inventory, [1, 0, 0, 2, 0, 0, 3])
        self.assertEqual(original_inventory, inventory)
        # Expected outcome: [1, 0, 0, 2, 0, 0, 3]

    # Test 9: Zeros with initial non-zero elements
    def test_zeros_with_initial_non_zero(self):
        inventory = [1, 0, 0, 0, 1]
        modified_inventory, original_inventory = duplicateZeros(inventory)
        self.assertEqual(modified_inventory, [1, 0, 0, 0, 0, 0, 0, 1])
        self.assertEqual(original_inventory, inventory)
        # Expected outcome: [1, 0, 0, 0, 0, 0, 0, 1]


if __name__ == '__main__':
    unittest.main()

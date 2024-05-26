import unittest

from LegCount import howManyLegs

class TestHowManyLegs(unittest.TestCase):

    def setUp(self):
        self.four_Legs = ['lion', 'deer', 'elephant', 'horse', 'dog', 'cat']
        self.two_Legs = ['monkey', 'parrot', 'ostrich']
        self.zero_Legs = ['snake', 'worm']
        self.multiple_Legs = ['spider', 'ant', 'centipede']

    # Test 1: Regular case with a mix of animals
    def test_regular_case(self):
        animals = ['lion', 'monkey', 'snake', 'deer', 'elephant']
        self.assertEqual(howManyLegs(animals, self.four_Legs), 3)

    # Test 2: No four-legged animals
    def test_no_four_legged_animals(self):
        animals = ['monkey', 'parrot', 'snake']
        self.assertEqual(howManyLegs(animals, self.four_Legs), 0)

    # Test 3: All four-legged animals
    def test_all_four_legged_animals(self):
        animals = ['lion', 'deer', 'elephant']
        self.assertEqual(howManyLegs(animals, self.four_Legs), 3)

    # Test 4: No animals
    def test_no_animals(self):
        with self.assertRaises(ValueError):
            howManyLegs([], self.four_Legs)

    # Test 5: Only non-four-legged animals
    def test_only_non_four_legged_animals(self):
        animals = ['snake', 'worm', 'ant']
        self.assertEqual(howManyLegs(animals, self.four_Legs), 0)

    # Test 6: Four-legged animals not in list
    def test_four_legged_not_in_list(self):
        animals = ['cow', 'sheep']
        self.assertEqual(howManyLegs(animals, self.four_Legs), 0)

    # Test 7: Mixed animals with duplicates
    def test_mixed_with_duplicates(self):
        animals = ['lion', 'deer', 'deer', 'elephant', 'cat', 'cat']
        self.assertEqual(howManyLegs(animals, self.four_Legs), 5)

    # Test 8: Case sensitivity check
    def test_case_sensitivity(self):
        animals = ['Lion', 'Deer', 'ELEPHANT']
        self.assertEqual(howManyLegs(animals, self.four_Legs), 0)

    # Test 9: Large input size
    def test_large_input(self):
        animals = ['lion'] * 1000 + ['monkey'] * 1000
        self.assertEqual(howManyLegs(animals, self.four_Legs), 1000)

    # Test 10: Empty strings in list
    def test_empty_strings_in_list(self):
        animals = ['lion', '', 'deer']
        self.assertEqual(howManyLegs(animals, self.four_Legs), 2)

if __name__ == '__main__':
    unittest.main()

import unittest
from Financial_Binary_Tree import TreeNode, maxDepth

class TestBinaryTree(unittest.TestCase):
    # Test 1: Tests an empty tree
    def test_empty_tree(self):
        self.assertEqual(maxDepth(None), 0)

    # Test 2: Tests a single node tree
    def test_single_node(self):
        tree = TreeNode("Is it a single node?")
        self.assertEqual(maxDepth(tree), 1)

    # Test 3: Tests a tree with two levels
    def test_two_levels(self):
        tree = TreeNode("Root", TreeNode("Left"), TreeNode("Right"))
        self.assertEqual(maxDepth(tree), 2)

    # Test 4: Tests a left heavy tree
    def test_left_heavy(self):
        tree = TreeNode("Root", TreeNode("Left", TreeNode("Left.Left")))
        self.assertEqual(maxDepth(tree), 3)

    # Test 5: Tests a right heavy tree
    def test_right_heavy(self):
        tree = TreeNode("Root", None, TreeNode("Right", None, TreeNode("Right.Right")))
        self.assertEqual(maxDepth(tree), 3)

    # Test 6: Tests a balanced tree
    def test_balanced_tree(self):
        tree = TreeNode("Root", TreeNode("Left", TreeNode("Left.Left"), TreeNode("Left.Right")),
                        TreeNode("Right", TreeNode("Right.Left"), TreeNode("Right.Right")))
        self.assertEqual(maxDepth(tree), 3)

    # Test 7: Tests an unbalanced tree
    def test_unbalanced_tree(self):
        tree = TreeNode("Root", TreeNode("Left", TreeNode("Left.Left", TreeNode("Left.Left.Left"))),
                        TreeNode("Right"))
        self.assertEqual(maxDepth(tree), 4)

    # Test 8: Tests a complex tree 1
    def test_complex_tree_1(self):
        tree = TreeNode("Root",
                        TreeNode("Left",
                                 TreeNode("Left.Left"),
                                 TreeNode("Left.Right", TreeNode("Left.Right.Left"))),
                        TreeNode("Right", None,
                                 TreeNode("Right.Right", TreeNode("Right.Right.Left"), TreeNode("Right.Right.Right"))))
        self.assertEqual(maxDepth(tree), 4)

    # Test 9: Tests a complex tree 2
    def test_complex_tree_2(self):
        tree = TreeNode("Root",
                        TreeNode("Left",
                                 TreeNode("Left.Left", TreeNode("Left.Left.Left", TreeNode("Left.Left.Left.Left")))),
                        TreeNode("Right"))
        self.assertEqual(maxDepth(tree), 5)

    # Test 10: Tests a skewed left tree
    def test_skewed_left(self):
        tree = TreeNode("Root",
                        TreeNode("Left",
                                 TreeNode("Left.Left",
                                          TreeNode("Left.Left.Left",
                                                   TreeNode("Left.Left.Left.Left")))))
        self.assertEqual(maxDepth(tree), 5)

    # Test 11: Tests a skewed right tree
    def test_skewed_right(self):
        tree = TreeNode("Root",
                        None,
                        TreeNode("Right",
                                 None,
                                 TreeNode("Right.Right",
                                          None,
                                          TreeNode("Right.Right.Right",
                                                   None,
                                                   TreeNode("Right.Right.Right.Right")))))
        self.assertEqual(maxDepth(tree), 5)

    # Test 12: Tests a complex tree 3
    def test_complex_tree_3(self):
        tree = TreeNode("Root",
                        TreeNode("Left",
                                 TreeNode("Left.Left",
                                          TreeNode("Left.Left.Left",
                                                   TreeNode("Left.Left.Left.Left"),
                                                   TreeNode("Left.Left.Left.Right"))),
                                 TreeNode("Left.Right")),
                        TreeNode("Right",
                                 TreeNode("Right.Left"),
                                 TreeNode("Right.Right",
                                          TreeNode("Right.Right.Left"),
                                          TreeNode("Right.Right.Right"))))
        self.assertEqual(maxDepth(tree), 5)

    # Test 13: Tests a single path left tree
    def test_single_path_left(self):
        tree = TreeNode("Root", TreeNode("Left", TreeNode("Left.Left", TreeNode("Left.Left.Left", TreeNode("Left.Left.Left.Left")))))
        self.assertEqual(maxDepth(tree), 5)

    # Test 14: Tests a single path right tree
    def test_single_path_right(self):
        tree = TreeNode("Root", None, TreeNode("Right", None, TreeNode("Right.Right", None, TreeNode("Right.Right.Right", None, TreeNode("Right.Right.Right.Right")))))
        self.assertEqual(maxDepth(tree), 5)

    # Test 15: Tests a balanced tree with a single leaf node
    def test_balanced_with_single_leaf(self):
        tree = TreeNode("Root",
                        TreeNode("Left",
                                 TreeNode("Left.Left",
                                          TreeNode("Left.Left.Left")),
                                 TreeNode("Left.Right")),
                        TreeNode("Right"))
        self.assertEqual(maxDepth(tree), 4)

    # Test 16: Tests a balanced tree with multiple leaf nodes
    def test_balanced_with_multiple_leaves(self):
        tree = TreeNode("Root",
                        TreeNode("Left",
                                 TreeNode("Left.Left",
                                          TreeNode("Left.Left.Left")),
                                 TreeNode("Left.Right",
                                          TreeNode("Left.Right.Left"))),
                        TreeNode("Right",
                                 TreeNode("Right.Left"),
                                 TreeNode("Right.Right",
                                          TreeNode("Right.Right.Left"),
                                          TreeNode("Right.Right.Right"))))
        self.assertEqual(maxDepth(tree), 4)

    # Test 17: Tests a balanced tree with different depths
    def test_balanced_with_different_depths(self):
        tree = TreeNode("Root",
                        TreeNode("Left",
                                 TreeNode("Left.Left",
                                          TreeNode("Left.Left.Left",
                                                   TreeNode("Left.Left.Left.Left"))),
                                 TreeNode("Left.Right")),
                        TreeNode("Right",
                                 TreeNode("Right.Left",
                                          TreeNode("Right.Left.Left")),
                                 TreeNode("Right.Right",
                                          TreeNode("Right.Right.Left",
                                                   TreeNode("Right.Right.Left.Left")),
                                          TreeNode("Right.Right.Right"))))
        self.assertEqual(maxDepth(tree), 5)

    # Test 18: Tests a balanced tree with a deeper right subtree
    def test_balanced_with_deeper_right(self):
        tree = TreeNode("Root",
                        TreeNode("Left",
                                 TreeNode("Left.Left")),
                        TreeNode("Right",
                                 TreeNode("Right.Left"),
                                 TreeNode("Right.Right",
                                          TreeNode("Right.Right.Left",
                                                   TreeNode("Right.Right.Left.Left")))))
        self.assertEqual(maxDepth(tree), 5)

    # Test 19: Tests a balanced tree with a deeper left subtree
    def test_balanced_with_deeper_left(self):
        tree = TreeNode("Root",
                        TreeNode("Left",
                                 TreeNode("Left.Left",
                                          TreeNode("Left.Left.Left",
                                                   TreeNode("Left.Left.Left.Left"))),
                                 TreeNode("Left.Right")),
                        TreeNode("Right",
                                 TreeNode("Right.Left"),
                                 TreeNode("Right.Right")))
        self.assertEqual(maxDepth(tree), 5)

    # Test 20: Tests a full binary tree
    def test_full_tree(self):
        tree = TreeNode("Root",
                        TreeNode("Left",
                                 TreeNode("Left.Left",
                                          TreeNode("Left.Left.Left"),
                                          TreeNode("Left.Left.Right")),
                                 TreeNode("Left.Right",
                                          TreeNode("Left.Right.Left"),
                                          TreeNode("Left.Right.Right"))),
                        TreeNode("Right",
                                 TreeNode("Right.Left",
                                          TreeNode("Right.Left.Left"),
                                          TreeNode("Right.Left.Right")),
                                 TreeNode("Right.Right",
                                          TreeNode("Right.Right.Left"),
                                          TreeNode("Right.Right.Right"))))
        self.assertEqual(maxDepth(tree), 4)

if __name__ == '__main__':
    unittest.main()

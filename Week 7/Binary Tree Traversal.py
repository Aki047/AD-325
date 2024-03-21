#Comprehensive Binary Tree Traversal and Construction

class TreeNode:
    """A class representing a node in a binary tree."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Node value
        self.left = left  # Left child
        self.right = right  # Right child

def preorderTraversal(root):
    """Traverse the tree in preorder: Root, Left, Right."""
    if root is None: return []
    return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right)

def inorderTraversal(root):
    """Traverse the tree in inorder: Left, Root, Right."""
    if root is None: return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

def postorderTraversal(root):
    """Traverse the tree in postorder: Left, Right, Root."""
    if root is None: return []
    return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.val]

from collections import deque

def levelOrderTraversal(root):
    """Traverse the tree in level order, using a queue."""
    if not root: return []
    queue, result = deque([root]), []
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    return result

# Example tree construction for demonstration
root = TreeNode(1, TreeNode(2), TreeNode(3))

# Demonstrating the traversal functions
print(f"Preorder: {preorderTraversal(root)}")    # [1, 2, 3]
print(f"Inorder: {inorderTraversal(root)}")      # [2, 1, 3]
print(f"Postorder: {postorderTraversal(root)}")  # [2, 3, 1]
print(f"Level Order: {levelOrderTraversal(root)}") # [1, 2, 3]


'''
Test 2 - large tree
root_complex = TreeNode(1)
root_complex.left = TreeNode(2)
root_complex.right = TreeNode(3)
root_complex.left.left = TreeNode(4)
root_complex.left.right = TreeNode(5)
root_complex.right.right = TreeNode(6)
root_complex.left.right.left = TreeNode(7)
root_complex.right.right.left = TreeNode(8)
root_complex.right.right.right = TreeNode(9)

print("Larger and More Complex Tree Traversals:")
print(f"Preorder: {preorderTraversal(root_complex)}")  # Expected: [1, 2, 4, 5, 7, 3, 6, 8, 9]
print(f"Inorder: {inorderTraversal(root_complex)}")   # Expected: [4, 2, 7, 5, 1, 3, 8, 6, 9]
print(f"Postorder: {postorderTraversal(root_complex)}") # Expected: [4, 7, 5, 2, 8, 9, 6, 3, 1]
print(f"Level Order: {levelOrderTraversal(root_complex)}")# Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]


Test 3- skewed tree
root_skewed = TreeNode(1)
root_skewed.right = TreeNode(2)
root_skewed.right.right = TreeNode(3)
root_skewed.right.right.right = TreeNode(4)

print("\nSkewed Tree Traversals:")
print(f"Preorder: {preorderTraversal(root_skewed)}")  # Expected: [1, 2, 3, 4]
print(f"Inorder: {inorderTraversal(root_skewed)}")   # Expected: [1, 2, 3, 4]
print(f"Postorder: {postorderTraversal(root_skewed)}") # Expected: [4, 3, 2, 1]
print(f"Level Order: {levelOrderTraversal(root_skewed)}")# Expected: [1, 2, 3, 4]

'''
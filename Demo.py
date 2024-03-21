"""
Assignment: Decision Support System for a Financial Institution Using Binary Tree

Problem Statement: Inventory Management System Update
The institution uses a decision support system to guide customer service representatives through a series of questions to identify the most suitable financial product for a customer's needs. This system is structured as a binary tree, where each node represents a question, and the two branches from each question lead to the next questions based on the customer's responses (Yes/No). It offers loans, mortgages, investments, and insurance.
"""


class TreeNode:
    def __init__(self, question, left=None, right=None):
        self.question = question  # The question at this node
        self.left = left  # Yes branch
        self.right = right  # No branch

def maxDepth(root):
        if not root:
            return 0
        else:
            left_depth = maxDepth(root.left)
            right_depth = maxDepth(root.right)
            return max(left_depth, right_depth) + 1

root = TreeNode("Do you have an existing account with us?",
                TreeNode("Are you looking for a loan product?",
                         TreeNode("Do you prefer low interest over high credit limit?"),
                         TreeNode("Are you interested in mortgage services?")),
                TreeNode("Are you interested in investment options?",
                         TreeNode("Are you a risk-averse investor?"),
                         TreeNode("Are you looking for insurance products?")))

print(f"Maximum depth of the decision tree: {maxDepth(root)}")

class TreeNode:
    """A node in a binary decision tree."""
    def __init__(self, question, left=None, right=None):
        self.question = question  # The question at this node
        self.left = left  # Yes branch
        self.right = right  # No branch

def maxDepth(root):
    """Determine the maximum depth of the binary tree."""
    if not root:
        return 0  # An empty node contributes no depth
    else:
        # Recursively find the depth of each subtree and take the maximum
        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)
        return max(left_depth, right_depth) + 1  # Add 1 to count the current level

# Example tree construction
root = TreeNode("Do you have an existing account with us?",
                TreeNode("Are you looking for a loan product?",
                         TreeNode("Do you prefer low interest over high credit limit?"),
                         TreeNode("Are you interested in mortgage services?")),
                TreeNode("Are you interested in investment options?",
                         TreeNode("Are you a risk-averse investor?"),
                         TreeNode("Are you looking for insurance products?")))
"""
# Demo of longer depth
root = TreeNode("Do you have an existing account with us?",
                TreeNode("Are you looking for a loan product?",
                         TreeNode("Do you prefer low interest over high credit limit?",
                                  TreeNode("Would you like to explore personal loans?", None,
                                           TreeNode("How about exploring our credit line options?")),
                                  TreeNode("Interested in refinancing options for existing loans?")),
                         TreeNode("Are you interested in mortgage services?",
                                  TreeNode("First-time home buyer? Explore our specialized mortgage options."),
                                  TreeNode("Looking to refinance? Let's find you better rates."))),
                TreeNode("Are you interested in investment options?",
                         TreeNode("Are you a risk-averse investor?",
                                  TreeNode("Explore our bonds and stable value funds for secure investment."),
                                  TreeNode("Check out our diversified mutual funds.")),
                         TreeNode("Are you looking for insurance products?",
                                  TreeNode("Need life insurance? Explore our term and whole life policies."),
                                  TreeNode("Interested in health insurance options?"))))
"""
"""
merge binary trees. Estimate complexity, etc.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(t1: TreeNode, t2: TreeNode) -> TreeNode:
    # Base case: if both nodes are None
    if not t1 and not t2:
        return None
    
    # If one of the nodes is None, return the other node
    if not t1:
        return t2
    if not t2:
        return t1
    
    # Merge values
    merged = TreeNode(t1.val + t2.val)
    
    # Recursively merge left and right children
    merged.left = mergeTrees(t1.left, t2.left)
    merged.right = mergeTrees(t1.right, t2.right)
    
    return merged

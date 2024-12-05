"""
Given the binary tree and a node, the task is to find
the parent of the given node in the tree.
Return -1 if the given node is the root node.

The idea is to write a recursive function that takes
the current node and its parent as the arguments 
()
"""
"""
        1
      /  \
      7   3
    / \   \
    4 5

"""
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
def findParentNode(target, root, parent):
    if not root:
        return -1
    #target is not found
    #e.g: now we are trying to find the parent of 7
    # we will traverse until we find the target, then we return parent
    if root.data == target:
        return parent
    #recursively search in left subtree
    left_search = findParentNode(root.left, target, root.data)
    if left_search != -1:
        return left_search
    return findParentNode(root.right, target, root.data)

#time complexity: O(n)
#space complexity: O(h)
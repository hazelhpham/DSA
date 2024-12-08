def validate(root):
    def isValid(node,left,right):
        if not node:
            return True
        if not (left < node.val < right):
            return False
        left = isValid(node.left, left, node.val)
        right = isValid(node.right, node.val, right)
        return left and right
    return isValid(root, float("-inf"), float("inf"))

#time complexity: O(n) where n is the number of nodes that dfs function visits. 
# it visits each node exactly once. 
#the best case when the tree is balanced: O(logN)
#space complexity: O(n) worst case; O(logN) best case
"""
e.g: 
for 7: we have to check 5 < 7 < 10; 
for 17: 15 < 17 < 20
            10
          /    \
         5      15
        / \     /  \
       2   7   12   20
          / \   /   /  \
         6   8 11   17   25

Starting with the root node (10), bounds (-inf, inf):

Node value: 10
-inf < 10 < inf → True
Recur for the left child with bounds (-inf, 10) and right child with bounds (10, inf).
Left subtree (node=5), bounds (-inf, 10):

Node value: 5
-inf < 5 < 10 → True
Recur for the left child (node=2, bounds (-inf, 5)) and right child (node=7, bounds (5, 10)).
Left child of 5 (node=2), bounds (-inf, 5):

Node value: 2
-inf < 2 < 5 → True
Recur for the left child (None, bounds (-inf, 2)) and right child (None, bounds (2, 5)).
Both children are None, so return True.
Right child of 5 (node=7), bounds (5, 10):

Node value: 7
5 < 7 < 10 → True
Recur for the left child (node=6, bounds (5, 7)) and right child (node=8, bounds (7, 10)).
Left child of 7 (node=6), bounds (5, 7):

Node value: 6
5 < 6 < 7 → True
Recur for the left child (None, bounds (5, 6)) and right child (None, bounds (6, 7)).
Both children are None, so return True.
Right child of 7 (node=8), bounds (7, 10):

Node value: 8
7 < 8 < 10 → True
Recur for the left child (None, bounds (7, 8)) and right child (None, bounds (8, 10)).
Both children are None, so return True.
Back to node=5:

Left subtree (node=2) and right subtree (node=7) are valid.
Return True.
Right subtree of root (node=15), bounds (10, inf):

Node value: 15
10 < 15 < inf → True
Recur for the left child (node=12, bounds (10, 15)) and right child (node=20, bounds (15, inf)).
Left child of 15 (node=12), bounds (10, 15):

Node value: 12
10 < 12 < 15 → True
Recur for the left child (node=11, bounds (10, 12)) and right child (None, bounds (12, 15)).
Left child of 12 (node=11), bounds (10, 12):

Node value: 11
10 < 11 < 12 → True
Recur for the left child (None, bounds (10, 11)) and right child (None, bounds (11, 12)).
Both children are None, so return True.
Back to node=12:

Left child (node=11) is valid, right child is None, so return True.
Right child of 15 (node=20), bounds (15, inf):

Node value: 20
15 < 20 < inf → True
Recur for the left child (node=17, bounds (15, 20)) and right child (node=25, bounds (20, inf)).
Left child of 20 (node=17), bounds (15, 20):

Node value: 17
15 < 17 < 20 → True
Recur for the left child (None, bounds (15, 17)) and right child (None, bounds (17, 20)).
Both children are None, so return True.
Right child of 20 (node=25), bounds (20, inf):

Node value: 25
20 < 25 < inf → True
Recur for the left child (None, bounds (20, 25)) and right child (None, bounds (25, inf)).
Both children are None, so return True.
Back to node=20:

Left child (node=17) and right child (node=25) are valid.
Return True.
Back to node=15:

Left subtree (node=12) and right subtree (node=20) are valid.
Return True.
Back to root=10:

Left subtree (node=5) and right subtree (node=15) are valid.
Return True.
"""

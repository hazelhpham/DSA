# Q1:
# Properties of a Red-Black Tree:
# Each node is either red or black.
# The root is black.
# All leaves (NIL nodes) are black.
# Red nodes cannot have red children (no two consecutive red nodes). --> 2nd level is red only -> next level is black ->... 
# Every path from a node to its descendant NIL nodes must have the same number of black nodes.

def red_black_tree(root):
    if not root:
        return None
    root.val = "Black"
    count = 0
    def black_leaves(node):
        if not node:
            return
        if not node.left and not node.right:
            node.val = "Black"
        black_leaves(node.left)
        black_leaves(node.right)
    def red_nodes(node):
        if node.val == "black":
            if node.left:
                node.left.val = "red"
                red_nodes(node.left)
            if node.right:
                node.right.val = "red"
                red_nodes(node.right)
    def count_black_nodes(node):
        if not node:
            return 0
        if node.val == "Black":
            count+=1
        left = count_black_nodes(node.left) 
        right = count_black_nodes(node.left)
        return count
        
        
        
            



    




#A lot of theory questions for trees 

#Q2: Binary Search Tree Implementation


#Q3: Sorting tree

#Q4: Making a tree into a linked list with the right most nodes on every level point to null

#Q5: DFS / BFs algorithm 

#Q6: Design a Lottery System that returns the winner at random

#Q7: designing an API for front desk trade execution

#Q8: binary tree question, the interviewer give me the binary tree let me print the order of this tree

#Q9: Efficiently check for suspicious transactions based on a few criteria (amount, location, time difference, etc.).

#Q10: Reverse linked list 

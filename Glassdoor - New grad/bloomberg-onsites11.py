#Q1:
"""
do a binary search on an unsorted array
"""

#Q2:
"""
Interview questions [1]
Question 1
1d candy crush, follow-up backtrack solutions most frequent element
"""

#Q3:
"""
Asteroid Collision
"""

#Q4:
"""
Inorder tree traversal
"""
# in order traversal = left, root, right
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def inOrderTraversal(root):
    if not root:
        return None
    left = inOrderTraversal(root.left)
    print(root.val)
    right = inOrderTraversal(root.right)
root = TreeNode(5)
root.left = TreeNode(8)
root.right = TreeNode(10)
inOrderTraversal(root)

#Q5:
"""
1. Valid palindrome 
2. Next largest Number.
"""

#Q6:
"""
Sort the Welsh alphabets using any language.
"""

#Q7:
"""
how to remove a node with a target value in a linked list
"""
class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
def removeFromLL(target):
    pass

#Q8:
"""
Make an algorithm that takes an integer and converts it 
into an ExcelColumn-type string. Ex. 1 -> A; 3 -> C; 27 -> AA.
"""
# 1 -> A
# ...
# 26 -> Z
# 27 -> AA
# 28 -> AB
    #or you can use ord(int)
    #e.g: 27
    #num // 26 -> first digit ->
    #num % 26 = 1
    # AA

    #e.g: 30
    # num // 26 = 1
    # num % 26 = 4
    # AD
def convert_integer_to_excel_column(num):
    result = []
    
    while num > 0:
        num -= 1  # Adjust for 1-based indexing
        remainder = num % 26
        result.append(chr(remainder + ord('A')))
        num //= 26  # Move to the next "digit"
    
    # Since the characters are appended in reverse order, reverse the result
    return ''.join(result[::-1])

# Examples
print(convert_integer_to_excel_column(1))   # Output: "A"
print(convert_integer_to_excel_column(26))  # Output: "Z"
print(convert_integer_to_excel_column(27))  # Output: "AA"
print(convert_integer_to_excel_column(28))  # Output: "AB"
print(convert_integer_to_excel_column(300)) # Output: "KN"


#Q9:
"""
room allocation in an office according to timings, with a high number of employees and a low number of available rooms.
"""

#Q10:
"""
Find the first occurrence of a target in a sorted stream of integers.
"""


#Q11:
"""
If we have a bad hashing algorithm and two values get hashed to the same bucket, 
how is the correct value retrieved?
"""


#Q12:
"""
Write a program in C that gets a string with letters and numbers only, 
and puts the letters on the left side and numbers on the right side. 
(e.g: "1ba23" -> "ba123" or any permutation like this). 
Time Complexity O(n), memory O(1)
"""
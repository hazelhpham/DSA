#1) Identify the parent child relationship among the following rows.
# Parent row: any row which can be represented by summation of the consecutive rows following it. 
# (If the consecutive row is a Parent then it's children may be collapsed/skipped during summation. 


# 2) Question 1: Given 4 random generated numbers from 1-10, 
# write a program to decide whether it is viable to use operations (limited in +, -, *, and /) 
# on each and every number exactly once to generate result 24.
from itertools import permutations

def apply_operation(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return float('inf')  # Avoid division by zero
        return a / b

def can_make_24(nums):
    if len(nums) == 1:
        # If there's only one number left, check if it's 24
        return abs(nums[0] - 24) < 1e-6  # A small tolerance for floating-point precision
    
    # Try all pairs of numbers with all operations
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                # Create a new list excluding nums[i] and nums[j]
                next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                
                for op in ['+', '-', '*', '/']:
                    result = apply_operation(nums[i], nums[j], op)
                    if can_make_24(next_nums + [result]):
                        return True
                    # Try the other order of the numbers (e.g., nums[j] op nums[i])
                    result = apply_operation(nums[j], nums[i], op)
                    if can_make_24(next_nums + [result]):
                        return True
    
    return False

def main():
    # Example: four random numbers from 1 to 10
    nums = [4, 1, 8, 7]
    if can_make_24(nums):
        print("It is possible to make 24.")
    else:
        print("It is not possible to make 24.")

# Run the program
main()

"""
LC #1, #133, #139, #1396, 
Design underground system
Word break
Clone graph

a question involving some unintelligible, 
vague instructions for refactoring an "AppStoreEntry" class.
"""

"""
Vending Machine Object Oriented Design 
"""
#what kind of products?
#for each product, there would be a unique code associated with it? 
# 3D - orange; 4D - apple ; etc
#user would have option to choose a code and vending machine will release the product
class VendingMachine:
    def __init__(self):
        self.d = {}
    def add(self, code, product): 
        self.d[code].append(product)
    def release(self, code):
        if code not in self.d:
            return "Not found"
        return self.d[code]
#test cases:
#data will be in a form of tuple ? or array
first_product = ['3D', 'orange']
second_product = ['4D', 'apple']

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


"""
Implement a class called AirMap that has two methods: 
1. add_route(start, destination) 
- adds ONE WAY connecting flight from one airport to another 
2. print_all_routes(start, destination) 
- prints all possible routes from start to destination 
Given the following routes,
print all possible routes between the airport C and D: 
A -----> B 
B -----> A 
A -----> C 
C -----> A 
A -----> D 
D -----> A 
B -----> C 
C -----> B 
B -----> D 
D -----> B 
Expected Output: [C,A,B,D C,A,D [C,B,A,D] [C,B,D]]
"""
from collections import defaultdict
class AirMap:
    def __init__(self):
        self.routes = defaultdict(list)
    def add_route(self, start, destination):
        #if there is start inside self.routes,
        #else, it is default as an empty list
        self.routes[start].append(destination)
    def print_routes(self, start, destination):
        #dfs on start
        if not start:
            return []
        res = []
        def backtracking(start, destination, path):
            if start == destination:
                res.append(path.copy())
                return
            for d in self.routes[start]:
                path.append(d)
                backtracking(d, destination, path)
                path.pop()
        backtracking(start, destination, [start])
        return res
            


"""
Interview

4 LC questions and 1 behavioral interview. 
1/2 easy LC. The rest medium and 1 low Acceptance medium. 
Then behavior after. Trying to move into a more practical style interview.

Interview questions [1]

Question 1

Just practice LC. Do about 50 Easy. and about 50 - 70 Medium. 20 hard. Top LC Bloomberg questions

Answer question
"""


"""

he was like "don't complicate the things. " He initially asked me my approach and said my approach. He said about its time complexity and asked if I can enhance it. Time complexity needs to be done in air and we need enhance it by thinking in the air.
 Somehow started the coding, he was continuously questioning my approach without even completing my code completely. Not sure how he was expecting a optimal solution without brute-force approach. After the interview I felt like to think twice if offered this position.

Interview questions [1]

Question 1

File entries, of service and their start/stop times. 
Return the top k services that has most execution time stamp. 
Since he mentioned file, I was not sure whether we need to read from the file or how do the program gets input, "don' t complicate the things" was the reply I got.
"""


"""
2. Given a string, return the nonrepeating subsequence
"""
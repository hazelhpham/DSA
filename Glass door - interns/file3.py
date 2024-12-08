# Q1: integer -> roman
def intToRoman(num: int) -> str:
    # List of tuples (Roman numeral, Integer value) in descending order
    roman_numerals = [
        ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
        ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
        ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
    ]
    
    result = ""
    
    # Iterate through the list and subtract the value from num
    for roman, value in roman_numerals:
        while num >= value:
            result += roman
            num -= value
    
    return result

#Q2: Study Cracking the coding interview and do all the chapter questions and then the medium and hard ones.

#Q3: Graph question about airplanes on shared code editor. 
# Interviewer helps you if you get stuck. Asked about the complexity of the solution afterwards.

#Q4: find the second largest number in a tree

#Q5: construct a LinkedList
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, val):
        if not self.head:
            self.head = Node(val)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(val)
    def print_tree(self):
        if not self.head:
            print("There is no linked list")
            return
        cur = self.head
        while cur:
            print(cur.val, end=" -> " if cur.next else "\n")  # Proper arrow placement
            cur = cur.next



#Q6: Given a list of rules, 
# where a rule has a job and list of dependencies for that job, 
# find a valid order in which the jobs can run.

# a variation of course schedule?

from collections import defaultdict, deque

def findJobOrder(jobs, dependencies):
    graph = defaultdict(list)
    in_degree = {job: 0 for job in jobs}

    # Build graph
    for job, deps in dependencies.items():
        for dep in deps:
            graph[dep].append(job)
            in_degree[job] += 1

    # Kahn's Algorithm
    queue = deque([job for job in jobs if in_degree[job] == 0])
    order = []

    while queue:
        job = queue.popleft()
        order.append(job)
        for neighbor in graph[job]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == len(jobs) else []

#Q7: Count the number of occurrences of the alphabets in a string.

#Q8:
#Create a system that receives hotel bookings of the form [ 5, 10 ] 
# (meaning that someone plans to come on day 5 and leave on day 10) 
# and checks if there is availability.


#Q9: 329. Longest Increasing Path in a Matrix
# ---> DFS with memoization
"""
- traverse all cells 
- start dfs on all cells in the matrix
- keep track of the longest path so far. 

- use memoization:
1. store the result of the longest increasing path from each cell.
2. if a cell's value is already computed, re-use it. 

dfs(x,y) function:
1. check the memo table for a pre-computed result 
2. recursively explores all valid neighboring cells when the value is
grater than current cell. 
3. updates the memo table with the longest path starting from 
(x,y)
"""
def longestIncreasingPath(matrix):
    if not matrix or not matrix[0]:
        return 0
    rows, cols = ...
    directions = ...
    memo = [[-1 for _ in range(cols)] for _ in range (rows)]
    #you fill -1 in every single cell 
    def dfs(x,y):
        if memo[x][y] != -1:
            return memo[x][y] #it is already computed
        max_length = 1
        for dx, dy in directions:
            nx, ny = dx+x, dy+y
            if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] > matrix[x][y]:
                max_length = max(max_length, 1 +dfs(nx,ny))
        memo[x][y] = max_length
        return max_length

#Q10: Partition labels

def partitionLabels(s):
    # Step 1: Record the last occurrence of each character
    last_occurrence = {char: i for i, char in enumerate(s)}
    
    # Step 2: Initialize pointers and result list
    partitions = []
    start, end = 0, 0

    # Step 3: Traverse the string
    for i, char in enumerate(s):
        end = max(end, last_occurrence[char])  # Update the end of the current partition
        if i == end:  # When we reach the end of a partition
            partitions.append(end - start + 1)  # Record the size of the partition
            start = i + 1  # Start a new partition
    
    return partitions
s = "ababcbacadefegdehijhklij"
last_occurrences = {'a': 8, 'b': 5, 'c': 7, 'd': 14, 'e': 15, 
 'f': 11, 'g': 13, 'h': 19, 'i': 22, 
 'j': 23, 'k': 20, 'l': 21}
output = [9, 7, 8]


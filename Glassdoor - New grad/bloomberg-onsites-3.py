
#Q21: Given an m x n grid of characters board and a string word, return true if word exists in the grid. 
# The word can be constructed from letters of sequentially adjacent cells, 
# where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
def wordSearch(word, grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    def backtracking(i,r,c):
        if i == len(word):
            return True
        if r >= ROWS or r < 0 or c >= COLS or c < 0 or grid[r][c] != word[i] or (r,c) in visit:
            return False
        visit.add((r,c))
        res = backtracking(i+1, r+1,c) or backtracking(i+1, r, c+1) or backtracking(i+1, r-1, c) or backtracking(i+1, r, c-1)
        visit.remove((r,c)) #backtracking -> remove to explore more 
        return res
    

    for i in range(ROWS):
        for j in range(COLS):
            if word[0] == grid[i][j] and backtracking(0,i,j):
                return True
    return False    
#time complexity: O(m*n*4^L)
#space complexity: O(m*n*4^L)

#Q22: Right side view of binary tree
#STATUS: DONE
from collections import deque
class Node():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
root = Node(1)
root.left = Node(3)
root.left.left = Node(5)
root.right = Node(8)
root.right.right = Node(10)
# [8 10] 
def rightSideViewBT(root):
    if not root:
        return []
    queue = deque([root])
    res = []
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(node.val)
    return res
print(rightSideViewBT(root))
#Time: O(n), space: O(n)



#Q23: Design: subway question. Design functions to record the number of people on the subway.
class SubwaySystem:
    def __init__(self):
        pass
    def getPeopleOnSubway(self):
        pass
#Q24: What is Memoization, and optimize a simple problem using memoization
"""
- Memoization is a type of caching. 
"""
#Q25: Flatten a Linked List

#Q26: Design a system similar to the main project of the team you're applying for


#Q27: Interview
# One LC medium. Went thru my resume. 
# Asked some basic computer networks questions.


# Question 28:
# Some binary tree problem, original LC problem.

#Question 29:
#1. Given a list of non-unique integers and a target value, return the count of how many pairs of integers sum to the target value 
# 2. Write a square root function (without using a built-in or library square root function) 
# 3. Given a sorted linked list, remove all duplicate nodes 
# 4. Implement a class that uses entry/exit swipe information (card, swipe, station) 
# to answer queries of average transit time between pairs of stations. (design and implement api)


#Question 30: Meeting rooms II
def meetingRoomsII(schedule):
    pass

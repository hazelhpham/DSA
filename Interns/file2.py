# second was an API design for a transport system that had users and 


#Q2: implement cding into a directory using python, 

def simplify_path(path: str) -> str:
    stack = []
    components = path.split("/")

    for part in components:
        if part == "..":
            if stack:
                stack.pop()  # Go up one directory
        elif part == "." or part == "":
            continue  # Ignore current directory or empty segments
        else:
            stack.append(part)  # Add valid directory/component

    return "/" + "/".join(stack)

# and a memoization question
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

#Q3: a car navigating a desert (2D array) from a starting point and whether it could reach a gas station with a given fuel amount. 
# It progressively got more difficult with obstacles being added to the map and by the time I was coding I was shook.
"""
Given a 2d matrix that represents a matrix where . denotes empty land, c indicates car, 
and o indicates oasis, and another integer gas which indicates gas we have left. 
Traversing one unit in the matrix consumes 1 gas unit. You can move up, down, left, and right.
So Example: the matrix below and gas = 5 returns true since we can get from c to o in 5 units (1 unit left, 3 units down, and 1 unit right)
[[. . . c .]
[. . . . .]
[. . . . .]
[ . . o . .]]
a) Check if the car can reach the oasis or not. (return bool val)

b) Now suppose there is a gas station in the matrix somewhere that is denoted by an integer k where 
k represents the gas units that the car will be refuelled. So if k is 2, the car will gain gas. 
Check if the car can still reach oasis (with or without a gas station).

"""
from collections import deque
def findOasis(matrix, gas):
    ROWS, COLS = len(matrix), len(matrix[0])
    directions = [[1,0], [-1,0], [0,1], [0,-1]]
    #find the starting position of the car 'c'
    start = None
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 'c':
                start = (r,c)
                break
        if start:
            break
    if not start:
        return False 
    #no starting car found
    
    #START BFS
    visited = set
    visited.add((start[0], start[1]))
    queue = deque([(start[0], start[1], gas)])
    while queue:
        x,y, remaining_gas = queue.popleft()
        #if we reach an oasis and have gas left
        if matrix[x][y] == 'o' and remaining_gas >= 0:
            return True
        for dx, dy in directions:
            nx, ny = dx+x, dy+y
            if (0 <= nx < ROWS and 0 <= ny < COLS and (nx,ny) not in visited and remaining_gas > 0):
                if matrix[nx][ny].isdigit(): #gas station is found
                    new_gas = remaining_gas - 1 + int(matrix[nx][ny])
                else:
                    new_gas = remaining_gas - 1
                if new_gas >= 0:
                    #only continue if there is enough gas
                    visited.add((nx,ny))
                    queue.append((nx, ny, remaining_gas - 1))
    return False
# ************************************************************************************************************
# c) Now let's say there's obstacles in the matrix represented by r. 
# How would you check if a car can reach an oasis? 


# you should not increment steps / levels when avoiding the obstacles. 
# just skip them entirely in your DFS traversal. 
# ensure to pass the updated remaining gas into the recursive DFS calls. 
def findOasisWithObstacles(matrix, gas):
    ROWS, COLS = len(matrix), len(matrix[0])
    directions = [[1,0], [-1,0], [0,1], [0,-1]]
    start = None
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 'c':
                start = (r,c)
                break
        if start: #this is because the outer loop might still be running if we dont break
            break
    if not start: 
        return False #we have never found the car to begin with. 
    dp = {}
    def dfs(x, y, remaining_gas):
        if (x,y) in dp:
            return dp[(x,y)]
        #out of the bounds of obstacles 
        if not( 0 <= x < ROWS and 0 <= y < COLS) or matrix[x][y] == 'r' or remaining_gas == 0:
            return False
        #reaching the oasis
        if matrix[x][y] == 'o':
            return True
        #mark cell as visited for this path
        dp[(x,y)] = False
        for dx, dy in directions:
            if dfs(x+dx, y+dy, remaining_gas-1):
                dp[(x,y)] = True
                break
        return dp[(x,y)]
    return dfs(start[0], start[1], gas)

#Q4: It was 2 round interview, one has leet code medium type questions and other was a system design round. 
# Preparing for topics such as graphs and dp would be sufficient

#Q5: uncompress a compressed string.
def decode_string(s: str) -> str:
    stack = []
    current_string = ""
    current_num = 0

    for char in s:
        if char.isdigit():
            # Build the number (in case it's multiple digits like "12" or "23")
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Push the current string and current number to the stack
            stack.append((current_string, current_num))
            current_string = ""
            current_num = 0
        elif char == ']':
            # Pop from the stack to get the previous string and repeat count
            prev_string, repeat_count = stack.pop()
            current_string = prev_string + current_string * repeat_count
        else:
            # Add characters to the current string
            current_string += char

    return current_string

#Q6: Asked about tree, multiple sorting algorithms. How to seek to a desired place in a
# very large file on disk not able to load to memory at once

#Q7: Leetcode: Number of ships 

#What is the difference between TCP and UCP? 

#Q8: Find the amount of pairs that add to k

#Q9: Implementing a metro system api based on a given api.


# Q1: modified BFS to link a bin-tree level by level in a zig-zag fashion 
from collections import deque
class TreeNode():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def zigZagConversion(root):
    if not root:
        return None
    queue = deque([root])
    left_to_right = True
    res = []
    while queue:
        level = []
        for _ in range(len(queue)):
            if left_to_right:
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                node = queue.pop()
                level.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        res.append(level)
        left_to_right = not left_to_right
    return res
# Q2: designing a subway system 


# Round 2  
# Q1: merge interval
def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Step 1: Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    current_interval = intervals[0]
    
    for next_interval in intervals[1:]:
        # If intervals overlap or are adjacent, merge them
        if next_interval[0] <= current_interval[1] + 1:
            current_interval[1] = max(current_interval[1], next_interval[1])
        else:
            # Add the current interval to the result and move to the next
            merged.append(current_interval)
            current_interval = next_interval
    
    # Add the last interval
    merged.append(current_interval)
    return merged

# Example Usage
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
result = merge_intervals(intervals)
print("Union of intervals:", result)

# Q2: word search

#How to go about designing a real time system where all data is needed for time series? 
#The server should be the one pushing the data instead of having the client pull. 
#Think of a Bloomberg terminal as an example.
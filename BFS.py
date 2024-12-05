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

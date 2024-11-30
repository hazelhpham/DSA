"""
https://leetcode.com/problems/rotting-oranges/description/

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""

"""
FIRST SOLUTION:
Some notes about the problem
- this is a 2d traversal problem. 
- the common solution: BFS / DFS. BFS prioritizes breadth over depth 
i.e: it goes wider before it does depper. 
- in addition to 2d grids, these 2 algorithms are often applied to
problems associated with tree / graph data structures as well. 

-> the contamination would propagate level by level, until it reaches the furthest orange. 
- the number of minutes that are elapsed would be = to the number of levels
in the graph that we traverse during the propagation. 
"""

#Time complexity: O(m*n)
#Space complexity: O(m*n)
from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])  # Get the dimensions of the grid
        q = deque()  # Initialize a queue for BFS
        fresh = 0  # Count the number of fresh oranges
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Define 4 possible directions for movement
        
        # Step 1: Initialize the queue with all rotten oranges and count fresh oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:  # If the orange is rotten
                    q.append((r, c))  # Add its position to the queue
                elif grid[r][c] == 1:  # If the orange is fresh
                    fresh += 1  # Increment the count of fresh oranges

        # If there are no fresh oranges to begin with, return 0 (nothing to rot)
        if fresh == 0:
            return 0

        # Step 2: Perform BFS to rot the fresh oranges
        time = 0
        while q:
            # Process all rotten oranges at the current "time level"
            for _ in range(len(q)):  # Iterate over the current level of the queue
                r, c = q.popleft()  # Pop the current rotten orange
                for dr, dc in directions:  # Check all 4 adjacent cells
                    nr, nc = r + dr, c + dc  # Calculate the new row and column
                    # If the adjacent cell is valid and contains a fresh orange
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Mark the fresh orange as rotten
                        q.append((nr, nc))  # Add the new rotten orange to the queue
                        fresh -= 1  # Decrement the count of fresh oranges
            time += 1  # Increment the time after processing one level of BFS

        # Step 3: Check if there are any fresh oranges left
        # If fresh == 0, all oranges are rotten, return time - 1
        # Subtract 1 because the last increment of time happens after the final level
        return time - 1 if fresh == 0 else -1  # If fresh > 0, return -1 (impossible to rot all oranges)



"""
SECOND SOLUTION:
- time complexity: O(m*n)
- space complexity: O(1) --> not using queue anymore in our code. 
---> we have to use in-place BFS algorithm. 

some notes about the problem:
- starting from the beginning (timestamp == 2), the cells are marked 
with the value 2 contain rotten oranges. from this moment on, we adopt a rule 
as stating as "the cells that have the value of the current timestamp should be visited
at this round of BFS"
- for each of the cell that is marked with the current timestamp, we
then go on to mark its neighbor cells that hold a fresh orange with the next
timestamp. ----> in-place modification. 
- at this moment, we should have timestamp = 3, and meanwhile we also
have the cells to be visited at this round marked out. 
"""

def orangesRottingOptimal(self,grid):
    ROWS, COLS = len(grid), len(grid[0])

    # run the rotting process, by marking the rotten oranges with the timestamp
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    def runRottingProcess(timestamp):
        #flag to indicate if the rotting process should be continued
        to_be_continued = False
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == timestamp:
                    #current contaminated cell
                    for d in directions:
                        n_row, n_col = row + d[0], col + d[1]
                        if ROWS > n_row >= 0 and COLS > n_col >=0:
                            if grid[n_row][n_col] == 1:
                                #this fresh orange would be contaminated next
                                grid[n_row][n_col] = timestamp + 1
                                to_be_continued = True
        return to_be_continued
    timestamp = 2
    while runRottingProcess(timestamp):
        timestamp+=1
    #end of process, to check if there are still fresh oranges left 
    for row in grid:
        for cell in row:
            if cell == 1: #still got a fresh orange left
                return -1
    return timestamp -2 

"""
- this is top-down memoization
- we use recursion memoization to solve the problem. 
Top-down approach (with Memoization):
1. recursive formula:
- the idea is to the move from bottom-right corner of the grid
(destination) to the top-left corner (starting point), and at each
cell (i,j), you can move either down or right
- the number of ways to reach the specific cell (i,j) is the sum of number
of ways to reach the cell below it (i+1, j) and the cell to the right (i, j+1)
if those cells are within bounds:
    paths[i,j] = paths[i+1, j] + paths[i, j+1]
2. base case:
- if you reach the bottom row / rightmost row, there is only 1 way to reach the end
- if i == m-1 or j == n-1, return 1 because there's only one way to reach bottom-right corner
from there 

3. memoization:
- to avoid re-calculating the same sub-problems multiple times, we use a memoization table (memo)
to store the results of previously computed paths. 

4. recursive calls:
- for each cell (i,j), we will call the recursive fucntion to compute the number of paths
by moving down or right, and store the result in memo.
"""
def uniquePaths(m, n):
    memo = {}
    def helper(i, j):
        #1. out of bound -> return 0
        if i >= m or j >= n:
            return 0
        #2. reaching the target -> return 1
        if i == m-1 and j == n-1:
            return 1
        #3. if it is inside the memo -> return memo[(i,j)]
        if (i,j) in memo:
            return memo[(i,j)]
        memo[(i,j)] = helper(i+1,j) + helper(i, j+1)
        return memo[(i,j)]
        #4. helper(i+1,j) + helper(i, j+1)

    return helper(0,0)

#time complexity: O(m*n)
#space complexity: O(m*n)
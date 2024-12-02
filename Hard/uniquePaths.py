def uniquePaths(m, n):
    # Create a 1D DP array for storing the number of unique paths for each column in the current row
    dp = [1] * n
    
    # Iterate through all the rows
    for i in range(1, m):
        # Update the DP array for each cell in the row
        for j in range(1, n):
            dp[j] += dp[j-1]  # Number of ways to get to cell (i, j) is the sum of ways from left and top
    
    return dp[n-1]

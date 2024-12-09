# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0

def coinChange(coins, amount):
    memo = {}

    def helper(remaining):
        # Base cases
        if remaining < 0:
            return float('inf')  # Not possible to make a negative amount
        if remaining == 0:
            return 0  # No coins needed to make amount 0
        if remaining in memo:
            return memo[remaining]

        # Recurrence relation: try every coin and take the minimum
        min_coins = float('inf')
        for coin in coins:
            min_coins = min(min_coins, helper(remaining - coin) + 1)

        memo[remaining] = min_coins
        return min_coins

    # Start with the full amount
    result = helper(amount)
    return result if result != float('inf') else -1

# Examples
print(coinChange([1, 2, 5], 11))  # Output: 3
print(coinChange([2], 3))         # Output: -1
print(coinChange([1], 0))         # Output: 0


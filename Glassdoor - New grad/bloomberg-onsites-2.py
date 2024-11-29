
#Q11: Neetcode 75: Number of islands

def numberOfIslands(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    islands = 0
    def dfs(r,c):
        if r >= ROWS or r < 0 or c >= COLS or c < 0 or (r,c) in visit or grid[r][c] != 1:
            return False
        visit.add((r,c))
        dfs(r+1, c) or dfs(r, c+1) or dfs(r-1, c) or dfs(r, c-1)
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1 and dfs(r,c):
                islands +=1
    return islands
        
#time complexity: O(M*N)
#space complexity: O(M*N)
#*********************************** END ********************************************************

#Q12:Sliding window algorithm 
def sliding_window(s):
    if not s:
        return ''
    l = 0
    char = set()
    for r in range(len(s)):
        char = s[l:r] #continue expanding it until it breaks a condition
        # if the condition is broke, 
        #re-size the window
        if s[r] in char:
            l = l + 1
            char.remove(s[l])
        #do something...
    return len(char)

#*********************************** END ********************************************************

#Q13: Develop an add method that adds a currency relation between 2 currencies (like USD and AUD) and 
# then a get method that gets the value of any one currency from any other currency. 
# So you can add USD to AUD and then add AUD to EUR, then maybe you query USD to EUR and it tells you how much EUR it'd be.
class CurrencyExchange:
    def __init__(self, currency_list):
        self.currency_list = {}
def add(currency1, currency2):
    pass
def get(currency):
    #you have to do dfs for this 
    pass

# *********************************** END ********************************************************
#Q20:
"""
'm' amount of oil can be purchased from 'n' companies.
Every company has 'k' capacity of oil to be sold, you can take zero or many times the quantity offered by each company. 
Give the maximum number of combinations possible.
For examples:
There are three companies: A, B, C
((A: 10), (B:15), (C,50))
Target: 60
Number of Combinations: 4 {[10,50], [15,45], [20,40],[10,20,30]}
"""
def combinationSum(target, dic, key):
    res = []
    def backtrack(total, path, key):
        if total == target:
            res.append(path.copy())
            return
        if total > target:
            return 
        visit = set()
        for key, val in dic.items():
            #if combination sum without duplicates:
            if key in visit:
                continue
            path.append(val)
            backtrack(total+val, path, key)
            path.pop()
    backtrack(0, [])
    return res
#TIME COMPLEXITY:
#SPACE COMPLEXITY: 

# *********************************** END ********************************************************
#Q13: Assume you are given a stream of sequences. You need to implement a system similar to promises in JavaScript, 
# where you wait for one stream to process before moving on to the next. 
# For instance, consider how we watch movies on Netflix: the sequences come in order. 
# Even if sequence 4 loads faster, it should still wait for sequences 1, 2, and 3 to load first. 
# The goal is to ensure that the sequences are processed in the correct order, regardless of their loading times.

#Q14: Know your graphs and backtracking 100% <3 months tag> 

#Q15: 2 medium graph questions

#Q16: Longest substring without repeating characters
def longestNoRepeating(s):

    pass
"""
"""

#Q17: validate binary search tree
#Q18: gas station

#Q19: How you optimize {project function} to handle large amount of requests at same time, give me a optimized solution

#Q20: neetcode 150 + bloomberg tagged on leetcode.

#Q21: Given two string, how to tell if they are anagram? (https://leetcode.com/problems/valid-anagram/)
# * Follow up questions:
# a. What is the runtime & space complexity?
# b. What if the element are not just alphabet, but could be anything (number, Korean letter, emoji..)?
# --> Using high-level language: Hash table
# c. Modify the current code to output how many characters you need to change in order to make the two string anagram?
# d. Runtime & space complexity?


# Q1) You will be given a deck of cards, which has 4 suites and 13 ranks. How would you store it? This a very open-ended question.
# A) Discussed different starting from scratch (like storing in an array) and then went on to implement an object-oriented way with classes and all. Later asked to implement a shuffle function.
# Q2) LC 380 : https://leetcode.com/problems/insert-delete-getrandom-o1/

# Q1) LC 1583 : https://leetcode.com/problems/count-unhappy-friends/
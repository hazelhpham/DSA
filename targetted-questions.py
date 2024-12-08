# You are tasked with analyzing the potential space in a cityscape outlined by a series of skyscrapers. 
# Each skyscraper's height is represented by an element in the array cityLine, where the width of each skyscraper is consistently 1, and they are placed directly adjacent to each other along a road with no gaps. 
# Your mission is to determine the largest square area that can fit within this row of skyscrapers.
# ***** VARIATION OF LARGEST AREA HISTOGRAM *********
# Design an auto correct system like on Apple
def autocorrect(dictionary, input_word):
    def is_one_edit_away(word1, word2):
        # Case 1: Same length - check for one substitution
        if len(word1) == len(word2):
            diff_count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff_count += 1
                    if diff_count > 1:
                        return False
            return diff_count == 1
        
        # Case 2: One extra character in word1 (deletion from word2)
        if len(word1) == len(word2) + 1:
            for i in range(len(word1)):
                # Try deleting word1[i] to match word2
                if word1[:i] + word1[i + 1:] == word2:
                    return True
        
        # Case 3: One extra character in word2 (insertion into word1)
        if len(word1) + 1 == len(word2):
            for i in range(len(word2)):
                # Try inserting word2[i] into word1 to match word2
                if word2[:i] + word2[i + 1:] == word1:
                    return True
        
        # Case 4: Transposition
        if len(word1) == len(word2) and len(word1) > 1:
            for i in range(len(word1) - 1):
                # Try swapping adjacent characters in word1
                if word1[:i] + word1[i + 1] + word1[i] + word1[i + 2:] == word2:
                    return True
        
        return False

    # Check dictionary for words that are one edit away
    candidates = [word for word in dictionary if is_one_edit_away(word, input_word)]
    
    # Return the first candidate or an empty string if no match
    return candidates[0] if candidates else None

# Example usage
dictionary = ["cat", "bat", "rat", "mat", "chat", "cut"]
input_word = "cay"

print(autocorrect(dictionary, input_word))  # Output: "cat"


"""
The main idea is to check if the word in the dictionary can be transformed into the input_word with just one edit. 
The types of allowed edits are:
Substitution (Changing one character to another at the same position).
Insertion/Deletion (One word has an extra character compared to the other).
Transposition (Two adjacent characters are swapped).
"""

"""
EXPLANATION:
Explanation:
Let’s go through the different cases without zip():

Substitution (Case 1):

We compare the characters of word1 and word2 one-by-one. If the characters are different, we increase the diff_count.
If diff_count exceeds 1, it means there’s more than one difference, so we return False. If exactly one character is different, we return True.
Deletion (Case 2):

If word1 has one extra character compared to word2, we try removing each character from word1 and check if the remaining string matches word2.
Insertion (Case 3):

Similarly, if word2 has one extra character compared to word1, we try removing each character from word2 and check if it matches word1.
Transposition (Case 4):

If the lengths are equal and greater than 1, we check for adjacent character swaps. We swap each adjacent pair of characters and check if that matches the second word.
"""


#Insert delete getRandom O(1)
import random

class RandomizedSet:
    def __init__(self):
        self.values = []  # Use a better name instead of `list`
        self.indices = {}  # Maps value -> index in `values`

    def insert(self, val):
        if val in self.indices:
            return False
        self.indices[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val):
        if val not in self.indices:
            return False
        index_to_remove = self.indices[val]
        last_val = self.values[-1]

        # Swap and remove
        self.values[index_to_remove] = last_val
        self.indices[last_val] = index_to_remove
        self.values.pop()
        del self.indices[val]
        return True

    def getRandom(self):
        if not self.values:
            raise ValueError("Set is empty!")
        return random.choice(self.values)
    

rs = RandomizedSet()
print(rs.insert(1))  # Expected: True
print(rs.insert(2))  # Expected: True
print(rs.remove(1))  # Expected: True
print(rs.getRandom())  # Expected: 2 (since only 2 remains)


#Number of islands 

# Number of islands

# Questions:
# - what is the input and output? what is the type? 
# - what are the constraints? < I want you to dig deeper into what kinds of
# constraints do we have and how we use it to leverage our solution?> 

# 1. Approach #1: DFS
# - Treat the 2D grid map as an undirected graph and there is an edge between
# 2 horizontallly and vertically adjacent nodes of value '1'.

# Algorithm:
# - Linear scan the 2d grid map, if a node contains a '1' -> it is a root node. 
# ---> triggers DFS.
# - During DFS, every visited node should be set as '0' to mark as visited node
# < or we can simply keep track of a visit set >. 
# - Count the number of root nodes that trigger DFS, this number would be the same
# number of islands since each DFS starting at some root identifies an island


# Time complexity: O(MxN)
# Space complexity: O(MxN)

# DFS:

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    num_islands += 1

        return num_islands

    def dfs(self, grid, r, c):
        if (
            r < 0
            or c < 0
            or r >= len(grid)
            or c >= len(grid[0])
            or grid[r][c] != "1"
        ):
            return
        grid[r][c] = "0"

        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)
"""
(?) WHY DON'T WE USE OR HERE?
e.g: self.dfs(grid, r-1,c) or self.dfs(grid, r+1,c) etc
   ---> If dfs(r + 1, c) returns True, the subsequent directions (r - 1, c, r, c + 1, r, c - 1) won't even be executed.
	As a result, not all neighboring cells may be visited if one of the earlier recursive calls evaluates to True.
   ---> or works when you check for validation: any path satisfies the condition. 
    but our goal here is to fully traverse connected paths of the grid, not just
    validate the exisitence. 
"""

  
  
  
  

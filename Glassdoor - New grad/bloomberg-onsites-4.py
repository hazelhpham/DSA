
#Question 31:
#Q1) You will be given a deck of cards, which has 4 suites and 13 ranks. How would you store it? This a very open-ended question.
#A) Discussed different starting from scratch (like storing in an array) and then went on to implement an object-oriented way with classes and all. 
# Later asked to implement a shuffle function.


#Question 32:
#Q1) LC 1583 : https://leetcode.com/problems/count-unhappy-friends/
#Q2) LC 200 : https://leetcode.com/problems/number-of-islands/

#Question 33:
#Level-order traversal of binary tree. Zigzag level-order traversal of binary tree.


#Question 34: design a Spotify like system, 
# which is roughly like an LRU cache fashion and at the same time to retrieve the top k played songs

#Question 35:
# 1) Best time to buy and sell stock 
# 2) Given an array, return the element that appears only once

#Question 36:
#An original BFS
#A classic backtrack (subset / permutations)
#A binary tree recursive algo. 

#Question 37: 
#use one pass to find the first unique character in a string 
from collections import Counter

def first_unique_char(s):
    count = Counter(s)  # Count frequency of each character
    for i, char in enumerate(s):  # Single pass through the string
        if count[char] == 1:
            return i  # Return the index of the first unique character
    return -1  # If no unique character found

# Test cases
print(first_unique_char("leetcode"))  # Output: 0
print(first_unique_char("loveleetcode"))  # Output: 2
print(first_unique_char("aabb"))  # Output: -1

#Question 38: valid BST, Create right pointers in BST Virtual Onsite Round 1 - 
# Merge Intervals II 
# Number of Islands Round 2
# Number of ships in a rectangle

#Question 39:Write this code recursively, nested for loop time complexity

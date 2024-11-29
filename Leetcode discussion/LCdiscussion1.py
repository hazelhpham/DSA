# Q1: 
# create a Deque class with some unusual methods all in constant time. 
class Deque:
    def __init__(self):
        pass
# Q2: a binary search question
# Q3: Dp problem dividing N oranges
# --> LeetCode 279: Perfect Squares

# Q4: vertical order traversal

# ********************************************************************************************************

#Q1:  (2020)
#Given a welsh dictionary, sorted in welsh alphabetical order, 
#and a list of words written in the welsh language, sort the list of words in welsh alphabetical order

#SOLUTION 1:
from collections import tuple
alphabets = ['a','b','c','ch','dd','d','e', 'f', 'ff', 'g', 'ng', 'h', 'i', 'j', 'l', 'll', 'm', 'n', 'o', 'p', 'ph', 'r', 'rh', 's', 't', 'th', 'u', 'w', 'y']
alpha_index = {}
for idx,val in enumerate(alphabets):
    alpha_index[val] = idx
def comp(s):
    ret = []
    i = 0
    while i < len(s)-1:
        if s[i] + s[i+1] in alpha_index.keys():
            ret.append(alpha_index[s[i] + s[i+1]])
            i+=2
        else:
            ret.append(alpha_index[s[i]])
            i += 1
    ret.append(alpha_index[s[len(s)-1]])
    return tuple(ret)
strings = ['abcd', 'abcdd']
a = strings.sort(key=comp)
print(strings)

#SOLUTION 2:
def comp(s):
    ret = []
    i = 0
    while i < len(s):
        if i+1 < len(s) and s[i] + s[i+1] in alpha_index.keys():
            ret.append(alpha_index[s[i] + s[i+1]])
            i+=2
        else:
            ret.append(alpha_index[s[i]])
            i += 1
    return tuple(ret)

# ********************************************************************************************************


#Q2: Implement a method that sort words, but instead of using the normal alphabet a, b, c, ..., x, y, z, 
# we have ch that goes between h and i in the sort order. So the alphabet becomes a, b, ... h, ch, i, ... x, y, z.
# Example 1:
# Inout: ["indigo", "charisma", "hotel"]
# Output: ["hotel", "charisma", "indigo"]
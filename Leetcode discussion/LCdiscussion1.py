# Q1: 
# create a Deque class with some unusual methods all in constant time. 
class Deque:
    def __init__(self):
        pass
# Q2: a binary search question
# Q3: Dp problem dividing N oranges
# --> LeetCode 279: Perfect Squares


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

def custom_sort_key(word):
    # Create a dictionary for custom order
    order = {chr(i): i-97 for i in range(97, 123)}  # 'a' to 'z'
    order['ch'] = 8  # 'ch' comes between 'h' and 'i'
    
    # Helper function to return a custom sort key based on the character positions
    def custom_order(c):
        if c == "ch":  # Handle "ch" as a special case
            return order[c]
        return order.get(c, -1)
    
    # We split the word by the custom rule, where we treat "ch" as a single character
    i = 0
    custom_key = []
    while i < len(word):
        if i + 1 < len(word) and word[i:i+2] == 'ch':  # Check for 'ch'
            custom_key.append("ch")
            i += 2  # Skip next character after "ch"
        else:
            custom_key.append(word[i])
            i += 1
    
    return [custom_order(c) for c in custom_key]

def sort_words(words):
    # Sort the words using the custom sort order
    return sorted(words, key=custom_sort_key)

# Example usage
words = ["indigo", "charisma", "hotel"]
sorted_words = sort_words(words)
print(sorted_words)  # Output: ["hotel", "charisma", "indigo"]

# Q1: 
# create a Deque class with some unusual methods all in constant time. 
class Deque:
    def __init__(self):
        pass
# Q2: a binary search question
def searchInRotatedArray(target, arr):
    if not arr:
        return -1
    # [ 5 6 7 8 1 2]
    #find 6
    #check if it is in left sorted array
    #check if it is in right sorted array 
    l = 0
    h = len(arr)-1
    while l <= h:
        mid = (l+h)//2
        if arr[mid] == target:
            return mid
        if arr[l] <= arr[mid]:
        #this left half is sorted
            if arr[l] <= target <= arr[mid]:
                h = mid - 1
            else:
                l = mid +1
        elif arr[mid] <= arr[h]:
            #
            if arr[mid] <= target <= arr[h]:
                l = mid + 1
            else:
                h = mid - 1 
    return -1

arr = [5, 6, 7, 1, 2]
print("search in rotated sorted array", searchInRotatedArray(5, arr))


# Follow-ups: Search in rotated sorted array II
def searchInRotatedSortedArrayII(arr, target):
    if not arr:
        return -1
    
    l = 0
    h = len(arr) - 1
    
    while l <= h:
        mid = (l + h) // 2
        
        if arr[mid] == target:  # Target found
            return mid
        
        # Handle the case where we can't determine the sorted half because of duplicates
        if arr[l] == arr[mid] == arr[h]:
            l += 1
            h -= 1
        # Left half is sorted
        elif arr[l] <= arr[mid]:
            if arr[l] <= target < arr[mid]:  # Target is in the left half
                h = mid - 1
            else:  # Target is in the right half
                l = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[h]:  # Target is in the right half
                l = mid + 1
            else:  # Target is in the left half
                h = mid - 1
    
    return -1  # Target not found

# Q3: Dp problem dividing N oranges
# --> LeetCode 279: Perfect Squares

def countWaysToDivide(N, K):
    # DP table to store results of subproblems
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    
    # Base Case: There is 1 way to divide 0 oranges into any number of parts
    for i in range(K + 1):
        dp[0][i] = 1

    # Fill the DP table using the formula
    for n in range(1, N + 1):
        for k in range(1, K + 1):
            # Ways to divide n oranges into k parts
            dp[n][k] = dp[n-1][k-1] + dp[n-1][k]

    return dp[N][K]

# Example
N = 5  # Number of oranges
K = 2  # Number of parts to divide into
print("Ways to divide oranges:", countWaysToDivide(N, K))



# ********************************************************************************************************

#Q1:(2020)
#Given a welsh dictionary, sorted in welsh alphabetical order, 
#and a list of words written in the welsh language, 
# sort the list of words in welsh alphabetical order

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
# we have ch that goes between h and i in the sort order. 
# So the alphabet becomes a, b, ... h, ch, i, ... x, y, z.
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

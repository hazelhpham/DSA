# Round 1:


# Start with walking through the resume and 
# Question 1: asking the most challenging project on resume.
# Question 2: 
# Almost similar to this question https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
# I came up with the solution that using stack then the interviewee asked me for another one that did not use extra space. 

def removeDuplicates(s, k):
    stack = []
    for char in s:
        if stack and s[-1][0] == char:
            s[-1][1] +=1
            if s[-1][1] == k:
                stack.pop()
        stack.append((char, 1))
    string_builder = []
    for char, count in stack:
        string_builder.append(char*count)
    return ''.join(string_builder)
#O(n)
#O(n)

def removeDuplicatesOptimal( s, k):
        # Convert the string to a list because strings are immutable in Python
        s = list(s)
        
        j = 0  # Pointer to keep track of the position where we write the next valid character
        counts = []  # Stack to keep track of counts of consecutive characters

        for i in range(len(s)):
            s[j] = s[i]  # Place the current character at the "write" position
            if j == 0 or s[j] != s[j - 1]:
                # If the character is different from the previous one, start a new group
                counts.append(1)
            else:
                # If it's the same as the previous character, increment its count
                counts[-1] += 1
                if counts[-1] == k:
                    # If the count reaches k, remove the character
                    counts.pop()
                    j -= k  # Move j back by k positions to erase the k characters

            j += 1  # Move the "write" pointer forward
        
        # The result string is the substring of s up to the "j" index
        return ''.join(s[:j])



# Start with the resume but this time, the interviewee focused on the architecture. He asked me to tell him the architecture of my project.

# Question1: Given a list of operation hour for each stock exchange, validate if the customer can send a trading order during the input hour.
# The interviewee asked me to list all possible solutions that I got and explain the time and space complexity of each solution. 
# Also, he asked me to describe the advantages and disadvantages of each one.
# After finishing all analysis, he asked me to code the simple solution and show him how I was going to test this problem.
#  Operation hours
#  09:00-16:00 Royal Bank of Scotland
#  11:00-17:00 Morgan Stanley
"""
basically see if the new_interval would be collapsed with the time intervals above
if its 10:00-12:00 ---> successful
[[9,16], [11,17]]
"""
def validateTrading(customerTime, bankTime):
    if not bankTime:
        return False
    if not customerTime:
        return True
    #when there is no time schedule, customer cannot make a trade!
    #use the start and end
    for time in bankTime:
        start_bank = time[0]
        end_bank = time[1]
        if customerTime >= start_bank and customerTime <= end_bank:
            #it is in the range of valid start and end time of a bank
            return True
    return False
#Brute force approach:
"""
Solution:
- iterate through each bank's time interval 
- for each bank interval, check if the customer's entire requested time fits within the bank's interval.
pros:
1. simple to implement
2. time complexity: O(n). where n is the number of slots in the bankTime list. 
Each check involes a constant-time comparison of 2 time intervals, so it's efficient when
the number of bank time slots is small. 
cons:
1. inefficient for large inputs: the number of bank time slots grow large -> this approach will be slow
2. doesn't account for overlaps. --> if you want to support more complex logic, such as merging overlapping time slots before checking
this solution won't work well. 


2nd solution:
Sorting and binary search. 
1. sort the bankTime 
2. use binary search to find earliest valid time slot that can fit
the customerString using bisect_left or similar approach

3rd solution:
Greedy approach

solution:
- iterate through sorted bank time intervals
- for each bank interval, try to merge overlapping intervals
- keep merging until you find a spot where customerTime can fit. 
this is especially good with an array that has many time slots. 
you use them to merge them all together. 

"""
#EXPECT: SUCCESS!
customerTime = [10,17]
bankTime = [[10,12], [9,17], [8,15]]
if validateTrading(customerTime, bankTime):
    print("Test case #1: customerTime" + str(customerTime) + "with this bank time" + str(bankTime) + "----> SUCCESS")
else:
    print("Test case #1: customerTime"+ str(customerTime) + "with this bank time" + str(bankTime) + " -----> FAILURE")
import bisect
#sorting and binary search
def validateTradingOptimal(customerTime, bankTime):
    if not bankTime:
        return False
    if not customerTime:
        return True
    bankTime = sorted(bankTime, key = lambda x:x[0])
    customer_start, customer_end = customerTime
    #use binary search to find the first interval that starts
    #after the customer's start time  
    idx = bisect.bisect_left(bankTime, [customer_start, -float("inf")])
    if idx < len(bankTime):
        bank_start, bank_end = bankTime[idx]
        if customer_start >= bank_start and customer_end <= bank_end:
            return True
    if idx > 0:
        #check the previous bank interval
        bank_start, bank_end = bankTime[idx-1]
        if customer_start >= bank_start and customer_end <= bank_end:
            return True
    return False

# Question 2 : Given two arrays, return the intersection of two lists.
# I came up with the first solution that used a set. 
# Then, he asked me to think of another one which does not need to declare extra space. 
# I told him if A and B are sorted, there is another smart brute force solution (using binary search).
# Then, he asked me to code the first solution (using set) and show him how to test this problem.
# A = [1, 2, 3, 4]
# B = [2, 4, 6]
# Result - [2, 4]

"""
1. use a set 

2. if A + B are sorted --> simply compre each element in the 2 arrays and append into new list

3. binary search?
"""


def intersection_with_set(A, B):
    # Convert A to a set for fast lookup
    set_A = set(A)
    result = []
    
    for num in B:
        # If the number exists in set_A, it's an intersection
        if num in set_A:
            result.append(num)
            set_A.remove(num)  # Ensure uniqueness (to handle duplicates)
    
    return result

# Example usage:
A = [1, 2, 3, 4]
B = [2, 4, 6]
print(intersection_with_set(A, B))  # Output: [2, 4]



"""
- in the case where 2 arrays are sorted ---> use pointers
"""
def intersection_sorted_twopointers(A, B):
    i, j = 0, 0
    result = []
    
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            result.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    
    return result

# Example usage:
A = [1, 2, 3, 4]
B = [2, 4, 6]
print(intersection_sorted_twopointers(A, B))  # Output: [2, 4]


import bisect

def intersection_binary_search_binarysearch(A, B):
    # First, sort both arrays (if not already sorted)
    A.sort()
    B.sort()
    
    result = []
    
    # Use binary search for each element in the smaller array
    for num in A:
        # Check if num is in B using binary search
        idx = bisect.bisect_left(B, num)
        if idx < len(B) and B[idx] == num:
            result.append(num)
    
    return result

# Example usage:
A = [1, 2, 3, 4]
B = [2, 4, 6]
print(intersection_binary_search_binarysearch(A, B))  # Output: [2, 4]

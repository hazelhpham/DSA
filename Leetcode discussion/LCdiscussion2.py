#Q1:
# You are hosting a meeting in 2 locations. All Employess need to attend the meeting in either one of the locations. The Costs of Transporting each employee is Given.
# A B
# Empoloyee 1: $1000 $1500.
# Employee 2: $2000 $800
# ...
# Each Location has a Maximum limit of people it can accomodate. How would you minimize the cost.
# Even Though I was not asked about it, A good followup question could be "How would you go about this problem if there were more than one locations?"
def twoCityScheduling(arr):
    pass


#Q2:
"""
 Find the absolute minimum distance between two points. Return those two points and the minimum distance. 
 Follow ups : minimize the space complexity and really simple ones, such as update the the previous points.
"""
#name of python function = camelCase 
def minDistanceBetweenTwoPoints(points):
    pass

#Q3:
"""
take 1D candy crush as the same as remove adjacent duplicates in string ii.


However, I don't think this is the case. There are 2 key differences.

remove adjacent duplicates in string ii removes the first k elements. So if you have aaaa, you will be left with a, candy crush will eliminate >=3. 
This is quite different to implement
candy crush is not a greedy remove method. for example: aabbbabbba in candy crush will get "", any greedy method will remove the first aaa and will leave a.
These are small differences that need to be accounted for. Just in case if you go in will incorrect assumptions.
"""

#Q4:Interleaving strings

#Q5: The question is to check the current status of Connect 4 game board, and to return if who wins without any moves or one of the players can win with the next move. 
# The input is board(2D array), and the next player.


#Q6:
"""
Given some numbers [3,5,7,8,10], and interval list : [1,6,15] , they wanted to know how many numbers occur between each interval . The answer for this example will be : [2,3] i.e [1,6] -> [3,5] and [6,15] -> [7,8,10].
I clarified the interval assumptions. the boundaries inclusivity & exclusivity. I gave a binary search related answer, after sorting out the numbers. Collaborated perfectly during the entire time.
The Solution I coded out :
For each element in intervals list , using Binary search get the index of element just less than or equal to the given element
eg for intervals [1,6,15] : [-1,1,4]
return the difference array : [(1-(-1)),(4-1)] : [2,3]
"""

#Q7:
"""
Given 2 linked list add the numbers and return the list -- https://leetcode.com/problems/add-two-numbers/


Follow up question 1 - Can you solve this question without using Stack
Follow up question 2 - Can this problem be solved without using carry /remainder
"""

#Q8: Add 2 numbers II 

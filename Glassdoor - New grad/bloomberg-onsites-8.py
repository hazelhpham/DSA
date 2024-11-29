# Q1:
# 1. Two City Scheduling 
# 2. All paths from source to target 
# 3. Matrix grid problem. Some cells have 1's and the rest have zeros. Every day all cells adjacent to the 1 cells turn into ones.
# Write a function to return number of days it takes for the whole grid to turn to 1's (Rotting oranges question)

#Q2: source https://leetcode.com/discuss/interview-question/2798094/Bloomberg-onsite-interview-experience 

"""
Trades
[ (“TSLA US Equity”, 500), (“TSLA US Equity”, 600), (“VOD LN Equity”, 1000), (“TSLA UW Equity”, 250)]


Equivalences
[ (“TSLA US Equity”, “TSLA UB Equity”), (“TSLA UB Equity”, “TSLA UW Equity”), (“VOD LN Equity”, “VOD IN Equity”)]


Here we have to consider TSLA US Equity, TSLA UB Equity, TSLA UB Equity, TSLA UW Equity as one company and count trade values from Trades input.


Output
[ ("TSLA US Equity", 1350), ("VOD LN Equity", 1000) ]


inputs:-


Trades
[ (“TSLA US Equity”, 500), ("TSLA UQ Equity", 100)]


Equivalences
[ ("TSLA US Equity", "TSLA UB Equity"), ("TSLA UQ Equity", "TSLA UW Equity"), ("TSLA UB Equity", "TSLA UQ Equity") ]


Output
[ (“TSLA US Equity”, 600)]

-----> Account merging 
"""

#Q3: Nested list 


#Q4: Given two integers n and p, continually iterate through 1...n and remove the pth integer, until there is only one integer left

#Q5: Find the kth largest number in BST?

#Q6: Deep copy of a random linked list.
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.random = None
head = Node(1)
head.next = Node(3)
head.next.next = Node(4)
head.next.random = head
head.random = head.next.next
def copyRandomList(head):
    if not head:
        return None
    oldToNew = {None:None}
    cur = head
    while cur:
        copy = Node(cur.val)
        oldToNew[cur] = copy
        cur = cur.next
    #reset cur again to point at the head again
    cur = head
    while cur:
        copy = Node(cur.val)
        copy.next = oldToNew[cur.next]
        copy.random = oldToNew[cur.random]
        cur = cur.next
    return oldToNew[head]



#Q7: Valid parentheses 

#Q8: flatten linked list 

#Q9: lots of people in a running competition and there are lots of check points, build and maintain a real time top ten list.
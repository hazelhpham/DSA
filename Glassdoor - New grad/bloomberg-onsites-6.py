# Q1: Remove every nth element from cyclical elements and return the index
# What is cyclical?
# In a cyclical structure, the last element is connected back to the first element, forming a loop or cycle. This means that after the last element, the sequence continues again from the beginning. It's commonly used in data structures like:

# Circular Linked Lists: where the last node's next pointer points back to the head node.
# Circular Arrays: where the index wraps around to the beginning when you go past the last element.
# 1 -> 2 -> 3 
# <---------|
def detectCycle(head):
    if not head:
        return False  # If the list is empty, no cycle exists
    slow, fast = head, head  # Initialize both slow and fast pointers to the head of the list
    while fast.next and fast.next.next:  # Continue while there are at least two nodes for the fast pointer
        slow = slow.next  # Move the slow pointer one step ahead
        fast = fast.next.next  # Move the fast pointer two steps ahead
        if slow == fast:  # If slow and fast pointers meet, a cycle is detected
            return True
    return False  # If fast pointer reaches the end of the list, no cycle exists
"""

Number of ways to purchase oil (https://leetcode.com/discuss/interview-question/550259/bloomberg-phone-interview-se-grad-2020)
This one was not listed, but brought up once on a post back in May 2020. 
Looking at discussion post, it seems to be a blend of https://leetcode.com/problems/subsets/ and dp(?)
Valid Palindrome (https://leetcode.com/problems/valid-palindrome/)
Follow up: How would you make the string valid, if not valid ?

To solve the "Valid Palindrome" problem, you need to check if a string reads the same forward and backward, 
ignoring non-alphanumeric characters and case differences.

Follow-up: If the string is not a palindrome, you can make it valid by removing one character at a time 
and checking again. If removing a single character allows the string to become a palindrome, it is valid. 
If more than one removal is required, it's not valid.

For implementation, use two pointers moving towards the center and validate each character step-by-step.
For more details, refer to the problem here.

"""


#Q4: Graph question to find shortest paths


#Q8: UDP Packet Processing in Order, accounting for lost/out of order packets.

#Q9: LFUcache 
# Technical: top k stocks, 
# word square

#Q10: Pre order and inorder traversal to construct the tree
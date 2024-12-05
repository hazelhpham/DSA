# Add 2 numbers in linked lists 

"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""
class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None
def add2Numbers(l1, l2):
    if not l1 and not l2:
        return ListNode(0)
    dummyNode = ListNode(0)
    cur = dummyNode
    carry = 0
    while l1 != None or l2 != None or carry != 0:
        num1 = l1.val if l1 else 0
        num2 = l2.val if l2 else 0
        total = num1 + num2
        val = total % 10
        new_node = ListNode(val)
        carry = total // 10
        cur.next = new_node
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummyNode.next #but this will return starting from 7 -> 0 -> 8

"""

Time complexity: 
𝑂(max⁡ (𝑚, 𝑛))
---> max time to loop through elements would be the time to loop through the longer linked list 
"""
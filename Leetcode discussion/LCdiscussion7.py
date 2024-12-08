 #Q1: Find the minimum steps to generate a number given only two operations (BFS)

#Q2:
"""
Design a system that gets packets out of order and how will you handle it.
My Solution: For example, if you have a video, and you receive packets in order 0,1,2,5,6,3,7,4, 
you will have to keep track of the incoming and previous packet. 
If the incoming packet is not the expected packet, you will need to store it somewhere and wait until the expected packet has arrived. If the expected packet does not arrive until your timeout, you either continue streaming with the next packet or throw an exception based on the importance of having every packet. For example, if it is just a song, it might not make a big difference if a couple of seconds are skipped. I used maps to write the code for my solution.

"""

#Q3:
"""
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
I was able to provide them with a recursive solution but could not give the DP solution. 
The interviewer did not seem to be satisfied.
"""
"""
Design 3 methods for a system. 
The first method enables us to add new customers to the end of the queue (waiting line). 
The second method enables us to place the first customer in the queue, to an available table. 
The 3rd method allows us to let a customer in the queue to move forward by 1 position when thhey pay $1. 
After some brainstorming, the approach that I came up with was to use a LinkedList and a Map of Node, Position. 
(The time complexity for each method was supposed to be O(1)). The interviewer was satisfied with my solution.
"""

#Q4:
"""
What are static variables in C++, why they're used.
Explain in detail what are virtual functions, why they're used. 
This was followed by discussion on runtime polymorphism.
Then basic questions on OOP about abstraction, encapsulation,etc.
Then she gave me 1 DSA problem and asked not to code, 
just tell the best approach you can have at this, what data structures will you use and what will be its time complexity. The question was something like this (I don't remember the exact question):


You are given a list of names with their phone numbers, you've to make an address book. Following searches can be made in this address book: 
* Search via name (Return phone number)
* Search via number (Return name)
"""


#Q5:
"""
Given a string containing brackets (always matched) and characters, print all strings which are there in the innermost brackets. 
eg: If input is ran(n(d))o(m()),
print 'd', ''.
"""

#Q6:
"""
Design an ecommerce website.
"""

# Note for you, be slow and think about problems. 

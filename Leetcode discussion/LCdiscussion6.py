#Q1: 
#   System Design (1 hour):
#   	Some version of the top-k stock trades by Volume and Value.
#   	Discussed several algorithmic approaches
#   	Deployment discussion.
#   	Functional requirements: Api end points, return types, user types
#   	Non Functional requirements: Real time? Latency, expected throughput, traffic, etc

#Q2:
#   Design a system that gets packets out of order and how will you handle it.
#   Design 3 methods for a system. The first method enables us to add new customers to the end of the queue (waiting line). The second method enables us to place the first customer in the queue, to an available table. The 3rd method allows us to let a customer in the queue to move forward by 1 position when thhey pay $1. 
# The time complexity for each method was supposed to be O(1).

#Q3: Design queue using stacks 

#Q4:
"""
  Design two classes:
  	Document that keep tracks of pages. Method to add a page, and one to retrieve a page.
  	Page that keeps tracks the order of words on that page. Method to add words.
  	Use those two classes to return a list of words, in order, with their respective page numbers, in order.
"""

#Q5:
# https://leetcode.com/discuss/interview-question/737605/Bloomberg-New-Grad-or-Hiring-Manager-System-Design-Round-or-Gathering-Questions

#Q6:
"""
Problem Description
Given a list of transactions consisting of a name, amount, time, and location, determine which transactions are potentially fraudulent.
A transaction is potentially fraudulent, if either of the following conditions is true:


The amount is greater than $1, 080.
The last or next transaction with the same name occurs at a different location within an hour (<= 60).
The input will be a string.
Each transaction will be on a separate line and will have the format: <names, , <times, , Time is measured in minutes.
Transactions are sorted by increasing order by time.

transaction = [
"Anne, 100, 1, Boston",
"Anne, 2000, 10, Boston",
"Bob, 50, 20, Boston",
"Cindy, 100,50, New York",
"Bob, 50, 70, New York",
"Bob, 50, 90, Atlanta",
"Bob, 50, 200, Atlanta",
"Bob, 50, 201, New York",
"Bob, 50, 400, New York"
]

"""

#Q7: LC528. Random Pick with Weight 
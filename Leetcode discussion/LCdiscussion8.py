# Q1: Similar to Collatz Conjecture (haven’t seen on LC before)
# somewhat close to sort integers by the power of two
# Starting from 1, generate a sequence - which denotes the operations used to reach the target
# 	* multiple by 2
# 	* floor division by 3

# Example 1:
# # target = 1
# # output: ""
# # explanation: 1 (target) = 1, no operations needed

# Example 2:
# # target = 2 
# # output: "*"
# # explanation: 2 (target) = 1 * 2 

# Example 3:
# # target = 8 
# # output: "***"
# # explanation: 8 (target) = 1 * 2 * 2 * 2 

# Example 4:
# # target = 10 
# # output: "****/*"
# # explanation: 10 (target) = 1 * 2 * 2 * 2 * 2 // 3 * 2

# Example 5:
# # target = 3 
# # output: "****/*/"
# # explanation: 3 (target) = 1 * 2 * 2 * 2 * 2 // 3 * 2 // 3
# follow-up question - what if we call the method multiple times?
# code a solution for expanded scope
# follow-up question - code optimization for the expanded scope
# follow-up question - optimize it further


#Q2:
"""
The task of design interview was to create a program which would stream data from some eternal data provider to several applications that are running on a machine. 
External data provider sends info about trades being done on stock exchange. Other applications are run as separate processes on the same machine, they can ask your program to send them data about exchange data on certain stock. The main questions of the design were about how to transfer data from your process to other processes, how to support streaming of data of multiple stocks. There were also extra questions about what to do when other processes that queried data die, how do you manage the state of the application. There was no coding in my system design interview, 
we have just discussed different approaches to the problem and I drawed my solution on paper.
"""
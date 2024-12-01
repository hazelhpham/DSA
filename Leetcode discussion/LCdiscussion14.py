#Q1:
# . Implement methods of a Garage class
# a ) addJob
# b) calculateTotalCost
# c) calculateTotalCostWithVAT
# d) calculateCostExcluding - can't remember the exact criteria to exclude
# The interviewer took a good amount of time to explain the problem. Because there were so many classes like Customer, Job, WorkItem, Motorbike etc. I managed to finish a) and b). 
# Explained my solution for c) and d). I didn't code c and d (as we were out of time). 
# I was out of time because there were so much discussion around first two methods (though I coded both of them real quick and tested).
#Q2:
"""
A linked list of cards are given. Write a code, to Shuffle the cards, without using inbuilt shuffle / random functions.
Functionalities :
Create a deck of card through linked list
Split the deck of cards randomly into 2 subsets
Merge the subsets randomly , so that previous order is not maintained
Display the deck of cards .
Eg:
I/p Cards: [A,4,6,7,9,K,Q,J,2]
Expected Output:
Create Linked List : [A->4->6->7->9->Q->J->2]
Split List into 3 decks : A->4->6->7 9->Q J->2
Merge the decks randomly : 9->6->7 ->Q ->J->2->4->A
"""

#Q3:
"""
If the graph is given as illustrated in the highlighted section, how will you use it to draw the table below it which displays Parent, Child and their ownerships % mapped (Parent to Child).


Example :


Suppose initially A has 100
According to the figure A--B = 50 %, table shows A - B = 50 % (which is 50 % of A's 100)
then According to the figure B--D = 50 %, table shows A - D = 25 % (which is 50 % of B's 50)
then According to the figure D--G = 10 %, table shows A - G = 2.5 % (which is 10 % of D's 25)


that's what is shown in the table.
I started creating a TreeNode with the node name 'A' etc. and its percentage and left and right child. Interviewer was ok with that. You need to print the same table. Hope that help !
"""


#Q5:
"""
A labyrinth of zeros and ones is given. Zero - "cannot pass", One - "can pass."
List all paths from top left to bottom-right corner. You can move only down or to the right.
Input: 2-dimensional array that contains the labyrinth.
Example:
Input = [[1,0,1], [1,1,1], [0,1,1]]
Input in 2D:
1 0 1
1 1 1
0 1 1


Output:
(0,0) (1,0) (1,1) (2,1) (2,2)
(0,0) (1,0) (1,1) (1,2) (2,2)
"""

#Q5:
"""
https://leetcode.com/problems/gas-station/description/
gas station problem. with a twist:
The car can go backwards
The solution is to return the maximum distance traveled, rather than simply a boolean
"""
#Q1:
# Implement methods of a Garage class
# a) addJob
# b) calculateTotalCost
# c) calculateTotalCostWithVAT
# d) calculateCostExcluding - can't remember the exact criteria to exclude
# The interviewer took a good amount of time to explain the problem. 
# Because there were so many classes like Customer, Job, WorkItem, Motorbike etc. I managed to finish a) and b). 
# Explained my solution for c) and d). I didn't code c and d (as we were out of time). 
# I was out of time because there were so much discussion around first two methods (though I coded both of them real quick and tested).
#this is SSE

#Q2:
"""
A linked list of cards are given. 
Write a code, to Shuffle the cards, without using inbuilt shuffle / random functions.

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
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, value):
        if not self.head:
            node = Node(value)
            self.head = node
        #traverse till the end of the list
        cur = self.head
        while cur:
            cur = cur.next
            if not cur.next:
                node = Node(value)
                cur.next = node
    def to_list(self):
        result = []
        cur = self.head
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result
    def split_into_parts(self, number_of_parts):
        for _ in range(number_of_parts):
            parts = LinkedList() #each part wopuld be a Linked List
        #we start at the beginning of the linked list
        current_node = self.head
        #traverse through each node in linked list
        index = 0
        while current_node:
            #this is basically like dividing cards equally for 4 people
            parts[index % number_of_parts].append(current_node)
            #so this is a simple hashing function?
            #this is round-robin fashion.
            #the % ensures that the cards are distributed evenly
            current_node = current_node.next
            index+=1
        return parts
    def merge_randomly_ll(self,linked_lists):
        merged_list = LinkedList()
        current_list = []
        for linked_list in linked_lists:
            current_list.append(linked_list)
        while any(current_list):
            for i in range(len(current_list)):
                if current_list[i]:
                    merged_list.append(current_list[i].value)
                    current_list[i] = current_list[i].next
        return current_list


#Q3:
"""
If the graph is given as illustrated in the highlighted section, 
how will you use it to draw the table below it which displays Parent, Child and their ownerships % mapped (Parent to Child).
Example :
Suppose initially A has 100
According to the figure A--B = 50 %, table shows A - B = 50 % (which is 50 % of A's 100)
then According to the figure B--D = 50 %, table shows A - D = 25 % (which is 50 % of B's 50)
then According to the figure D--G = 10 %, table shows A - G = 2.5 % (which is 10 % of D's 25)
that's what is shown in the table.
I started creating a TreeNode with the node name 'A' etc. and its percentage and left and right child. Interviewer was ok with that. You need to print the same table. Hope that help !
"""
class TreeNode:
    def __init__(self, val, percentage):
        self.val = val
        self.percentage = percentage  # Ownership percentage from the parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def print_tree(node, parent_name, accumulated_percentage):
    if not node:
        return

    # Calculate the percentage from the parent to the current node
    current_percentage = accumulated_percentage * (node.percentage / 100)

    # Print the current relationship and percentage
    if parent_name:  # Root node doesn't have a parent
        print(f"{parent_name} -- {node.val} == {current_percentage:.2f}%")
   #this is formatted string f"..{} .." 
    # Recurse for each child
    for child in node.children:
        print_tree(child, node.val, current_percentage)

# Example Usage
if __name__ == "__main__":
    # Create the tree
    A = TreeNode('A', 100)  # Root node, ownership starts at 100%
    B = TreeNode('B', 50)
    D = TreeNode('D', 50)
    G = TreeNode('G', 10)

    # Build the relationships
    A.add_child(B)
    B.add_child(D)
    D.add_child(G)

    # Print the tree
    print_tree(A, None, 100)  # Start with 100% ownership at the root


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
def findAllPaths(grid):
    if not grid:
        return []
    res = []
    ROWS, COLS = len(grid), len(grid[0])
    def backtrack(x,y, path):
        if x == ROWS -1 and y == COLS - 1:
            res.append(path.copy())
            return
        if x > ROWS or x < 0 or y < 0 or y > COLS or grid[x][y] == 0:
            return
        directions = [(1,0), (0,1)] #move down 1 position is (1,0) ; move right is (0,1)
        for d in directions:
            new_x, new_y = d[0]+x, d[1]+y
            if grid[new_x][new_y] == 1:
                path.append((new_x, new_y))
                backtrack(new_x, new_y, path)
                path.pop() #to explore new cells
    backtrack(0,0, [0,0])
    return res
#time complexity: O( number of paths * (m+n)) -> worst scenario: all cells are 1s and we have to go through every cell
#space complexity: O(number of paths * (m+n))

#Q5:
"""
https://leetcode.com/problems/gas-station/description/
gas station problem. with a twist:
The car can go backwards
The solution is to return the maximum distance traveled, rather than simply a boolean
"""
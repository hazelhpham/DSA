#Q1: Using principles of OOP, lets design the game of chess.


#Q2: write an algo that returns the last nth value of a given linked list


#Q3: flattening a tree

#Q4: Maze problem seeing if you can reach the end within n steps.
from collections import deque

def canReachEnd(maze, start, end, n):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
    queue = deque([(start[0], start[1], 0)])  # (row, col, steps taken)
    visited = set()
    visited.add(tuple(start))

    while queue:
        row, col, steps = queue.popleft()
        
        # If we've reached the end and the steps are within the limit
        if (row, col) == tuple(end) and steps <= n:
            return True
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, steps + 1))
    
    return False  # If we can't reach the end within n steps

# Example usage:
maze = [
    [0, 0, 0, 1],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [1, 0, 1, 0]
]
start = (0, 0)
end = (3, 3)
print(canReachEnd(maze, start, end, 5))  # Output: True


#Q5:
"""
and later a tree problem where you would simply use BFT or DFT with a counter. Next they schedule a «virtual onsite». One coding interview, again easy problem with maximum simultaneous meeting to count needed meeting rooms. First I had a wrong idea, implemented it. And later the interviewer pointed out an example where my code would be incorrect. I quickly fixed it and we talked a bit more about testing etc. This, together with the phone screen, were some really nice people I would say. Next the same day I had a system design interview. I needed to design an alerts system that notifies users about stock price change. Taking into account that there are a lot of alerts. Honestly comparing to their coding questions this one wasn’t asked right. No text to refer to, no nothing. I was told to “not think about load” and to “draw an overview", but then the interviewers would delve into details before I was finished. On this interview I felt the strongest communication barrier
"""

#Q6:
"""
pertaining to calendar management
"""

#Q7:
"""
Design a real-time chat application with one-one chat and group chat functionalities. 
Seamlessly scalable and fault tolerant. Real-time delivery and persist messages required.
"""

#Q8:
"""
Generate a book glossary by calculating each word how many times has been repeated and in which pages is present
"""

#Q9:
"""
Implement double linked list in any language of choice
"""

#Q10:

"""
 finding the time range of when banks will close.
"""

#Q11:
"""
Given an 2D matrix, find the matrix cell with the maximum number of matrix cells that can be travelled from that cell. You can only move right, left, up and down. You can move until you reach an end of the matrix or an obstacle. Obstacles are stated as 'X', free cells are empty.
"""


#Q12:
"""
Final round coding - max overlapping meetings
"""
import heapq

def maxOverlappingMeetings(intervals):
    if not intervals:
        return 0

    events = []
    
    # Create events for all start and end times
    for interval in intervals:
        events.append((interval[0], 1))  # 1 represents start of a meeting
        events.append((interval[1], -1))  # -1 represents end of a meeting
    
    # Sort the events
    events.sort(key=lambda x: (x[0], x[1]))

    max_overlap = 0
    current_overlap = 0

    # Traverse the events and calculate overlaps
    for event in events:
        current_overlap += event[1]
        max_overlap = max(max_overlap, current_overlap)

    return max_overlap

# Example usage:
intervals = [[0, 30], [5, 10], [15, 20], [10, 15]]
print(maxOverlappingMeetings(intervals))  # Output: 3 (meetings overlapping between 5 and 15)

"""
Answer question
Question 3

Final round sys design - design & improve existing system for real-time stock market data from exchange to the customers
"""


#Q13:
"""

Calculate string length by using a recursion, check is a number sequence is a palindrome.
"""

#Q14:
"""
Given coins array and amount, find the minimum number of coins needed
"""

#Q15:
"""
Evaluate Division 
"""
"""
Second Interviewer asked me two questions; 
Given a list of integers return them in sorted order based on frequency, 
& String to Integer (ATOI) Both interviewers asked me about a difficult problem (could be technical or not) 
that I have faced recently, Also Why Bloomberg?
"""


#Q16:
"""
Matrix multiplication for a very sparse large matrices
"""
from collections import defaultdict

def sparse_matrix_multiply(A, B):
    """
    Multiplies two sparse matrices A and B.
    Input:
      A, B - Dictionaries where keys are (row, col) and values are the elements.
    Output:
      Resultant sparse matrix C in the same dictionary format.
    """
    # Check dimensions
    if not A or not B:
        return {}

    # Find dimensions of A and B
    max_row_A = max(row for row, _ in A.keys())
    max_col_B = max(col for _, col in B.keys())
    
    # Transpose B for easier access during multiplication
    B_transposed = defaultdict(list)
    for (row, col), value in B.items():
        B_transposed[col].append((row, value))

    # Resultant sparse matrix
    C = defaultdict(float)

    # Perform sparse multiplication
    for (i, k), val_A in A.items():
        if k in B_transposed:  # Check if column k of A exists in B
            for j, val_B in B_transposed[k]:
                C[(i, j)] += val_A * val_B

    return dict(C)
#Q17:
"""
Asked to determine the text of the most nested parentheses 
A(B(C)) -> C Find all routes between two given nodes (e.g. A, D): A -> B B -> C B -> D C -> D A, B, C, D A, B, D
"""


#q18:
"""
You are asked to make a program, that will get message packets out of order.
 Write a class that will correctly log the sequence in order and wait if a number in the sequence has not been logged yet
"""
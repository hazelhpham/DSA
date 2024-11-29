#Q1: Print out an adjacency list

#Q2: BFS on graphs

from collections import deque
from typing import List
# Function to return Breadth First Traversal of given graph.
def bfsOfGraph(self, adj: List[List[int]]) -> List[int]:
    res = []
    visited = set()
    visited.add(0)
    queue = deque([0])
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            res.append(node)
            for child in adj[node]:
                if child not in visited:
                    queue.append(child)
                    visited.add(child)
    return res

#Q3: DFS on graphs 
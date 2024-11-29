"""
CYCLE DETECTION
Given an undirected graph. The task is to check if there is a cycle
in a given graph. 
Input: V = 4, E = 4
Output: Yes 


1. using BFS:
- a visit set
- a queue 

basically just go thru each node like usual
then once we see them in the visit set -> we return False

2. using DFS
- if we encounter a visited vertex again, then we say, there is
a cycle
- we keep track of parent node [(node, and par) in Graph Valid Tree] 
in the DFS traversal and ignore the parent node from visited condition. 


Key Idea:
In an undirected graph, when traversing the graph (via DFS), every edge is bidirectional. This means:

If we visit a node u and traverse to its neighbor v, we must account for the fact that the edge (v, u) (back to the parent) will also be encountered during the traversal.
This back edge to the parent is not a cycle; it’s simply revisiting the previous node in the traversal.
To distinguish a true cycle from this backtracking behavior, we skip the parent node during the cycle check.
"""

#we are building an undirected graph
import collections


def build_graph(edges, graph):
    if not edges:
        return {None:None}
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    #no return because we are modifying in place
    #return graph
def detect_cycle_BFS(node):
    #BFS way 
    visit = set()
    queue = collections.deque([(node, -1)]) #(node, parent)
    while queue:
        node, parent = queue.popleft()
        #cycle is found
        if node in visit:
            return True
        visit.add(node)
        for nei in graph[node]:
            if nei != parent: #if child node == parent node --> cycle detected. 
                queue.append((nei, node))
    return False #no cycle is found
def detect_cycle_DFS(graph, node, visit, parent):
    visit.add(node)
    for nei in graph[node]:
#if there is no cycle -> we would dfs further
        if nei not in visit:
            detect_cycle_DFS(graph,nei,visit, node)
            return True
#The condition node == par can be skipped during cycle detection in an undirected graph because the edge connecting a node back to its parent is not a cycle.
        elif nei != parent: #cycle detected
            return True
    return False
edges = [(1,2), (2,3), (0,1), (0,2)]
graph = collections.defaultdict(list)
# 1 <-> 2
# 2 <-> 3
# 0 <-> 1
# 0 <-> 2
build_graph(edges, graph)
print(detect_cycle_BFS(1))
visit = set()
print(detect_cycle_DFS(1, graph, visit, -1))


#Leetcode questions that utilize Cycle detection: 
#Graph Valid Tree

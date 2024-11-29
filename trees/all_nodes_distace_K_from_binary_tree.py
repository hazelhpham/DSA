"""
Given the root of a binary tree, the value of a target node target, and an integer k, 
return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
"""

#turn this into a graph
#and we do bfs/dfs on it to find the list of values that k distance from targetted node

#this is how the tree node looks like: 
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 
from collections import defaultdict
from collections import deque
def build_graph(root , parent, graph):
    #remember, to build a graph k distance from node
    #traverse from parent -> root.left -> root.right
    if not root:
        return
    if parent:
        graph[root.val].append(parent.val)
        graph[parent.val].append(root.val)
    if root.left:
        build_graph(root.left,root,  graph)
    if root.right:
        build_graph(root.right,root, graph)

""""
              5
            /   \
           4    3
         /  \  /   \
        7   8  10   11 
    5 = [4,3]
    4 = [5,7,8]
    3 = [5, 10,11]
    7 = []
    8 = []
    10 = []
    11 = []
"""
from collections import deque, defaultdict

def bfs(target, k, graph):
    res = []
    visit = set([target])  # Start with the target node in the visited set
    queue = deque([target])  # Start the BFS from the target node
    level = 0  # Use level to track the current distance from target

    while queue:
        # Process all nodes at the current level
        for _ in range(len(queue)):
            node = queue.popleft()
            if level == k:
                res.append(node)  # Add node to result if its distance is k
            for nei in graph[node]:
                if nei not in visit:
                    visit.add(nei)
                    queue.append(nei)
        
        # If we have processed all nodes at the current level, increase the level
        if level == k:
            break  # No need to explore further after reaching level k
        level += 1
    
    return res
def dfs(node, visit, graph, parent):
    pass
#i think i missing checking on whether it is equal to parent node or not
graph = defaultdict(list)
target = 10
k = 2
target2 = 5
k2 = 3
parent = Node(5)
parent.left = Node(6)
parent.left.left = Node(10)
parent.right = Node(7)
parent.left.right = Node(12)
parent.right.left = Node(11)
parent.right.right = Node(14)
build_graph(parent, None, graph)
print(graph.values())
print("with target", target, "this will be the list of values,", bfs(target, k, graph), "that has distance equals to",k, "from the target" )
print("with target", target2, "this will be the list of values,", bfs(target2, k2, graph), "that has distance equals to",k2, "from the target" )

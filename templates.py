#BFS on GENERIC TREES that can have more than 1 children
from collections import deque
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.children = []
def bfs(root):
    if not root:
        return None
    queue = deque([root])
    res = []
    while queue:
        node = queue.popleft()
        #do something with node
        res.append(node.val)
        queue.append(node.children)
    return res

def dfs(root):
    if not root:
        return None
    #pre-order traversal
    #do something with root here
    print(root.val)
    for child in root.children:
        dfs(child)

#BFS on BINARY TREES: each node has at most 2 children: left and right
def dfsBinaryTree(root):
    if not root:
        return None
    #pre-order traversal
    #do something with root here
    print(root.val)
    dfs(root.left)
    dfs(root.right)
def bfsBinaryTree(root):
    if not root:
        return None
    queue = deque([root])
    res = []
    while queue:
        node = queue.popleft()
        #do something with node
        res.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res
#for graph, you have to have a visited set to keep track of
#visited nodes
def bfs_graph(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
def dfs_graph(graph, node):
    if visited is None:
        visited = set()
    if node in visited:
        return 
    visited.add(node)
    print(node)
    for neighbor in graph[node]:
        dfs_graph(graph, neighbor)
#dfs iterative using graphs
def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

#BFS/DFS on matrices
def bfs_matrix(matrix, start):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    visited = set()
    queue = deque([start]) #(row, col)
    while queue:
        r,c = queue.popleft()
        if (r,c) in visited:
            continue
        visited.add((r,c))
        print(matrix[r][c])
        for dr, dc in directions:
            new_r, new_c = dr+r, dc+c
            if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited:
                queue.append((new_r, new_c))
def dfs_matrix(matrix, r,c, visited = None):
    rows, cols = len(matrix), len(matrix[0])
    if visited is None:
        visited = set()
    if (r,c) in visited and not (0 <= r < rows and 0 <= c < cols):
        return
    visited.add((r,c))
    #process the current cell
    print(matrix[r][c])
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    for dr, dc in directions:
        dfs_matrix(matrix, r+dr, c+dc, visited)
def dfs_matrix_iterative(matrix, start):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0,1), (O, -1), (1,0), (-1,0)]
    visited = set()
    stack = [start]
    while stack:
        r, c = stack.pop()
        if (r,c) in visited:
            continue
        visited.add((r,c))
        print(matrix[r][c])
        for dr, dc in directions:
            nr, nc = dr+r, dc+c
            if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
                stack.append((nr,nc))

        
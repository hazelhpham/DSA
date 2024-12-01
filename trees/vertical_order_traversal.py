"""
         5 [0]
        /   \
      8[-1]    10[1]
    / \        / \  
[-2]9  11[-1] 13[0]  14[2]
-> [[9], [8,11],[5,13],[10], [14]]
"""
from collections import deque, defaultdict
def verticalOrder1(root):
    if not root:
        return []
    #use a default dict list instead
    d = defaultdict(list)
    queue = deque([(root, 0)]) #root and the current position = 0
    while queue:
        layer = []
        for _ in range(len(queue)):
            node, position = queue.popleft()
            layer.append(node.val)
            if node.left:
                queue.append((node.left, position-1))
            if node.right:
                queue.append((node.right, position+1))
        d[position].append(layer)
    d = sorted(d, key=lambda x:x[0])
    return d.values()
#time: O(N* logN)
#space: O(N)
#is there a more optimal solution for this? Yes!
# ----> you keep track of the min range and max range and append from min-range to max-range
#no need to use sort() function


from collections import deque, defaultdict

def verticalOrder2(root):
    if not root:
        return []
    
    column_table = defaultdict(list)  # To store nodes in each column
    queue = deque([(root, 0)])  # (node, column index)
    min_column, max_column = 0, 0  # To track the leftmost and rightmost column indices
    
    while queue:
        node, column = queue.popleft()
        column_table[column].append(node.val)
        
        # Update the min/max column index
        min_column = min(min_column, column)
        max_column = max(max_column, column)
        
        # Add children to the queue with updated column indices
        if node.left:
            queue.append((node.left, column - 1))
        if node.right:
            queue.append((node.right, column + 1))
    
    # Prepare the result by iterating through the columns in sorted order
    result = []
    for col in range(min_column, max_column + 1):
        result.append(column_table[col])
    
    return result

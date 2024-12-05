from collections import deque

class Solution:
    def isCompleteTree(self, root):
        if not root:
            return True  # An empty tree is complete

        null_node_found = False  # Tracks if a `None` node has been encountered
        queue = deque([root])  # Start BFS traversal with the root node

        while queue:
            node = queue.popleft()

            # If a `None` node is encountered
            if node is None:
                null_node_found = True
            else:
                # If a `None` node was encountered previously, and we now see a valid node,
                # the tree is not complete because valid nodes cannot appear after `None`.
                if null_node_found:
                    return False

                # Enqueue the left and right children for further processing.
                queue.append(node.left)
                queue.append(node.right)

        return True  # If we process all nodes without returning `False`, the tree is complete.

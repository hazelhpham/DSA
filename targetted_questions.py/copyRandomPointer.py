"""
No, you do not need a constructor for the Solution class in this 
case because your copyRandomListOptimal method does not rely on any instance-specific data or initialization.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None
class Solution:
    def __init__(self):
        self.visited = {}
    def getClonedNode(self, node):
        #recursive way
        #check if the node inside the visited map yet
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = Node(node.val)
                return self.visited[node]
        return None
    def copyRandomList(self, head):
        if not head:
            return head
        old_node = head
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node
        while old_node != None:
            new_node.random = self.getClonedNode(self, old_node.random)
            new_node.next = self.getClonedNode(old_node.next)
            #move one step ahead in the linked list 
            old_node = old_node.next
            new_node = new_node.next
        return self.visit[head]


            


    def copyRandomListOptimal(self, head):
        if not head:
            return None

        # Step 1: Clone nodes and interweave them with the original list
        ptr = head
        while ptr:
            new_node = Node(ptr.val)
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        # Step 2: Assign random pointers to the cloned nodes
        #remember, A --randomly---> C
        # A' ---randomly --> C'
        # copy_node.random --randomly---> original.random.next
        ptr = head
        while ptr:
            if ptr.random:
                ptr.next.random = ptr.random.next
            ptr = ptr.next.next

        # Step 3: Separate the original and cloned lists
        ptr_old_list = head
        ptr_new_list = head.next
        head_new = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            if ptr_new_list.next:
                ptr_new_list.next = ptr_new_list.next.next
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next

        return head_new

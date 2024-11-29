import collections
#THIS IS TREE
#BINARY TREE IS DIFFERENT TYPE OF REPRESENTATION

#BINARY TREE:
class Node:
    def __init__(self, x):
        self.x = x
        self.right = None
        self.left = None

#NON-BINARY TREE
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        #adding to children to self object 
        #-> that self will become the parent of this child
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level+=1
            p = p.parent
        return level
    #find parents of the node
    #if there is 1 parent -> depth = 1
    #if there are 2 parents -> depth = 2
    def print_tree(self):
        print(self.data)
        if self.children:
            for child in self.children:
                # print("the children of the node is",child.data)
                blank = child.get_level()
                print(blank * " ", end="")
                child.print_tree()
def main():
    node = TreeNode(10)
    node_child1 = TreeNode(9)
    node.add_child(node_child1)
    print("first print")
    node.print_tree()
    node_child2 = TreeNode(100)
    node.add_child(node_child2)
    print("second print")
    node.print_tree()
    print(node_child2.get_level())

main()
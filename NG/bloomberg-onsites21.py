# # Imagine we have a network of nodes where new information can be passed from one node to another node anaglous to how new gossip spreads 
# from one person to the next. In order for information to spread across the network, each node finds a node to pass down the latest info or 
# gossip it knows and this process repeats til the information is consistent across all nodes. This gossiping communication is one way a distributed 
# system can reach consensus on information the network holds without seeing all the data available from all the nodes.
# Let's say we have a list of nodes each holding a unique positive integer and we'd like to use this method to reach a consensus on what the largest integer is. 
# A node can look like the following,
# struct Node
# {
#   int my_value;
#   int largest_value_i_know;
  
#   Node(int value)
#   {
#     my_value = value;
#     largest_value_i_know = value; //self, that's the only thing  it knows 
#   };
# };
# We will use a vector of nodes to represent the network and the goal is to implement a function like this:


# void find_largest_value(vector<Node>& nodes) 
# //prints out the consensus and number of rounds.
# Assumptions/ Hints by interviewer:
# You're given random neighbor assignments, 3 neighbors per node.
# You're given the assumption that this graph is fully connected.
# No messages are lost.


# Note:
# 1.How will you represent a single node? 
# //Define class and data structure and write methods.
# 2.How will you write data to ther nodes's buffer for propogation. 
# //One way could be each node will have its own arraylist as a buffer. 
# This arraylist is exposed to other nodes via a public method to append a value.
# At its core, the problem boils down to this:

# Goal: Find the largest number among a group of nodes, where each node initially knows only its own value.
# Method: Each node can share ("gossip") the largest value it knows so far with its neighbors. Over time, the largest value spreads throughout the network.
# Here’s the simplified breakdown:

# Nodes:
# Each node holds two pieces of information:
# Its initial value.
# The largest value it has learned so far (starts as its own value).
# Connections:

# Nodes are connected in a graph-like structure.
# Each node knows which other nodes are its neighbors and can share information with them.
# Gossiping:

# A node tells its neighbors the largest value it knows.
# Neighbors update their knowledge if the value they receive is larger than what they know.
# Process:

# Repeat the gossiping process for a few rounds (iterations).
# By the end, every node will know the largest value in the network.
# Output:

# Print the largest value that all nodes have agreed on and the number of rounds it took.


class Node:
    def __init__(self, value):
        self.value = value
        self.max_value = value
        self.neighbors = []  # Neighboring nodes
    
    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
    
    def gossip(self):
        for neighbor in self.neighbors:
            neighbor.receive_gossip(self.max_value)
    
    def receive_gossip(self, value):
        self.max_value = max(self.max_value, value)

def find_largest_value(nodes, max_rounds=5):
    rounds = 0
    while rounds < max_rounds:
        for node in nodes:
            node.gossip()
        rounds += 1
    
    # Check if consensus is reached
    consensus_value = nodes[0].max_value
    all_agree = all(node.max_value == consensus_value for node in nodes)
    
    print(f"Largest Value: {consensus_value}")
    print(f"Consensus Reached in {rounds} Rounds: {all_agree}")

# Example Network
node_a = Node(3)
node_b = Node(5)
node_c = Node(2)
node_d = Node(9)

# Create a fully connected graph
node_a.add_neighbor(node_b)
node_a.add_neighbor(node_c)
node_a.add_neighbor(node_d)
node_b.add_neighbor(node_a)
node_b.add_neighbor(node_c)
node_b.add_neighbor(node_d)
node_c.add_neighbor(node_a)
node_c.add_neighbor(node_b)
node_c.add_neighbor(node_d)
node_d.add_neighbor(node_a)
node_d.add_neighbor(node_b)
node_d.add_neighbor(node_c)

# List of nodes
nodes = [node_a, node_b, node_c, node_d]

# Find largest value
find_largest_value(nodes, max_rounds=5)

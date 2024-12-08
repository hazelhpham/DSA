# Q1:
# n a Retail Inventory Management Alice went to buy products from an inventory in a retail mart. Each inventory has various products, 
# all with varying weights. Alice decides to use a scooter that can pick up three products at a time. The products in each inventory are 
# lined up in a single row, and Alice indexes them from 0 to n−1, starting from the first product to the n th product in the row. 
# In each selection, Alice picks the lightest remaining product in the inventory with weight w and uses the scooper to pick up that product 
# along with the two other products adjacent to it. Alice repeats this process until there are no more products left in the inventory. Alice wants to find the sum of the weights of the lightest products which can be chosen in every selection. Note: If there are two products with the lightest weight at different indexes, Alice chooses the product at the smallest index. If the product only has one other product adjacent to it, then the product itself and the single adjacent product will be removed. Example Let there be n=4 products in the inventory with weights represented by weights =[4,3,2,1]. First, choose the minimum weight (i.e., 1) and add that weight up to the total. The products with weights 2 and 1 are removed. The array of products is now [4,3]. - Then, choose the minimum weight from the remaining products (i.e., 3) and add that weight up to the total. The products with weights 3 and 4 are removed, and now there are no more products in the inventory. Hence, the total is 1+3=4. Function Description Complete the function findTotalWeight in the editor below. findTotalWeight has the following parameter: products: the array of integers denoting the weights of the products in the inventory Returns int: an integer denoting the sum of minimum weighted products at each selection. Constraints - 3≤w≤2000 - 3≤ length of products ≤2000 - 1≤ products [i]≤10


# Another example would be [6,4,9,10,34,56,54] and output is 68. 
# to explain it in a bit more detail 4 is the smallest weight, so we add 4 
# to thhe sum and remove it's adjacent numbers 6 and 9 from the list, 
# in the next iteration we look at numbers 10, 34 and 10 is thhe smallest 
# so we add 10 to the sum and remove 34 and next iteration we look at 56 and 54 and 54 is the smaller number so we add 54 to the sum and remove 56 so the total sum = 68



#Q2:
"""
Onsite:
Interview 1: Deep Copy stuff and pretty challenging follow ups, it isn't enough to go thru the tagged questions and know one solution, 
make sure you know all solutions as well as think about follow ups they may ask such as how a change in the input data structure could affect your solution.
"""
"""
Interview 2: Simpler questions but still had to dicuss multiple approaches.
Simple question involving creating a graph and then seeing if there was a path from A -> B. 
Second question was a dp problem involving coins.
"""


#Q3:
"""
Given a list of banks with opening times, and a time interval for trading. Determine if you can tradewith any banks during the given interval. E.g


00:00 - 08:00 Bank of America
12:00 - 17:00 Swiss Bank
18:00 - 23:00 Goldman Sachs


Example 1
06:00 - 10:00 FAIL
Because no bank is open from through out the interval 06:00 - 10:00


Example 2
13:00 - 17:00 SUCCESS
Because Swiss Bank is open from 13:00 - 17:00
"""

#Q4:
"""
Design a stock alert system. A client enters some stock and a thresold they want to receive alerts on. 
Design a system that notifies the client when this threshold is met.
"""

#Q5:
"""
Manager round. Design a system that allow users to retrieve stock info as fast as possible.
"""

#Q6:
"""
- They were very open ended questions about optimizing query time for a bloomberg specific terminal function, 
and another one about designing a help system so that respondents can take care of problems if a part of the terminal/product crashes.
"""

#Q7:
"""
- How would you implement autocomplete in a browser? 
- Whats the Data Structure and Algorithm?
"""
print("Question: How would you implement auto-complete in a browser? ")
print("Answer: I would use Dictionary/Hash Map or probably a trie.")
"""
********** DATA STRUCTURE DEFINITION *********
- A trie = a tree-like data structure that stores strings where nodes represent 
characters. It's particularly efficient for searching prefixes because it allows us to traverse
the structure character by character. 

Advantages: 
1. Autocomplete suggestions for a prefix can be found in O(k). where k is
the length of the prefix. 
2. Compact representation: Words with common prefixes share nodes, saving memory. 
3. Easily extendable: Adding or removing words is straightforward. 
- A dictionary is fine; a hash map could be used to map prefixes to a list of possible
completions. However, this approach may consume more memory since prefixes would need
to be explicitly stored. 
"""
"""
********* ALGORITHM ***********
1. Build a trie: 
- insert word from dataset -> into the trie. 
- optionally, store metadata at each node (e.g: word freq for ranking suggestions)
2. search for prefix:
- traverse the trie node by node, following chracters of the input 
prefix. 
- once the prefix is found, retrieve all words that brnach out from that
node using DFS / BFS. 
3. rank suggestions
- rank suggestions based on criteria such as word freq, relevance, or recency

"""
#Q8:

"""
  System Design (1 hour):
  	Some version of the top-k stock trades by Volume and Value.
  	Discussed several algorithmic approaches
  	Deployment discussion.
  	Functional requirements: Api end points, return types, user types
  	Non Functional requirements: Real time? Latency, expected throughput, traffic, etc
"""
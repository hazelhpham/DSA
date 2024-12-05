#Q13: Develop an add method that adds a currency relation between 2 currencies (like USD and AUD) and 
# then a get method that gets the value of any one currency from any other currency. 
# So you can add USD to AUD and then add AUD to EUR, then maybe you query USD to EUR and 
# it tells you how much EUR it'd be.


"""
i will talk about how i will sovle this problem:
1. build an adjacency list and it would be a bi-directional list 
(USD) <--0.5--> (AUD)
(AUD) <---2---> (USD)

so now i have to turn a list into a graph of nodes connecting towards each other.
the edges would be val = a and the reverse way would be 1/a

and then i would do bfs on the graph to find the "shortest" path
2. 
"""
from collections import defaultdict
class Node():
    def __init__(self, val):
        self.val = val
        self.children = []
class CurrencyExchange():
    def __init__(self):
        self.graph = defaultdict(list)
# ce.add("USD", "AUD", 1.5)  # 1 USD = 1.5 AUD
# ce.add("AUD", "EUR", 0.75)  # 1 AUD = 0.75 EUR
    def add(self, from_curr, to_curr, rate):
        self.graph[from_curr].append((to_curr, rate))
        self.graph[to_curr].append((from_curr, 1/rate))
    def exchange(self):
        pass
        

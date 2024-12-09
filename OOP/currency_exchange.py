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
from collections import defaultdict, deque

class CurrencyExchange:
    def __init__(self):
        self.graph = defaultdict(list)

    def add(self, from_curr, to_curr, rate):
        # Add bidirectional edge
        self.graph[from_curr].append((to_curr, rate))
        self.graph[to_curr].append((from_curr, 1 / rate))

    def exchange(self, start, end):
        # If start or end currencies do not exist, return -1
        if start not in self.graph or end not in self.graph:
            return -1
        
        # BFS setup
        queue = deque([(start, 1.0)])  # (current currency, cumulative rate)
        visited = set()

        while queue:
            current, rate = queue.popleft()
            if current == end:
                return rate
            
            visited.add(current)

            # Explore neighbors
            for neighbor, edge_rate in self.graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, rate * edge_rate))
        
        # If no path found, return -1
        return -1

        

#Question 40:
# Design AutoComplete search feature LC Medium
# A problem Graph and Tree

#Question 41:
#Question on balanced brackets


#Question 43: Time bases key value cache

#Question 44: Give some routes, print all the paths from start airport to destination airport.



#Question 47:
"""
study tagged past 3 months that’s what got me my full correctness on the onsite

i think what went wrong was some minor problems writing some of the code like trying to add a graph node to 
my visited set just before checking whether my node was visited lol
 (idk why it caused a rejection cuz i fixed it without the interviewer needing to tell me)

"""

#Question 48: Coin change

#Question 49:
# 1. BST in min-max fashion 
# Onsite: 
# 1. Variation of Insert Delete GetRandom O(1) on a different class (OOP style) 
# 2. System Design on browser history


#Question 50: design a subway class that has a method to get the average passing time between 
# 2 stations in a time complexity O(1)


class Subway:
    def __init__(self):
        # Dictionary to store total travel time between stations
        self.times = {}
        # Dictionary to store the count of trips between stations
        self.counts = {}

    def add_trip(self, start: str, end: str, time: int) -> None:
        # If the start station is not in times, initialize it
        if start not in self.times:
            self.times[start] = {}
            self.counts[start] = {}
        # If the end station is not in the dictionary for the start station, initialize it
        if end not in self.times[start]:
            self.times[start][end] = 0
            self.counts[start][end] = 0
        
        # Update the total travel time and the count of trips
        self.times[start][end] += time
        self.counts[start][end] += 1

    def get_average_time(self, start: str, end: str) -> float:
        # If no trips have been made from start to end, return 0 (no average)
        if start not in self.times or end not in self.times[start]:
            return 0.0
        # Calculate and return the average time
        total_time = self.times[start][end]
        trip_count = self.counts[start][end]
        return total_time / trip_count

# Example Usage:
subway = Subway()
subway.add_trip("StationA", "StationB", 10)
subway.add_trip("StationA", "StationB", 20)
subway.add_trip("StationA", "StationC", 15)

# Get average time between StationA and StationB
print(subway.get_average_time("StationA", "StationB"))  # Output: 15.0

# Get average time between StationA and StationC
print(subway.get_average_time("StationA", "StationC"))  # Output: 15.0

# Get average time between StationB and StationC (no trips)
print(subway.get_average_time("StationB", "StationC"))  # Output: 0.0

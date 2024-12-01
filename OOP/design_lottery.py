# Design a lottery system that returns a winner at random
"""
we would have a data structure for a list of people who participate. 
each person with an unique ID? we can store that based on a specific order
1 - first person who buys lottery
2 - second 
3 - third
etc
n - n people
and we would int(random(n)) to pick a random winner 
-> O(n)

if we want the getRandom() function to be O(1) 
-> choice(list)

list of indices= [1,2,3] ---> push into this list of people: push() O(1)
dic of people = {1:peopleA, 2:peopleB, 3:peopleC} 
and for getRandom():
    rd = choice(list_indices)
    return dic[rd] 
"""
from random import choice

class LotterySystem:
    def __init__(self):
        # List to store indices of participants
        self.list = [] 
        # Dictionary to store index -> person's name
        self.d = {}

    def addPeople(self, personName):
        # Add a person to the system with a unique index
        index = len(self.list)  # The new person's index is the current size of the list
        self.d[index] = personName
        self.list.append(index)  # Append the index to the list
        return True  # Confirmation that person is successfully added

    def getRandomPerson(self):
        # Handle the case where there are no participants
        if not self.list:
            return None  # Or raise an exception if you prefer
        # Pick a random index and return the corresponding person's name
        rd = choice(self.list)
        return self.d[rd]
    
    def deletePerson(self, personName):
        index = -1
        #we have to go and find the index of person's name to delete 
        for key, val in self.d.items(): #O(n) ? #if i were given an ID, then this would be O(1)
            if personName == val:
                index = key
                del self.d[key] #O(1)
        #delete from the list O(1)
        if index != len(self.list) - 1:
            self.list[index], self.list[-1] = self.list[-1], self.list[index]
        self.list.pop() #O(1)

        
        



# Time Complexity:
# addPeople(): O(1) because appending to the list and adding to the dictionary both take constant time.
# getRandomPerson(): O(1) because choice() is O(1) for randomly selecting an element, and dictionary lookup by key is also O(1).
# Space Complexity:
# O(n), where n is the number of people added to the lottery system. You store n elements in the list and the dictionary.
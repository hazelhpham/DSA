# Q1: 
# How to optimally employ ships to deliver shipping containers 
# of different weights in a specified number of days.
# ---> bin packing problem
# Example Usage

def schedule_ships(containers, ships, days):
    # Sort containers by descending weight
    containers.sort(reverse=True)
    
    # Prepare a list of ships and their schedules
    ship_schedule = {i: [] for i in range(len(ships))}
    ship_capacity = ships[:]  # Copy ship capacities
    
    # Assign containers to ships
    for container in containers:
        assigned = False
        for i, capacity in enumerate(ship_capacity):
            if container <= capacity:
                ship_schedule[i].append(container)
                ship_capacity[i] -= container
                assigned = True
                break
        if not assigned:
            return f"Cannot schedule all containers within {days} days."
    
    # Check if scheduling is possible within the given days
    total_trips = sum(len(schedule) for schedule in ship_schedule.values())
    if total_trips > days * len(ships):
        return f"Scheduling not possible within {days} days."
    
    return ship_schedule
containers = [10, 15, 20, 25, 30, 5]
ships = [50, 60, 70]  # Ship capacities
days = 2

result = schedule_ships(containers, ships, days)
print("Ship Schedule:", result)

#Q2: Min stack
class MinStack:
    def __init__(self):
        self.stack = []      # Main stack to store all elements
        self.min_stack = []  # Auxiliary stack to store the minimum elements

    def push(self, val: int) -> None:
        # Push value onto the main stack
        self.stack.append(val)
        
        # Push the minimum onto the min stack
        # If min_stack is empty or val <= current minimum, update min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Remove and return the top element from the main stack
        if self.stack:
            val = self.stack.pop()
            # If the popped value is the current minimum, pop it from min_stack
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        # Return the top element of the main stack
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        # Return the top element of the min stack (current minimum)
        return self.min_stack[-1] if self.min_stack else None

#Q3: How to implement a shuffle linked list
import random
class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next 
    def shuffleLinkedList(head):
        if not head:
            return None
        
#Q4: build a stock class where you can get the last stock added to portfolio
class StockPortfolio:
    def __init__(self):
        self.portfolio = []  # Use a list as a stack to store stock names

    def add_stock(self, stock_name: str):
        """
        Add a stock to the portfolio.
        :param stock_name: Name of the stock to add.
        """
        self.portfolio.append(stock_name)
        print(f"Added stock: {stock_name}")

    def remove_stock(self):
        """
        Remove the last stock added to the portfolio.
        """
        if self.portfolio:
            removed_stock = self.portfolio.pop()
            print(f"Removed stock: {removed_stock}")
            return removed_stock
        else:
            print("Portfolio is empty. No stock to remove.")
            return None

    def get_last_stock(self):
        """
        Get the last stock added to the portfolio without removing it.
        :return: The last stock added, or None if the portfolio is empty.
        """
        if self.portfolio:
            return self.portfolio[-1]
        else:
            print("Portfolio is empty.")
            return None

    def show_portfolio(self):
        """
        Display the current portfolio.
        """
        print("Current Portfolio:", self.portfolio if self.portfolio else "Empty")

# Example Usage
if __name__ == "__main__":
    portfolio = StockPortfolio()

    # Add stocks
    portfolio.add_stock("AAPL")
    portfolio.add_stock("GOOGL")
    portfolio.add_stock("AMZN")

    # Show portfolio
    portfolio.show_portfolio()

    # Get the last stock added
    print("Last Stock Added:", portfolio.get_last_stock())

    # Remove the last stock
    portfolio.remove_stock()

    # Show portfolio after removal
    portfolio.show_portfolio()

#Q5: depth first search for a binary tree that had no limit of leaves for each level.
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # List to hold any number of children

def dfs_recursive(node):
    if not node:
        return
    
    print(node.value)  # Process the current node
    for child in node.children:
        dfs_recursive(child)


#Q6: 
# make a wordle app in python, 
import random

def load_word_list():
    # Replace with a larger dictionary for a real game
    return ["apple", "grape", "brick", "stone", "charm", "brain"]

def generate_feedback(guess, target):
    feedback = [""] * len(guess)
    target_counts = {}
    
    # First pass for correct positions (Green)
    for i, (g, t) in enumerate(zip(guess, target)):
        if g == t:
            feedback[i] = "🟩"
        else:
            target_counts[t] = target_counts.get(t, 0) + 1
    
    # Second pass for wrong positions (Yellow/Gray)
    for i, g in enumerate(guess):
        if feedback[i] == "":
            if target_counts.get(g, 0) > 0:
                feedback[i] = "🟨"
                target_counts[g] -= 1
            else:
                feedback[i] = "⬜"

    return "".join(feedback)

def play_wordle():
    word_list = load_word_list()
    target_word = random.choice(word_list)
    attempts = 6

    print("Welcome to Wordle! You have 6 attempts to guess a 5-letter word.")
    
    for attempt in range(attempts):
        while True:
            guess = input(f"Attempt {attempt + 1}/6: ").lower()
            if len(guess) == 5 and guess.isalpha():
                break
            print("Invalid guess. Please enter a 5-letter word.")
        
        feedback = generate_feedback(guess, target_word)
        print("Feedback:", feedback)
        
        if guess == target_word:
            print("🎉 Congratulations! You guessed the word!")
            return
    
    print(f"Game over! The word was: {target_word}")

# Run the game
play_wordle()

# part 2 was to implement hard mode 
# round 3: a stack question and a tree question

#Q7:
# 1) If the word can be retrieved from the matrix 
# 2) Sort the words written with Welsh alphabet

#Q8: System design question to implement metropolitan with data structures and calculate the average time people entered and exited stations.


#Q9: How I should design a mobile application which stores videos and you can resume what you were watching after taking a pause.


#Q10: Design Bloomberg's terminal for news.


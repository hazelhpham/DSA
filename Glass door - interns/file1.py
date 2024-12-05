# Q1: 
# How to optimally employ ships to deliver shipping containers 
# of different weights in a specified number of days.


#Q2: Min stack

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


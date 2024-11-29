#Q1: 
# Next 45 mins: Coding question
# A TV show is "addictive" if the viewers quickly become addicted to the show and eventually finish watching the show. 
# It can be tracked after viewing how many episodes of a show at least 70% of the viewers who watched that continued on to finish the show entirely. In other words, more that 70% of the viewers who watched the first x eposides of a show continued on to finish the entire show. The x is what we are looking for.
# Assumptions:
# All shows have 10 episodes
# viewers always start from the first episode (no skipping).
# Given a log of entries consisting of a user id, the show name and the episode number that was watched, produce the x for each show.
# Sample Input:
# The following function is called for each log entry
# void process_log(string show, int episode, int user_id)
# Expected Output:
# void print_results();


#Q2:
"""
After I passed my phone interview with Bloomberg, they asked me to do an onsite interview (Similar to the phone interview due to COVID). Two interviewers were there. The first 10 minutes were talking about projects with the typical "Why Bloomberg" question. Then we went to the coding question:


Assume that you are designing a Browser history thingy. Say the user went into site "a" then "b" then "c". The history would be : c->b->a.
Now assume you went into "a" again: The result becomes a->c->b.
So the thing here is, if you revisit a site, you remove it from your result and so on.


If you think about it, this is pretty similar to LRU cache. All you need is a list (in c++ is a doubly linked list ), and an unordered map that maps every string to its iterator. You can now erase a string from the list in O(1) using the map and can add any new string to the front of the list. The whole operation takes O(1).


Some interesting questions that followed up :
1 - When to use reference in c++ and when not.
2 - Difference between public and private in classes.
3 - Is a function public or private in default in a class.
4 - The use of const.
5 - Some multithreading concepts.


What I get from this interview is that the interviewers really care about your knowledge of the language that you're using. It's not always the coding problem. The phone interview had the same process too.


The last 5 mins were free for me to ask any question to the interviewers.
"""


#Q3:
"""
https://leetcode.com/discuss/interview-question/1003903/Bloomberg-or-Onsite-or-Consensus-on-the-largest-integer-in-the-network
"""

#Q4: 
"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""

#Q5:

"""
I have an interview with bloomberg and met a non-leetcode problem.
The Input is given as a 2D matrix with True and False values, a interger variable n representing the number of iteration.
The output should print the pattern in n-th iteration. The iteration follow the following rules:


Each X representing a True Value and a Blank represents False. In n-th each iteration, the true value of (n-1)-th iteration will be replaced by a copy of entire n-1 iteration itself.


              XXX XXX XXX
			  X X X X X X
			  XXX XXX XXX
XXX           XXX     XXX
X X    ->     X X     X X      ->  ...
XXX           XXX     XXX
              XXX XXX XXX
			  X X X X X X
			  XXX XXX XXX

constraints?
"""

def generate_pattern(n):
    if n == 1:
        # Base pattern for n=1
        return [
            [True, True, True],
            [True, False, True],
            [True, True, True]
        ]
    
    # Recursive step
    prev_pattern = generate_pattern(n - 1)
    size = len(prev_pattern)
    new_size = 3 * size  # The new pattern is 3 times larger in both dimensions
    new_pattern = [[False] * new_size for _ in range(new_size)]
    
    # Fill the new pattern
    for i in range(3):
        for j in range(3):
            for x in range(size):
                for y in range(size):
                    if (i == 1 and j == 1):  # Middle section is blank
                        new_pattern[i * size + x][j * size + y] = False
                    else:
                        new_pattern[i * size + x][j * size + y] = prev_pattern[x][y]
    
    return new_pattern

def print_pattern(pattern):
    for row in pattern:
        print("".join("X" if cell else " " for cell in row))

# Example usage:
n = 3  # Number of iterations
pattern = generate_pattern(n)
print_pattern(pattern)

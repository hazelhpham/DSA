# Remove ints from an array.
# Example:
# Input: array = [-8, 3, -5, 1, 51, 56, 0, -5, 29, 43, 78, 75, 32, 76, 73, 76], 
# ranges = [[5, 8], [10, 13], [3, 6], [20, 25]]
# Output: [-8, 3, -5, 29, 43, 76, 73, 76]


"""
https://leetcode.com/problems/design-underground-system
https://leetcode.com/problems/longest-substring-without-repeating-characters
https://leetcode.com/problems/trapping-rain-water
https://leetcode.com/problems/two-city-scheduling/
https://leetcode.com/problems/add-two-numbers-ii
https://leetcode.com/problems/word-search-ii
"""

"""
Measure TV Show Addictiveness
Problem Statement:
One way to measure how "addictive" a TV show is to look at the number of viewers who finish a show after watching a certain number of episodes. We want to find the nth episode such that 70% of the viewers of the nth episode will continue to watch all episodes of the show. The lower the value of n, the more addictive the show is.


We can assume that all shows have 10 episodes and all viewers watch the episodes sequentially without skipping. Given a log of entries consisting of:


user_id: an integer representing the viewer's ID.
show_name: a string representing the name of the show.
episode_number: an integer representing the episode number the user watched.
You need to find n for each show.


You can assume this function is called for each log entry.


Function Signature:
void process_log(string show, int episode, int user_id);
void print_results();
Input:
The process_log(string show, int episode, int user_id) function is called for each log entry to process the viewing data.
After processing all log entries, the print_results() function is called to calculate and print the results.


Output:
The print_results() function should output the earliest episode n for each show where at least 70% of viewers continue watching until the last episode. If no such episode n is found for a show, it should indicate this.


Example usage
int main() {
    process_log("Breaking Bad", 1, 1001);
    process_log("Breaking Bad", 2, 1001);
    process_log("Breaking Bad", 3, 1001);
    process_log("Breaking Bad", 10, 1001);
    process_log("Breaking Bad", 1, 1002);
    process_log("Breaking Bad", 2, 1002);
    process_log("Breaking Bad", 1, 1003);
    process_log("Breaking Bad", 2, 1003);
    process_log("Breaking Bad", 3, 1003);
    process_log("Breaking Bad", 4, 1003);
    process_log("Breaking Bad", 5, 1003);
    process_log("Breaking Bad", 6, 1003);
    process_log("Breaking Bad", 7, 1003);
    process_log("Breaking Bad", 8, 1003);
    process_log("Breaking Bad", 9, 1003);
    process_log("Breaking Bad", 10, 1003);

    process_log("Game of Thrones", 1, 2001);
    process_log("Game of Thrones", 2, 2001);
    process_log("Game of Thrones", 3, 2001);
    process_log("Game of Thrones", 4, 2001);
    process_log("Game of Thrones", 5, 2001);
    process_log("Game of Thrones", 1, 2002);
    process_log("Game of Thrones", 2, 2002);
    process_log("Game of Thrones", 3, 2002);
    process_log("Game of Thrones", 4, 2002);
    process_log("Game of Thrones", 5, 2002);
    process_log("Game of Thrones", 6, 2002);
    process_log("Game of Thrones", 7, 2002);
    process_log("Game of Thrones", 8, 2002);
    process_log("Game of Thrones", 9, 2002);
    process_log("Game of Thrones", 10, 2002);

    print_results();

    return 0;
}
Constraints:
show_name consists of lowercase English letters and spaces.
episode_number is an integer between 1 and 10.
user_id is an integer.
The log size can be up to 100,000 entries.
"""


"""
https://leetcode.com/problems/non-decreasing-array/description/
greedy
"""

"""
https://leetcode.com/problems/design-an-ordered-stream/description/
"""
class OrderedStream():
    def __init__(self, capacity):
        self.capacity = capacity 
        self.array = [None] * self.capacity
        self.pointer = 0
# capacity = 5
# insert 2
# 
    def insert(self, id, value):
        #convert id from 1-indexed to 0-indexed
        index = id - 1
        #insert the value at the correct index
        self.array[index] = value
        #if the pointer isnt at this index, 
        #return an empty list
        if index != self.pointer:
            return []
        result =  []
        while self.pointer < self.capacity and self.array[self.pointer] is not None:
            result.append(self.array[self.pointer])
            self.pointer+=1 #move the pointer forward
        return result 




"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
Given a linked list with 2 extra pointers backward and forward, 
return a boolean if the linked list is valid. 
A valid LL is when the backward pointer points to a node before it and the forward pointer points to a node after it.
"""

"""
https://leetcode.com/problems/min-stack/
"""

"""
Given a collection of intervals, 
return a maximal set of non-overlapping intervals while prioritising the longer intervals.

- sort the intervals: sort based on their length (long interval first) 
and then by their start time
- greedy selection
"""
def maxNonOverlappingIntervals(intervals):
    intervals = sorted(intervals, key = lambda x:(-x[1]+x[0], x[0]))    
    result = []
    last_end = -float("inf")
    for start, end in intervals:
        if start >= last_end:
            result.append((start,end)) #select the interval
            last_end = end #update the last end to this interval
    return result
intervals = [[1,10], [2,5], [4,9], [5,11], [1,100]]
print(intervals)
print(maxNonOverlappingIntervals(intervals))
"""
2nd Interview-
https://leetcode.com/problems/all-paths-from-source-to-target/ 
[The given graph can have cycles though]
https://leetcode.com/problems/valid-parentheses/
"""


"""
Example :
string1 = "ABBK"
string2 = "DBCN"
dictionary = {"DBPN", "ABPN", "ABKK", "ABPN", "DCCN", "ABPK" }


Answer = 4
{ABBK -> ABPK -> ABPN -> DBPN -> DBCN } -> total 4 conversions required.
"""

"""
A linked list of cards are given. Write a code, to Shuffle the cards, without using inbuilt shuffle / random functions.
Functionalities :


Create a deck of card through linked list
Split the deck of cards randomly into 2 subsets
Merge the subsets randomly , so that previous order is not maintained
Display the deck of cards .
Eg:
I/p Cards: [A,4,6,7,9,K,Q,J,2]
Expected Output:
Create Linked List : [A->4->6->7->9->Q->J->2]
Split List into 3 decks : A->4->6->7 9->Q J->2
Merge the decks randomly : 9->6->7 ->Q ->J->2->4->A


Similiar Problem : [ Interviewer asked to solve using linked list ] https://leetcode.com/problems/shuffle-an-array/
"""


#https://leetcode.com/problems/allocate-mailboxes/description/
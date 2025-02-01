#Question 1
# Print the top 10 largest elements from integer array. 
# Follow up to top K
def topElements(arr):
    pass
#first implement solution for top 10

#follow-up: top K --> use Heap 


#time complexity:
#space complexity:

# *********************************************************************************************************
# Question 2
# Given a string, rearrange it in decreasing order by the characters frequency and in lexicographical order if their frequency is equal.
from collections import Counter
def orderString(s):
    if not s:
        return ""
    count = Counter(s)
    count = sorted(count.items(), key= lambda x:(-x[1], x[0]))
    #sorted_data = sorted(data, key=lambda x: (-x[1], x[2], x[0]))
    # ---> you sort based on firstly, the first element of tuple, then 2nd element in tuple
    #then 3rd element in tuple. 
    #SO, the first element from tuple will be prioritized first, then 2nd, then 3rd. 
    """
    ebbaa
    b - 2
    a - 2
    e - 1
    """
    string_builder = []
    for key, val in count.items():
        string_builder.append(key*val) # bbaae
    return ''.join(string_builder)
                

# Question 3
# Given a large string (a book) and a list of words (unique words), 
# print all occurences **WHERE ALL THE WORDS** (not 1 at a time) appear consecutively in the string. 
# (the order does not matter, but need to be all from the list and having no other words between them). 
# Example:
# s: "This is a test is. other a" 
# words: ["is", "a", "test"] 
# OUTPUT: 1,2
def find_consecutive_occurrences(s, words):
    from collections import Counter

    # Split the string into words
    string_words = s.split() #ok
    word_count = len(words) #ok
    word_set = set(words) #ok, you have put into the set to avoid duplicates 
    word_frequency = Counter(words)  # Frequency of words in the list

    result = []
    n = len(string_words)

    for i in range(n - word_count + 1):
        # Check a window of size `word_count`
        window = string_words[i:i + word_count]
        window_count = Counter(window)

        # Check if the current window matches the word list
        if window_count == word_frequency:
            result.append(i)

    return result


# Example usage
string = "This is a test is other a"
words = ["is", "a", "test"]

print(find_consecutive_occurrences(string, words))

# Question 4

# Consider the browser search where you type an URL. 
# You need to keep track of the history and to print the most recent URLs the user searched. 
# More or less LRU cache.
# ---> i keep the URL in a node. 

# Question 5
# Custom Index Engine
# Design and implementation


# Question 7:
# 7.1 : Given a matrix filled with different integers and an entry point, 
# count the number of connected points (adjacent up, down, left, right) 
# with the same value as the entry point. 

# 7.2: Box stacking problem without rotating sides. 
# Do it using DP. Find all paths from a source to destination in a graph


#Question 8:
#Input: (1, "abcd"), (2, "efgh"), (4, "mnop"), (5, "qrst"), (3, "ijkl")
# Write a program to output the data from the stream in realtime in order, so 1,2,3,4,5..
# You cannot queue up the incoming data from the stream.
# So for example if the first incoming bit of data is (1, "abcd"), 
# and the second is (4, "mnop"), you cannot output (4, "mnop") until you get 2, 3.

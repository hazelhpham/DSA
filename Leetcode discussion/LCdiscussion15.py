#Q1: https://leetcode.com/problems/non-decreasing-array/description/

#Q2: 
"""
INPUT: given 2 character arrays as shown below
p1 = ['A', 'B','C','E','G','D','B']
P2 = ['A', 'B','A','C','E']


OUTPUT:
part1: Give the intersection: ['A', 'B','C','E'] he didnt specify if it has to be in sorted order, just the intersection.


part2: Give the characters sorted by frequency: ['A','B','C','E','G','D'] no need to sort lexicographically if the frequencies are same, just any order is fine


I was able to solve it using dictionary and sorting with time: O(nlogn) but then he asked me to solve it in O(n) and so I solved it using bucket sort.


He said memory will be wasted if count of some character is too big, i couldnt optimize it further as it was almost time.
You can use heap to sort the frequency of the character since there are only maximum 26 characters => it takes O(26log26) to extract the data from the heap and store it. 
The final time and space complexity is still O(n) but it can avoid 
wasting memory if the frequency array is spare and potentially run faster than bucket sort. 
But in my opinion, bucket sort is good enough since we need the same amount of memory to store the frequency in the first place, 
he just nitpicking some constant factor here. In practice it is true that we can run out of memory but this is just a new grad interview ...

Because OP mentions a dictionary, I assumed this (char, freq) mapping was there and it was sorted that way and the interviewer was unhappy with that. 
In that case, yes the complexity is AlogA where A is the size of the alphabet, and 26log26 looks really great. 
I do not understand why anyone would be unhappy with that. The interviewer might follow up though to the case where alphabet is large so you need to improve again.



You are right that they are no difference if OP created tuple with frequency and character then sorting by frequency but I think OP did not notice it and said O(NlogN) where N is the length of the string. 
And the interviewer may not fully understand as well. Hence the miscommunication from both side.



how is this any different than OPs first approach? You can as well just sort it once (like he did) and in that case it was nlogn (26log26) too.
"""
from collections import Counter

def intersection(p1, p2):
    count1 = Counter(p1)  # count frequencies in p1
    result = []

    for char in p2:
        if count1[char] > 0:  # if char exists in p1
            result.append(char)
            count1[char] = 0  # Avoid adding duplicates to the result

    return result
from collections import Counter

def sort_by_frequency(p1):
    # Step 1: Count frequencies of characters
    count = Counter(p1)

    # Step 2: Create frequency buckets
    max_freq = max(count.values())
    buckets = [[] for _ in range(max_freq + 1)]

    for char, freq in count.items():
        buckets[freq].append(char)

    # Step 3: Gather characters based on frequencies (order by frequency)
    result = []
    for i in range(max_freq, 0, -1):  # Start from highest frequency
        for char in buckets[i]:
            result.extend([char] * i)  # Add character i times to the result
    
    return result

#Q3: Design underground system
#Q4: Valid palindrome II

#Q5:
"""
Bit Manipulation and the other was related to String
"""
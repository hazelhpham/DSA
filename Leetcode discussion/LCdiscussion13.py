# Q1:
# Given an array of stock prices, return the range within k days (each index in array is stock price for day).
# Above was what we worked with along with some scratch code as it seemed simple enough and he agreed with. The problem came with the follow up, he asked what if the stock array was updated everyday, how could we improve the time complexity? I could not for the life of me figure it out and eventually he told me that we could use a BST to find the lowest and the max in O(1) time (we can use set in c++ as it is implemented as a BST). Since inserting an entry would only be O(log n), the total time complexity would be O(k log n) rather than O(k n) (because we call our O(n) scan, k times)


# I actually think I did good in the whole interview except this part, I spaced out and accidently said that I forgot what a BST was LMAOO.


# https://leetcode.com/problems/validate-binary-search-tree/
# This one was very straight forward.


#Q2:
"""
Round 2:
Interviewer was a little straight forward but still nice. Same format, 10 minute resume lookover then technical. He only asked me one question.


Trending Stock
We mainly had discussion about the data structures used and really hammered down on the time complexity and how we could improve it. I decided to use one hash table for count, and a vector<vector> which would hold the frequent companies and pop off when we return. We ended up talking about this the majority of the time and I did not have the chance to code it out. A
fter the interview, he told me that I would definitely be contacted by HR the day of or the next.
"""

#Q3:
"""
You have a <Key, Value> structured input data for all objects
Where you have
Insert : O(1)
Lookup : O(1)
Delete : O(1)
You can traverse the added elements in the order they were inserted.
"""


#Q4:
"""
You are given a custome alphabets that could contain alphabets with two characters or three characters in one letter of the alphabets. sort the given strings lexicographicaly based on the custome alphabet.


custom_alphabet = {"A", "AA", "B", "CC", "D" "DE", "E", "TD", "F", "GAC" "GG", "HA", "II", "J", "KK", "L",  "MM", "N", "O", "P", "PL", "QQ", "R", "SS", "T", "UU", "V", "WW", "X", "YY", "Z"}
the list you are given to sort cantains strings formulated by the above alphabets.


Example 1:



given_list = [ "AAB", "AB"]

output = ["AB", "AAB"]
in the strings you have to give priority to letters in the alphabets with more characters like if there is "AA"in the string you should not say it is formed by twoAs instead consider it as one letter as"AA"since it exists in the alphabet.


was able to come up with anO(M*N) + O(Nlog(N))solution where M being the size of the strings and N being the size of the list. And the interviewer seemd to agree on the solution that I proposed and I am waiting for a feedback.
"""

#Q5:
"""
Given a collection of intervals, return a maximal set of non-overlapping intervals while prioritising the longer intervals.


input - (1,5),(2,7),(11,18)
output - (11, 18), (2, 7)


Any ideas?
"""

#Q6:
"""
What's the most efficient solution to implement the two below functions? Any ideas?


execute_trade(ticker,volume)
most_traded(n)
execute_trade('IBM',600)
execute_trade('NFLX',800)
execute_trade('AAPL',700)
execute_trade('AMZN',1000)
execute_trade('AAPL',400)
execute_trade('GOGL',1200)
most_traded(3)
GOGL 1200
AAPL 1100
AMZN 1000
most_traded(3)
most_traded(4)
most_traded(5)
"""


#Q7:
"""
Merge intervals
Given a buffer that contains multiple messages, parse the buffer and process each message.
When an exchange sends several messages over a TCP socket, they can be concatenated when performing the read. This is solved by parsing the buffer, and splitting in to multiple messages for each process call.
Please implement a packetize function that takes a constant char* and size_t:
void packetize(const char *data, size_t length);
This function can be a member function if necessary.
The packetize function should call a process function, with signature:
void process(const char *data, size_t length);


Given data buffer may contain incomplete packet, which may continue in the next call to packetize. At the same time, buffer may contain multiple packets as well, in which case all of the packets must be collected and process should be called for each one.
"""

#Q8:
"""
Phone Interview - Welch Dictionary
Onsite interview 1 - Given source and target print all paths .


I coded the solution in the onsite round and even answered the OOPS related question and how to optimise the code and the underlying implementation ragarding unordered map and ordered map with the time complexity.
Don't know where it went wrong. One problem that I had was that the accent of the interviewer was very thick so sommunication was a bit difficult.
"""

#Q9:
"""
You are given a list of stock exchange along with startTime and endTime in which these exchanges operate.
0 <= startTime, endTime <= 23


[
	['Exchange A', 2, 7], 
	['Exchange C', 11, 17], 
	['Exchange B', 9, 16],
	['Exchange D',14, 20]
]
Then, given a list of buy/sell orders which need to be executed in the given timeframe you need to find out what all orders can be served with atleast 1 exchange.


[
	['Order 1', '3', '6'],
	['Order 2', '9', '12'],
	['Order 3', '21', '22']
]
So in this case Order 1 and 2 can be served but 3 cannot be served by any exchange.


Follow-up = What if some exchanges operate from night to morning, ex - ['Exchange X', 23, 5]. Same thing with orders.
"""
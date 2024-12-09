# Q1:
# Given an array of stock prices, return the range within k days (each index in array is stock price for day).
# Above was what we worked with along with some scratch code as it seemed simple enough and he agreed with. 
# The problem came with the follow up, he asked what if the stock array was updated everyday, 
# how could we improve the time complexity? I could not for the life of me figure it out and eventually 
# he told me that we could use a BST to find the lowest and the max in O(1) time 
# Since inserting an entry would only be O(log n), 
# the total time complexity would be O(k log n) rather than O(k n) (because we call our O(n) scan, k times)

def stock_price_range(prices, k):
    result = []
    for i in range(len(prices)):
        start = max(0, i - k + 1)
        window = prices[start:i + 1]
        result.append((min(window), max(window)))
    return result

# Example
prices = [10, 20, 5, 15, 30, 25]
k = 3
print(stock_price_range(prices, k))
# Output: [(10, 10), (10, 20), (5, 20), (5, 15), (5, 30), (15, 30)]



# https://leetcode.com/problems/validate-binary-search-tree/
# This one was very straight forward.
def validateBinarySearchTree(root):
    if not root:
        return None
    def valid(root, left, right):
        if not root:
            return True
        if not (left < root.val < right):
            return False
        left = valid(root.left, left, root.val)
        right = valid(root.right, root.val, right)
        return left and right
    return valid(root, float("-inf"), float("inf"))
#Time complexity: O(n), n is the number of nodes. 
#Space complexity: O(logn) for balanced tree. O(n) is for skewed tree. 
#Q2:
"""
Round 2:
Interviewer was a little straight forward but still nice. Same format, 10 minute resume lookover then technical. He only asked me one question

Trending Stock
We mainly had discussion about the data structures used and really hammered down on the time complexity and how we could improve it. 
I decided to use one hash table for count, and a vector<vector> which would hold the frequent companies and pop off when we return.
We ended up talking about this the majority of the time and I did not have the chance to code it out. 
After the interview, he told me that I would definitely be contacted by HR the day of or the next.
"""
#stocks = [ [BB, 100], [BB, 100], [TSLA, 500], [GGLE, 1]]
import heapq
def trendingStock(stocks):
    if not stocks:
        return 0 #there is no trending stock at all
    d = {}
    for company, stock in stocks:
        if company in d:
            d[company]+=1
        else:
            d[company] = 1
    d = sorted(d.items(), key=lambda x:x[1])
    print(d[0]) #BB
#time complexity: O(n)
#space complexity: O(n)




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
You are given a custome alphabets that could contain alphabets with two characters 
or three characters in one letter of the alphabets. sort the given strings lexicographicaly based on the custome alphabet.
custom_alphabet = {"A", "AA", "B", "CC", "D" "DE", "E", "TD", "F", "GAC" "GG", "HA", "II", "J", "KK", "L",  "MM", "N", "O", 
"P", "PL", "QQ", "R", "SS", "T", "UU", "V", "WW", "X", "YY", "Z"}
the list you are given to sort cantains strings formulated by the above alphabets.
Example 1:
given_list = [ "AAB", "AB"]

output = ["AB", "AAB"]
in the strings you have to give priority to letters in the alphabets with more characters like if there is "AA"
in the string you should not say it is formed by twoAs instead consider it as one letter as"AA"since it exists in the alphabet.
was able to come up with anO(M*N) + O(Nlog(N))solution where M being the size of the strings and N being the size of the list. 
And the interviewer seemd to agree on the solution that I proposed and I am waiting for a feedback.
"""

#Q5:
"""
Given a collection of intervals, 
return a maximal set of non-overlapping intervals while prioritising the longer intervals.
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
When an exchange sends several messages over a TCP socket, they can be concatenated when performing the read. 
This is solved by parsing the buffer, and splitting in to multiple messages for each process call.
Please implement a packetize function that takes a constant char* and size_t:
void packetize(const char *data, size_t length);
This function can be a member function if necessary.
The packetize function should call a process function, with signature:
void process(const char *data, size_t length);


Given data buffer may contain incomplete packet, which may continue in the next call to packetize. 
At the same time, buffer may contain multiple packets as well, in which case all of the packets must be collected and process should be called for each one.
"""

#Q8:
"""
Phone Interview - Welch Dictionary
"""
# LZW Compression
def lzw_compress(input_string):
    # Initialize dictionary with single characters
    dictionary = {chr(i): i for i in range(256)}  # 256 ASCII characters
    current_code = 256  # The next available code
    result = []
    w = ""
    
    for c in input_string:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = current_code
            current_code += 1
            w = c
    
    # Output the code for the last string
    if w:
        result.append(dictionary[w])
    
    return result

# LZW Decompression
def lzw_decompress(compressed_data):
    # Initialize dictionary with single characters
    dictionary = {i: chr(i) for i in range(256)}
    current_code = 256
    w = chr(compressed_data[0])
    result = [w]
    
    for code in compressed_data[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == current_code:
            entry = w + w[0]
        result.append(entry)
        
        # Add w+entry to the dictionary
        dictionary[current_code] = w + entry[0]
        current_code += 1
        w = entry
    
    return "".join(result)

# Example usage:
input_string = "ABABABABA"
compressed_data = lzw_compress(input_string)
print("Compressed Data:", compressed_data)

decompressed_data = lzw_decompress(compressed_data)
print("Decompressed Data:", decompressed_data)

"""
Onsite interview 1 - Given source and target print all paths .
I coded the solution in the onsite round and even answered the OOPS related question and how to optimise the code and 
the underlying implementation ragarding unordered map and ordered map with the time complexity.
"""
def pathsToTarget(source, target):
    pass
#ordered map?
#un-ordered map?
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
Then, given a list of buy/sell orders which need to be executed 
in the given timeframe you need to find out what all orders can be served with atleast 1 exchange.
[
	['Order 1', '3', '6'],
	['Order 2', '9', '12'],
	['Order 3', '21', '22']
]
So in this case Order 1 and 2 can be served but 3 cannot be served by any exchange.

Follow-up = What if some exchanges operate from night to morning, ex - ['Exchange X', 23, 5]. Same thing with orders.
"""

def can_serve_orders(exchanges, orders):
    results = []
    for order in orders:
        order_name, order_start, order_end = order[0], int(order[1]), int(order[2])
        can_serve = False
        
        for exchange in exchanges:
            exchange_name, exchange_start, exchange_end = exchange[0], exchange[1], exchange[2]
            
            # Check for overlap
            if order_start <= exchange_end and order_end >= exchange_start:
                can_serve = True
                break
        
        results.append((order_name, can_serve))
    return results

# Example Inputs
exchanges = [['Exchange A', 2, 7], 
             ['Exchange C', 11, 17], 
             ['Exchange B', 9, 16],
             ['Exchange D', 14, 20]]

orders = [['Order 1', '3', '6'], 
          ['Order 2', '9', '12'], 
          ['Order 3', '21', '22']]

# Run the function
results = can_serve_orders(exchanges, orders)
for order, status in results:
    print(f"{order} can be served: {status}")


def normalize_intervals(start, end):
    if start <= end:
        return [(start, end)]
    else:  # Spans midnight
        return [(start, 23), (0, end)]

def can_serve_orders_with_night_shifts(exchanges, orders):
    results = []
    
    # Normalize exchange intervals
    normalized_exchanges = []
    for exchange in exchanges:
        name, start, end = exchange[0], exchange[1], exchange[2]
        intervals = normalize_intervals(start, end)
        for interval in intervals:
            normalized_exchanges.append((name, interval[0], interval[1]))
    
    # Check orders
    for order in orders:
        order_name, order_start, order_end = order[0], int(order[1]), int(order[2])
        order_intervals = normalize_intervals(order_start, order_end)
        can_serve = False
        
        for order_interval in order_intervals:
            for exchange_name, exchange_start, exchange_end in normalized_exchanges:
                if order_interval[0] <= exchange_end and order_interval[1] >= exchange_start:
                    can_serve = True
                    break
            if can_serve:
                break
        
        results.append((order_name, can_serve))
    return results

# Example Inputs with Night Shifts
exchanges = [['Exchange A', 2, 7], 
             ['Exchange C', 11, 17], 
             ['Exchange B', 9, 16],
             ['Exchange D', 14, 20],
             ['Exchange X', 23, 5]]

orders = [['Order 1', '3', '6'], 
          ['Order 2', '9', '12'], 
          ['Order 3', '21', '22'], 
          ['Order 4', '23', '2']]

# Run the function
results = can_serve_orders_with_night_shifts(exchanges, orders)
for order, status in results:
    print(f"{order} can be served: {status}")

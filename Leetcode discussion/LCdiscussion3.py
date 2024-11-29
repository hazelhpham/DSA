#Q1:
# Given a list of operation hour for each stock exchange, validate if the customer can send a trading order during the input hour.Design a function to test if selected banks collective trading hours cover the duration of the order without any gaps.
# Operation hours
# 09:00-16:00 Royal Bank of Scotland
# 11:00-17:00 Morgan Stanley
# ....
 
# Test case #1 - expected result: SUCCESS
# 10:00-17:00

# Test case #2 - expected result: FAILURE
# 15:00-21:00 


#Q2:
"""
# Test case1
trades = [ ("TSLA US Equity", 500), ("TSLA UQ Equity", 100)]
equals = [ ("TSLA US Equity", "TSLA UB Equity"), ("TSLA UQ Equity", "TSLA UW Equity"), ("TSLA UB Equity", "TSLA UQ Equity") ]
print(group_trades(trades, equals))

# Test case2
trades = [ ("TSLA US Equity", 500), ("TSLA US Equity", 600), ("VOD LN Equity", 1000), ("TSLA UW Equity", 250)]
equals = [ ("TSLA US Equity", "TSLA UB Equity"), ("TSLA UB Equity", "TSLA UW Equity"), ("VOD LN Equity", "VOD IN Equity")]
print(group_trades(trades, equals))
"""
from collections import defaultdict
def group_trades(trades, equals):
    
    company_to_idx = {}
    
    for i, (p1,p2) in enumerate(equals):
        if p1 in company_to_idx:
            company_to_idx[p2] = company_to_idx[p1]
        elif p2 in company_to_idx:
            company_to_idx[p1] = company_to_idx[p2]
        else:
            company_to_idx[p1] = i        
            company_to_idx[p2] = i    
    
    idx_to_companies = defaultdict(list)
    for company, idx in company_to_idx.items():
        idx_to_companies[idx].append(company)
    
    trades_result = defaultdict(int)
    for company, cost in trades:
        cmp_idx = company_to_idx[company]
        master_company = idx_to_companies[cmp_idx][0]
        trades_result[master_company] += cost
    
    return list(trades_result.items())


#Q3:
# 1. design live stock trading

#Q4:
# 2. rules managment

#Q5:
#https://leetcode.com/problems/binary-tree-maximum-path-sum/ 


#Q6:
"""
Task was very easy. We have tickers of stocks and many prices.
We need to add them and then be able to take N oldest by ticker and N params.
I think I choose right base structure Dictionary<string, XXX>
To store stock prices per ticker name.

-add("AAPL",121)
-add("TSLA",108)
-add("AAPL",125)
-add("AMZN",112)
-get_last_N_Values("AAPL",2) //here N is 2 so we use unordered_map<string,list> which wil be ("AAPL",[125,121])
returns [125,121]
"""

#Q7:
"""
Hello I had a first interview with Bloomberg and did not pass. I thought about the possible solutions but I cannot figure out what the optimal solution is.


Design a module and insert a data looking like this.


(id:1, timestamp: 1pm, tags: ["us", "uk", "japan"])
You want to query all the data by passing in a tag and timestamp.


(tag: "us", start_time: "12pm", end_time: "2pm")
The module will read more than insert. Reading should be faster than inserting. 
What is the possible optimal solution that read is more optimized than insert? Thank you in advance
"""

#Q8:
"""
Currency Conversion (https://leetcode.com/discuss/interview-question/483660/Google-or-Phone-or-Currency-Conversion)

https://leetcode.com/discuss/interview-question/124837/Stock-Ticker 
Not able to solve this one in optimized manner. Gave a brute force solution
Interviewers asked about resume and projects and "Why Bloomberg?"
"""
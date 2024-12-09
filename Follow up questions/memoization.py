"""
- the memoization technique is caching, which is the key concept of DP.

1. what is memoization?
- used to optimize recursive algorithms by storing (or caching)
the results of expensive function calls and reusing those results when the
same inputs occur again. this is especially useful in problems with overlapping
subproblems, which is a hallmark of DP. 

- in simpler terms, memoization ensures that you don't compute the same value
repeatedly. once a result has been computed for a particular sub-problem, it is stored,
and subsequent calls with the same inputs will retrieve the result directly from memory
rather than re-calculating it. 

2. why is memoization important in DP? 
- DP breaks a problem down to sub-problems. 
- these sub-problems can overlap -- meaning a problem can be computed multiple times

"""
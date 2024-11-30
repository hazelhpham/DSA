# Q1:
# Technical phone interview (45 min):


# Interviewer introduction, about my projects, and why Bloomberg (10 min)


# Technical Questions Hackerrank (25 min):
# https://leetcode.com/problems/validate-binary-search-tree/submissions/
# Q1) Write a function that checks if a binary tree is a valid binary search tree (25 min)


# Talked about brute force O(n^2) (5 min)
# Optimized solution to O(n) (5 min)
# Walk through an example of an optimized solution (5 min)
# Implementation of optimized solution (5 min)
# Interviewer asked to walk through with 2 more examples and provide time/space complexity (5 min)

#Q2:
"""
First Problem: A process tree has crashed and you are given a sequence of it's nodes in random order, 
each representing a process and possible child(s). Each node has at most two child process. 
Find the root process node


Input:
{5 : [], 1: [2, 3], 4 : [], 3: [6], 6 : [], 2 : [4, 5]}


                        1
                    /      \
                2            3
            /     \          / 
            4     5         6
Output: 1
"""
# For the first problem, the root node would be an ID that is not a child of any node -> definition of root node
# Approach 1:


# Loop through the entire input object and add all the child ID to a hash map called children
# Loop through the input object again, check if ID is in the children hash map created above
# a. If ID exist in children hash map -> it is a child and cannot be a root node
# b. if ID doesn't exist in children hash map -> must be the root node
# E.g., {5 : [ ] , 1: [2, 3], 4 : [ ], 3: [6], 6 : [ ], 2 : [4, 5]} <--- example from original post
# All process = [5, 1, 4, 3, 6, 2]
# All children = [2, 3, 6, 4, 5]
# Only ID that is in All process but not in All children is 1, so 1 is root node.


# Time complexity = O(n)
# Space complexity = O(n)

#Q2:
"""
Second Problem: Word Break ii

"""


#Q3:
"""
Given a sorted array of n elements, possibly with duplicates, find the number of occurrences of the target element.


Example 1:


Input: arr = [4, 4, 8, 8, 8, 15, 16, 23, 23, 42], target = 8
Output: 3
Example 2:


Input: arr = [3, 5, 5, 5, 5, 7, 8, 8], target = 6
Output: 0
Example 3:


Input: arr = [3, 5, 5, 5, 5, 7, 8, 8], target = 5
Output: 4
Expected O(logn) time solution.


Related problems:


https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
"""

#Q4:
"""
Hi everyone,
I had this problem on my interview with Bloomberg. It is easily solved in O(N), but it is required to solve it in O(1) (all following functions).


Build your own data structure which does the following functions:


add(integer) -> add a new integer.
getAll() -> return all elements in same insertion order.
deleteLast() -> delete the last inserted element.
getMaximum() -> return the maximum value of all elements.
getMaximumNeighbourValues() -> return the maximum value of two consecutive elements.
Example:
[7, 3, 1, 10]: maxValue=10, maxNeighborsValue=11
deleteLast -> [7, 3, 1]: maxValue=7, maxNeighborsValue=10
add(2) -> [7, 3, 1, 2]: maxValue=7, maxNeighborsValue=10
add(8) -> [7, 3, 1, 2, 8]: maxValue=8, maxNeighborsValue=10


Solution:
I came up to solve to first four functions in O(1). I used an arrayList to store the elements (to keep its order while insertion), and I used a LinkedHashMap to store the element as a key, and its occurrences as a value (that way, I kept the order to see which element is deleted, and I kept if maximum value should be modified -> takes the second last element in the map). That way, all functions have complexity O(1).


But the fifth function is still unclear for me!


"""

#Q5:
"""
The 1st round: Phone Call
It was pretty easy got asked 2 questions, one similar to LRU cache
2nd one similiar to Two sum find array pairs that add up to target value


I was able to solve both and moved forward to the video interview


2nd Round: Video Interview
2 interviewees, started off with behavioural questions like why bloomberg and so on.
The coding questions,


*Given a Subway system where the customer can swipe in his card to check in and swipe out his card to check out at destination station, get the average time needed to travel between any 2 stations. and I should save customer Id, create swipeIn and swipeOut functions and another to get the average


My main problem was that the interviewer didnt write the question or even a part of it, he just read it out loud really fast and ofcourse its a video call the connection isnt 100% so this for me ruined everything.


While he was reading the question I was trying to write on hackerrank shared screen what the question is and i asked a lot of question to understand what he wants but it made nervous already that it wasnt clear, the question isnt hard its complex for us internationals to understand it on the spot while listening.


Anyways, I did something like that (sudo code below: Excuse me if I forgot "self.")


def __init__(self):
	self.myDict=defaulttdict(list)
	self.time=0
	self.myStation=defaulttdict(list)
	
def swipeIn(InTime,arrSt,custId):
	self.time=InTime
	selfmyDict[custId].append(arrSt)
	
def swipeOut(OutTime,DestSt,custId):
	TotalTime=OutTime-self.Time
	myDict[custID].append(DestSt)
	myDict[custID].append(TotalTime))
	val=myDict[custID]
	route=val[0]+val[1] #arrivalSt+desSt
	
	if Route in self.myStation:
		v=self.myStation[Route]
		v[0]+=TotalTime #store all totalTime
		v[1]+=1 #store number if passengers
		v[2]=v[0]/v[1] #to store the average
   else:
	   v=[0,0,0]
		v[0]=TotalTime #store all totalTime
		v[1]=1 #store number if passengers
		v[2]=v[0]/v[1] #to store the average
	myStation[route]=v
	
def GetAverage(dest,arr):
	 route=dest+arr
	 if route in myStation:
		 v=myStation[route]
		 return v[2]
	return -1	 
I told him that I can sort route to get the same value for station AB=BA, but he told me its find he'd consider them differnt routes


Other Questions which I didnt do well in:
how does python store dictionaries? what key types are ok in python (I told him i only used strings and integers)


Follow up Question
1.what if a person lost his card how can you utilize that fact?
Ans: I told him I wouldnt store his custID anymore so I can use an orderdict with any capacity I want for example 500K persons and if i get a new person I remove the oldest entry from my OrderedDict


What if route didnt exisits between 2 stations?
Ans: I told him thats why I returned -1 he told me its not idicative I told him we dont have negative time, but i can instead return a string"No Route"
I know that overall I didnt do great, yet I got bumped from the rejection, I think things wouldve been better if he wrote down the questions and I should definitely study a thing or two on how things work with python internally
"""


#Q6:
"""
There was one question and hackerrank coderpad (I was expecting a proper hackerrank assessment)


Question:


'm' amount of oil can be purchased from 'n' companies. Every company has 'k' capacity of oil to be sold, you can take zero or many times the quantity offered by each company. Give the maximum number of combinations possible.


For examples:
There are three companies: A, B, C


A - 10
B - 15
C - 50


Target: 60


Number of Combinations: 4 {[10,50], [15,45], [20,40],[10,20,30]


I was able solve the question by priting all combination but my count was not updating, I was debugging the code but he told he didn't know java at all so we can move on. I thought I would get through, but they rejected me.


I hope this expereince might be useful for you!


Approach, I took:


I have generated multiples of all quantities in a list till the target amount. Then generated all possible subsets and for every subset, I was calculating sum of all elements in the subset. Later, compared sum with target, I have incremented count.


public class Solution {
    static Integer count=new Integer(0); // Global
    public static void main(String args[] ) throws Exception {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT */
        int [] given= {10,15,50};
        int target=60;
        List<Integer> quantities=new ArrayList<>();
        
        for(int i=0;i<given.length;i++) {
            int multiple=1;
            while(given[i]*multiple < target)  {
                if(!quantities.contains(given[i]*multiple))
                    quantities.add(given[i]*multiple);
                multiple++;
            }
        }
        //System.out.println(quantities);
        List<Integer> temp=new ArrayList<>();
        subset(quantities, temp, 0, target);
        System.out.println(count);


    }


public static void  subset(List<Integer> quantities, List<Integer> temp, int index, int target) {
    int sum=0;
    for(Integer i: temp) sum+=i;
    if(sum==target) {
        count++;
    }
    for(int i=index; i<quantities.size();i++) {
        temp.add(quantities.get(i));
        subset(quantities, temp, i+1, target);
        temp.remove(new Integer(quantities.get(i)));
    }
"""
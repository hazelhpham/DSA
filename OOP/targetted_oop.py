# Question 1:
# you have a class that took in UDP message and at the end of the UDP message you want to sequence them in the right order? 
# is this design ordered stream on leetcode? 


# Question 2:
# Summary
# Given one directional airport connections, devise a solution that can provide the route from Airport A to Airport B.
# Implement 2 functions: one that adds a one-directional airport connection between 2 airports, and second that return out all possible routes between an origin and a destination. This could be done by implementing a class called AirMap that has two methods:


# 1


# addConnection(start, destination)
# adds a ONE WAY connecting flight from start to destination
# 2


#  getAllRoutes(start, destination)
#  return all possible routes from start to destination irrespective of hops
# A ----> B
# B ----> A
# A ----> C
# C ----> A
# A ----> D
# D ----> A
# B ----> C
# C ----> B
# B ----> D
# D ----> B


# airMap.getAllRoutes('C', 'D');
# [[C,A,B,D,]
# [C,A,D,]
# [C,B,A,D,]
# [C,B,D,]]


# public class Solution {

#  public class AirMap {
#  HashMap<String, ArrayList<String>> connections = new HashMap<>();

#  public void addConnection(String start, String end){

#  }

#  public List<List<String>> getAllRoutes(String start, String end){

#  }

# }
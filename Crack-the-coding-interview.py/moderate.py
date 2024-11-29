#Q1: Living People: Given a list of people with their birth and death years,
#  implement a method to compute the year with the most number of people alive.
#  You may assume that all people were born between 1900 and 2000 (inclusive). 
#  If a person was alive during any portion of that year, they should be included in that year's count. 
#  For example, Person (birth= 1908, death= 1909) is included in the counts for both 1908 and 1909.

# A - (1901, 1999)
# B - (1999)
# C - (1905, 1955)
#merge interval ?
# -> 1905 - 1955  -> people A and C are alive
#are we doing range? or specific year? 
#this is the solution for specific year:
def livingPeople(years):
    if not years:
        return 0
    d = {}
    #for each year, if we go through the list of values, if we see it exists
    #we would increment the count in our dictionary
    for key, val in years.items():
        if val in d:
            d[val] +=1
        else:
            d[val] = 0
    years = sorted(d.items, key = lambda x:x[1])
    return years[0]


"""
This is the correct approach and the solution:
Input:

A list of birth and death years for individuals.
Example:
python
Copy code
people = [(1901, 1999), (1999, 1999), (1905, 1955)]
Output:

The year with the maximum number of people alive.
Approach:

Count the number of people alive for each year between 1900 and 2000.
Use an array to track births and deaths.
Calculate the net alive count for each year using a running sum.

"""
def living_people(people):
    # Initialize an array to track the changes in population for each year
    year_counts = [0] * 102  # For years 1900 to 2001 (index 0 -> year 1900)

    # Update birth and death years
    for birth, death in people:
        year_counts[birth - 1900] += 1  # Increment for birth
        year_counts[death - 1900 + 1] -= 1  # Decrement for death (next year)

    # Calculate the cumulative sum to get the number of people alive each year
    max_alive = 0
    max_year = 1900
    current_alive = 0

    for year in range(101):  # From 1900 to 2000
        current_alive += year_counts[year]
        if current_alive > max_alive:
            max_alive = current_alive
            max_year = 1900 + year

    return max_year

# Example Usage:
people = [(1901, 1999), (1999, 1999), (1905, 1955)]
print(living_people(people))  # Output: 1905

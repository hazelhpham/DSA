#bisect
"""
bisect module in Python provides support for maintaining
a list in sorted order without having to sort the list repeatedly. 

It can be used for binary searching and insertion in a sorted list. 

The main function in the bisect module are:
1. bisect.bisect_left(list, item)
- finds the position where item should be inserted to maintain the sorted order of a list
- it returns the index of first element greater than or equal to item
- this is equivalent to find the lower bound of item

2. bisect.bisect_right(list, item)
- it returns the position of the first element greater than item, i.e upper bound 
- this is typically used when you want to insert the item at rightmost position if
there are duplicate elements
"""

import bisect
lst = [1,3,4,6,8,9]
left_index = bisect.bisect_left(lst, 5)
right_index = bisect.bisect_right(lst,5)

print(f"Left index for 5: {left_index}") #3
print(f"Right index for 5 : {right_index}") #3

#before the index


#intersection of 2 arrays using bisec.bisec_left(num, arr)
import bisect

def intersection_binary_search_binarysearch(A, B):
    # First, sort both arrays (if not already sorted)
    A.sort()
    B.sort()
    
    result = []
    
    # Use binary search for each element in the smaller array
    for num in A:
        # Check if num is in B using binary search
        idx = bisect.bisect_left(B, num)
        if idx < len(B) and B[idx] == num:
            result.append(num)
    
    return result
"""
Step-by-Step Explanation:
Sorting the Arrays:

Both arrays are sorted at the beginning of the function. In this case, both A and B are already sorted.
A = [1, 2, 3, 4]
B = [2, 4, 6]
Initialize Result List:

We initialize an empty list result to store the intersection of A and B.
result = []
Iterating over each element in A:

Now, the function starts iterating over each element in the sorted list A using the for num in A loop.
Iteration 1 (num = 1):
We check if 1 exists in B using binary search.
idx = bisect.bisect_left(B, 1)
bisect_left returns the position in B where 1 could be inserted while maintaining the sorted order.
For B = [2, 4, 6], bisect_left will return 0, because 1 would be inserted at the start of the list, before 2.
The condition if idx < len(B) and B[idx] == num is checked:
idx = 0, so idx < len(B) is true.
But B[0] == 2, which is not equal to 1, so the condition fails.
No element is added to the result list for num = 1.
Iteration 2 (num = 2):

We check if 2 exists in B using binary search.
idx = bisect.bisect_left(B, 2)
bisect_left will return 0, as 2 is already at index 0 in B.
The condition if idx < len(B) and B[idx] == num is checked:
idx = 0, so idx < len(B) is true.
B[0] == 2, which is equal to 2, so the condition is true.
2 is added to the result list: result = [2].
Iteration 3 (num = 3):

We check if 3 exists in B using binary search.
idx = bisect.bisect_left(B, 3)
bisect_left will return 1, because 3 would be inserted between 2 and 4 in B.
The condition if idx < len(B) and B[idx] == num is checked:
idx = 1, so idx < len(B) is true.
But B[1] == 4, which is not equal to 3, so the condition fails.
No element is added to the result list for num = 3.
Iteration 4 (num = 4):

We check if 4 exists in B using binary search.
idx = bisect.bisect_left(B, 4)
bisect_left will return 1, because 4 is already at index 1 in B.
The condition if idx < len(B) and B[idx] == num is checked:
idx = 1, so idx < len(B) is true.
B[1] == 4, which is equal to 4, so the condition is true.
4 is added to the result list: result = [2, 4].
"""
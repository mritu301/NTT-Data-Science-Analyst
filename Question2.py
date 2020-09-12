#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 10:28:34 2020

@author: Mritunjay Kumar
@Question: 2 (Counting Pairs)
"""

def countingPairs(lst, k):
    count = 0
    n = len(lst)
    resultPair = []
    
    for i in range(0, n):                    # Iterate the loop for all elements in the list
        for j in range(i+1, n) :             # Then again iterate from the next index in the inner loop to that list               
            if (abs(lst[i] - lst[j]) == k):  # See the difference between the elements, if it matches the value K then 
                count += 1                   # Increase the count value by 1
                resultPair.append([lst[i],lst[j]])
                
    print("Resultant pairs : ", resultPair)
    return count 

# Test case 1:-
# lst = [1,3,5], K = 2
# expected: we will have 2 pairs: {(1,3), (3,5)}
lst = [1,3,5]
k = 2
print("Counting Pairs of ", lst, " with ", k, " is ", countingPairs(lst,k))


# Test case 1:-
# lst = [1,3,5, -4, -6, 7, 6, 4, -1, 1, 9, 34], K = 2
# expected: we will have 9 pairs: {[1, 3], [1, -1], [3, 5], [3, 1], [5, 7], [-4, -6], [7, 9], [6, 4], [-1, 1]}
lst1 = [1,3,5, -4, -6, 7, 6, 4, -1, 1, 9, 34]
k1 = 2
print("Counting Pairs of ", lst1, " with ", k1, " is ", countingPairs(lst1,k1))




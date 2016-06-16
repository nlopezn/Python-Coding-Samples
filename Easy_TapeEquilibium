
# Author: Nicola Lopez

"""  CODING PROBLEM FROM codility.com
A non-empty zero-indexed array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7 
P = 2, difference = |4 − 9| = 5 
P = 3, difference = |6 − 7| = 1 
P = 4, difference = |10 − 3| = 7 
Write a function:

def solution(A)
that, given a non-empty zero-indexed array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Assume that:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
"""


# Method: take input list. Split list into 2 parts (first half, second half). Find the sum of first half. Find sum of second half. 
# Find the absolute difference of first half and second half | first half - second half | , for all of the possible splits. 
# Find the smallest absolute difference from the list of differences 


import numpy as np


def getMinimumDifference(input_list):
    
    differences_list = getDifferencesList(input_list)
    
    minimum_difference = getMinimum(differences_list)
    
    return minimum_difference


def getMinimum(input_list):

    minimum = input_list[0]    
    
    for element in input_list[1:]:
        if element<minimum:
            minimum = element
            
    return minimum

def getDifferencesList(input_list):
    
    list_of_differences = []
    
    for number in range(len(input_list)):
        first_sum = sum(input_list[:number+1])
        second_sum = sum(input_list[number+1:])
        difference = np.abs(first_sum - second_sum)
        
        list_of_differences.append(difference)
        
    return list_of_differences
     
    #return list_of_differences


def sum(input_list):
    temp_sum = 0
    for element in input_list:
        temp_sum = element + temp_sum
    return temp_sum 

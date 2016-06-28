


# Author: Nicolas Lopez

"""  CODING PROBELM FROM www.codility.com
A zero-indexed array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
Triplet (0, 2, 4) is triangular.

Write a function:

int solution(int A[], int N);
that, given a zero-indexed array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
the function should return 1, as explained above. Given array A such that:

  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1
the function should return 0.

"""

#  Use sorted() function to do the sorting

def solution(A):

    if A==[] or len(A)<3:
        return 0 
        
    #orderedA = sorted(A)      # doing a sort from smallest to largest is the heart of the solution. 
    orderedA = getOrdered(A)
    
    for index in range(len(orderedA)-2):
        A = orderedA[index]
        B = orderedA[index+1]
        C = orderedA[index +2]
        
        if A+B>C:    # It is only necessary to check this condition. Since the array is ordered, C>A and C>B. So C+B>A, and C+A>B
            return 1 
       
            
    return 0 
    
# Alternatively can write own merge-sort algorithm
    
    
def getOrdered(A):
    
    N = len(A)
    
    n = int(N/2)
    
    if N==1:
        return A
    
    temp_list = []    
    if N==2:
        if A[1]<A[0]:
            temp_list.append(A[1])
            temp_list.append(A[0])
            return temp_list
            
        else:
            return A
    if N>2:
        half_1 = A[:n]
        half_2 = A[n:]
        
        half_1_ordered = getOrdered(half_1)
        half_2_ordered = getOrdered( half_2)
        
        total_ordered_list = merge(half_1_ordered,half_2_ordered)
        
        return total_ordered_list
        
def merge(A,B):
    temp_array = []
    pos_a = 0
    pos_b = 0
    
    for a in A:
        for b in B[pos_b:]:
            if b<a:
                temp_array.append(b)
                pos_b = pos_b+1 
            elif a<=b:
                temp_array.append(a)
                pos_a = pos_a +1 
                break
    if pos_a<len(A):
        temp_array = temp_array + A[pos_a:]
    if pos_b<len(B):
        temp_array = temp_array + B[pos_b:]
        
    return temp_array

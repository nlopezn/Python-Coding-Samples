


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
    orderedA = sort(A)
    
    for index in range(len(orderedA)-2):
        A = orderedA[index]
        B = orderedA[index+1]
        C = orderedA[index +2]
        
        if A+B>C:    # It is only necessary to check this condition. Since the array is ordered, C>A and C>B. So C+B>A, and C+A>B
            return 1 
       
            
    return 0 
    
# Alternatively can write own merge-sort algorithm
    
def sort(array):
    
    size_array = len(array)
    if size_array!=1:
        mid_point = int(size_array/2)
        A=array[:mid_point]
        B=array[mid_point:]
        A_sorted = sort(A)
        B_sorted = sort(B) 
        
        return merge(A_sorted,B_sorted)
    
    elif size_array==1:
        return A
        
def merge(A,B):
    
    merged_list =[]
    size_A=len(A)
    size_B=len(B)
    
    index_A=0
    index_B=0    
    
    while index_A<size_A and index_B<size_B:
        if A[index_A]<=B[index_B]:
            merged_list.append(A[index_A])
            index_A+=1
        else:
            merged_list.append(B[index_B])
            index_B+=1
    if index_A==size_A:
        merged_list = merged_list + B[index_B:]
    elif index_B==size_B:
        merged_list = merged_list + A[index_A:]
        
    return merged_list

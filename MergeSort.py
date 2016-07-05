
#Author: Nicolas Lopez 

"""
Recursive form of Merge-Sort Algorithm. 
Input: List or array of numbers
Output: Sorted list or array in ascending order

Sort Method: If the input list is longer than 1, split the array into 2 parts. Then sort each part separately. The sorting is done 
by calling on the same function that is being defined. This is the recursive part. After the first part and second part are sorted, 
merge the 2 parts together. 

Merge Method: Start at the first index of the two arrays that are to be sorted (A[0] and B[0]). Compare the first two numbers. Pick the smaller
number to be placed into an 'output array'. For example, suppose A[0] is smaller than B[0]. The move to the next index in A. So now, compare 
A[1] with B[0]. Pick the smaller of that pair. Repeat the process until you reach the end of A or the end of B.  
The last step is to combine the 'output array' with the rest of what's left over, which could be the tail of A or the tail of B. 

"""


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

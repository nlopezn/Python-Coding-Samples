


# Author: Nicolas Lopez

def solution(A):

    if A==[] or len(A)<3:
        return 0 
 
    orderedA = getOrdered(A)
    
    for index in range(len(orderedA)-2):
        A = orderedA[index]
        B = orderedA[index+1]
        C = orderedA[index +2]
        
        if A+B>C:
            return 1
       
            
    return 0 
    
# Alternatively could also used sorted() function to do the sorting instead of own merge-sort algorithm
    
    
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
    temp = []
    pos_a = 0
    pos_b = 0
    
    for a in A:
        for b in B[pos_b:]:
            if b<a:
                temp.append(b)
                pos_b = pos_b+1 
            elif a<=b:
                temp.append(a)
                pos_a = pos_a +1 
                break
    if pos_a<len(A):
        temp = temp + A[pos_a:]
    if pos_b<len(B):
        temp = temp + B[pos_b:]
        
    return temp

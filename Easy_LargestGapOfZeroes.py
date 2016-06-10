"""
Find Largest Gap (number of consecutive 0's) in the binary representation of a number
"""


def getLargestGap(N):
    
    binary_list = getBinary(N)
    temp_gap_length =0
    longest_gap_length = 0
    temp_longest_gap_length =0

    for number in binary_list:
        if number == 0:
            temp_gap_length = temp_gap_length +1
            
            if temp_gap_length>longest_gap_length:
                temp_longest_gap_length = temp_gap_length
                
        elif number ==1:
            longest_gap_length = temp_longest_gap_length
            temp_gap_length = 0
            
    return longest_gap_length
   
    
    
def getBinary(N):
    power =getLargestPower(N)
    binary_list =[0]*(power+1)
    binary_list[0]=1
    division= N/(2**power)
    
    if division==1:
        return binary_list
    elif division>1:
        new_number = N-(2**power)
        new_binary_list =getBinary(new_number)
        length = len(new_binary_list)
        binary_list[-length:]=new_binary_list
        return binary_list
        
        
        
def getLargestPower(N):
    for n in range(100):
        factor = 2**n
        division = N/factor
        if division==1:
            return(n)
        elif division<1:
            return(n-1)

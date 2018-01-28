#Using the Python language, have the function PentagonalNumber(num) read num which will be a positive integer and 
#determine how many dots exist in a pentagonal shape around a center dot on the Nth iteration. 


def PentagonalNumber(num): 
    a=1+5*(num-1)*num/2
    return a
    
print PentagonalNumber(raw_input())

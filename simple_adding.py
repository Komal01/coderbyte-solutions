#Text of challenge: "Have the function SimpleAdding(num) add up all the
#numbers from 1 to num. For the test cases, the parameter num will be
#any number from 1 to 1000."

def SimpleAdding(num): 

    n=0
    for i in range(1,num+1):
        n=n+i
    return n
    
print SimpleAdding(raw_input())
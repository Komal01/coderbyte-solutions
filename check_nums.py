def CheckNums(num1,num2): 
    if num1<num2:
        return 'true'
    elif num1>num2:
        return 'false'
    else:
        return -1
        
    
print CheckNums(raw_input())
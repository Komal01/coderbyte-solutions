#Using the Python language, have the function ScaleBalancing(strArr) read strArr which will contain two elements, 
#the first being the two positive integer weights on a balance scale (left and right sides) and 
#the second element being a list of available weights as positive integers. 
#our goal is to determine if you can balance the scale by using the least amount of weights from the list, but using at most only 2 weights.
def ScaleBalancing(strArr): 

    a,b = eval(strArr[0])
    x = eval(strArr[1])

    for i in range(0, len(x)):
        if a + x[i] == b or b + x[i] == a:
            return x[i]
        for j in range(i + 1, len(x)):
            if a + x[i] == b + x[j] or a + x[j] == b + x[i] or a + x[i] + x[j] == b or a == b + x[i] + x[j]:
                return str(x[i]) + ',' + str(x[j])
    return 'not possible'
    
  
print ScaleBalancing(raw_input())
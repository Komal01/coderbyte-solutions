#Using Python language, have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it

def FirstFactorial(num): 
    factorial = 1
    for i in range(1,num+1):
      factorial=factorial*i
    return factorial
  
print FirstFactorial(raw_input())  
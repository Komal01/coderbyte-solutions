#Write a program to count the no. of ones in the binary of a decimal number. store the result in the array with first
#index having the total no. of ones followed by places of ones in ascending order.
NOTE: CONSIDER NUMBER WHO HAVE '1' AT THE STARTING INDEX ELSE IGNORE. EG: 6 HAS ITS BINARY EQUIVALENT TO '110' SO 
THIS IS ACCEPTABLE.



n= int(input("Enter the Number:"))

def getOneBits(n):
    count=0
    final_array=[]
    binary= bin(n)
    temp = binary[2:]
    for i in range(len(temp)):
        if temp[i] == '1':
            count+=1
            final_array.append(i+1)
    final_array.insert(0,count)
    return final_array

getOneBits(n)

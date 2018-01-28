#take any four digit number (whose digits are not all identical), and do the following:
#Rearrange the string of digits to form the largest and smallest 4-digit numbers possible.
#Take these two numbers and subtract the smaller number from the larger.
#Use the number you obtain and repeat the above process until you get the number 6174



def KaprekarsConstant(num): 
    count=0
    while num!= 6174:
        snum = '{:04d}'.format(num)
        num = int("".join(sorted(snum,reverse =True))) - int("".join(sorted(snum)))   
        count+=1
    return count
     
print KaprekarsConstant(raw_input())
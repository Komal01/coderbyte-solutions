#The positive odd numbers are sorted in ascending order as 1,3,5,7,9,11,13,15,17,19…………….,
#and grouped as (1), (3,5), (7,9,11), (13,15,17,19) and so on. Thus, the first group is(1) , the second group is (3,5), the third group is (7,9,11) etc
#In general, the kth group contains the next k elements of the sequence. Given k, find the sum of the elements of the kth group.	
		
k = int(input())
first = int((k * (k - 1)) + 1)  # computing the first number in the kth group 
sum = 0
while k:         # finding the sum.
    sum += first
    first += 2
    k=k-1
print (sum)
 		

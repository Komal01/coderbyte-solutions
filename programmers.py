#N programmers are standing in a line. All of them have some skills given by Ai, where 1<=i<=N.Their trainer can teach them and can increase their skills. At a time he can teach only one concept to one student. By learning a new concept, the skills of a programmer increase by 1.
#The trainer can teach only P concepts to some students. He can teach multiple concepts to same student.
#The trainer wants that most of the programmers should have the same skill level. 

from collections import Counter
T= int(input())
N,P = map(int,input().split(' '))
arr = input()
arr = arr.split(" ")
num = [int(i) for i in arr]
for i in range(P-1):
    a = num.index(min(num))
    num[a] += 1
    
data = Counter(num)
m_c =max(num, key=data.get)
    
result1 = num.count(m_c)

print (result1, m_c)

#You have to print the numbers from 1 to 200 in new line.But for every multiple of 5 print "Foo", 
#for every multiple of 7 print "Bar" and for every multiple of both 5 and 7 print "FooBar" instead of the number.

for i in range(1,201):
    if i%5==0 and i%7==0:
        print("FooBar")
    elif i%5 ==0:
        print("Foo")
    elif i%7==0:
        print("Bar")
    else:
        print(i)
		
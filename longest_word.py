#using Python language, have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string
def LongestWord(sen): 
    sen = sen.translate(None,"+=-_\{}[];':./<>?,!@#$%^&*()")
    a= sen.split(" ")
    return max(a , key=len)
    
print LongestWord(raw_input())
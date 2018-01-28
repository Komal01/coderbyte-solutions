#Text of challenge: "Have the function LetterChanges(str) take the str parameter
#being passed and modify it using the following algorithm. Replace every letter
#in the string with the letter following it in the alphabet (ie. c becomes d, z
#becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and
#finally return this modified string."

def LetterChanges(str): 
    newstring = ""
    for char in str:
        if char.isalpha():
           if char.lower()=='z':
               char='a'
           else:
               char=chr(ord(char)+1)
        if char in 'aeiou':
            char=char.upper()
        newstring = newstring + char        
    return newstring
     
print LetterChanges(raw_input())
def anagram(string1,string2):
    string1=string1.lower()
    string2=string2.lower()
    if sorted(string1)==sorted(string2):
        return("string is anagaram")
    else:
        return("not an anagram")
    
str1=input("Enter First string: ")
str2=input("Enter second String: ")

print(anagram(str1,str2))


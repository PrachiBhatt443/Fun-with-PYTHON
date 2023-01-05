#Find if words are anagram 
str1 = input("Enter first word")
str2 = input("Enter second word")
if(len(str1)==len(str2)):
    s1 = sorted(str1)
    s2 = sorted(str2)
    if(s1==s2):
        print(str1 + " and " + str2 + " are anagram.")
    else:
        print(str1 + " and " + str2 + " are not anagram.")
else:
    print(str1 + " and " + str2 + " are not anagram.")
str1=input("Enter any string of characters").lowerQwertyuioplkmjnhbgvfcdxszaqwetgvbn
()
y=set(str1)-set(" ")
print(y)
if len(y)==26:
    print("Yes its a panagram")
else:
    print("oops its not a panagram")
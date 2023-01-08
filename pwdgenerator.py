import random
def shuffle(a):
  random.shuffle(a)
  return ''.join(a)
def rletter():
    u=chr(random.randint(65,90))
    return u
# def rdigit():
#     v=random.randint(65,90)
#     return v
l=int(input("Enter the length:"))
a=[]
for i in range(l):
    s=rletter()
    # s=rdigit()
    a.append(s)
#Generate password using all the characters, in random order
# password = uppercaseLetter1 + uppercaseLetter2 # + ....
password = shuffle(a)
#Ouput
print(password)
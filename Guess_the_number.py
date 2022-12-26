import random
num=random.randint(1,10)
num_of_guess=0
p_name=input("Welcome, Please Enter your name")
print("Can you guess my favourite number from 1 to 10\nYou have five chances")
while num_of_guess<5:
    num_of_guess+=1
    guess=int(input("Enter your guess:"))
    if guess< num:
        print("Too low,increase a bit")
    elif guess> num:
        print("Too high,decrease a bit")
    else:
        print("Gotcha,You got it")
        break
    print("chances left",5-num_of_guess)
if guess!=num:
    print("You can't guess it")
    print("Answer is",num)
    
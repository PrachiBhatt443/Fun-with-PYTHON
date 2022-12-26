from random import randint
#list of options
l=["Rock","Paper","Scissors"]
#assigning random option to computer
computer=l[randint(0,2)]
player=False
while player==False:
    player=input("Rock,Paper,Scissors?")
    if player==computer:
        print("TIE")
    elif player=="Rock":
        if computer=="Scissors":
            print("You win","Let's smash the scissors")
        else:
            print("You loose",computer,"cover the rock")
    elif player=="Scissors":
        if computer=="Paper":
            print("You win","Let's cut the paper")
        else:
            print("You loose",computer,"smashed your scissors")
    elif player=="Paper":
        if computer=="Rock":
            print("You win","Let's cover the rock")
        else:
            print("You loose",computer,"cuts the paper")
    else:
        print("Invalid input")
player=False
computer=l[randint(0,2)]
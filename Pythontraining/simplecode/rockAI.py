import random

computer_choice = random.choice(["paper", "rock", "scissors"])
user_choice = input("Pick rock, paper or scissors!\n")

if computer_choice == user_choice:
    print ("TIE!")

elif user_choice == "rock" and computer_choice == "scissors":
    print ("YOU WIN! Computer had " + computer_choice)

elif user_choice == "scissors" and computer_choice == "paper":
    print ("YOU WIN! Computer had " + computer_choice)

elif user_choice == "paper" and computer_choice == "rock":
    print ("YOU WIN! Computer had " + computer_choice)

else:
    print ("YOU LOSE! You had " + user_choice + ", and computer choose " + computer_choice)

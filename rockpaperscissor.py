import random

user = input("Enter: ").lower()
options = ("rock", "paper","scissor")
computer = random.choice(options)
print(f"Computer: {computer}")
if user == computer:
    print("Draw")
elif user == "scissor" and computer == "rock":
    print("U lost")
elif user == "rock" and computer == "scissor":
    print("u won")
elif user == "scissor" and computer == "paper":
    print("U won")
elif user == "paper" and computer == "scissor":
    print("U lost")
elif user == "rock" and computer == "paper":
    print("U lost")
elif user == "paper"  and computer == "rock":
    print("U won")                   

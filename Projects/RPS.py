import random

opn = ("rock", "paper", "scissors")

score1 = 0
score2 = 0
running = True

while(running):
    choice = True  
    player_choice = None
    computer_choice = random.choice(opn)

    while player_choice not in opn:
      if(choice == False):
        print("Not in option!")
      player_choice = input("Enter your Choice: ").lower()
      choice = False

    print(f"Player Choice: {player_choice}")
    print(f"Computer Choice: {computer_choice}")

    if(player_choice == computer_choice):
      print("It's a tie")
    elif(player_choice == "rock" and computer_choice == "scissors"):
      score1 += 1
      print("You win!")
    elif(player_choice == "paper" and computer_choice == "rock"):
      score1 += 1
      print("You win!")
    elif(player_choice == "scissors" and computer_choice == "paper"):
      score1 += 1
      print("You win!")
    else:
      score2 += 1
      print("Computer wins.")

    Again = input("\nDo you want to play again? (yes/no)\n").lower()
    if(Again != "yes"):
      running = False

print(f"\nYour Score: {score1}")
print(f"Computer Score: {score2}")
print("Thanks for playing!\n")


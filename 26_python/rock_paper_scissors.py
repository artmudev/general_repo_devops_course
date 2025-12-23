import random

weapon = ["rock", "paper", "scissors"]

def weapon_choice():
    print("Choose your weapon!")
    for i in range(len(weapon)):
        print(f"{i + 1} : {weapon[i]}")


weapon_choice()

player_choice = input("Choose your weapon 1-3" + "\n")


if player_choice == "1":
    player_weapon = "rock"
elif player_choice == "2":
    player_weapon = "paper"
elif player_choice == "3":
    player_weapon = "scissors"
else:
    print("Invalid choice, please choose anything between 1 and 3")
    exit()

computer_weapon = random.choice(weapon)

if player_weapon == computer_weapon:
    print(f"Computer chose {computer_weapon}, it's a draw!")
elif (
    (player_weapon == "rock" and computer_weapon == "scissors") or
    (player_weapon == "paper" and computer_weapon == "rock") or
    (player_weapon == "scissors" and computer_weapon == "paper")
):
    print(f"Computer chose {computer_weapon}, you win!")
else:
    print(f"Computer chose {computer_weapon}, Computer wins!")

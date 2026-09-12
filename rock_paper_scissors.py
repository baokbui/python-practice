# Rock, Paper, Scissors with 2 player input
import time

player1 = input("Player 1, please enter your name: ")
player2 = input("Player 2, please enter your name: ")

player1_choice = input(f"{player1} - Rock, Paper, or Scissors: ")
player2_choice = input(f"{player2} - Rock, Paper, or Scissors: ")

game_state = True

while game_state:
    print("Rock!")
    time.sleep(0.5)
    print("Paper!")
    time.sleep(0.5)
    print("Scissors!")
    time.sleep(0.5)
    print("Shoot!")
    time.sleep(0.5)

    print(f"{player1}: {player1_choice}")
    print(f"{player2}: {player2_choice}")
    time.sleep(1)

    if player1_choice == "Rock" and player2_choice == "Scissors":
        print(f"Congratulations {player1}!")
    elif player1_choice == "Rock" and player2_choice == "Paper":
        print(f"Congratulations {player2}!")
    elif player1_choice == "Paper" and player2_choice == "Rock":
        print(f"Congratulations {player1}!")
    elif player1_choice == "Paper" and player2_choice == "Scissors":
        print(f"Congratulations {player2}!")
    elif player1_choice == "Scissors" and player2_choice == "Paper":
        print(f"Congratulations {player1}!")
    elif player1_choice == "Scissors" and player2_choice == "Rock":
        print(f"Congratulations {player2}!")
    else:
        print(f"It's a tie! Or player(s) didn't play the right thing...")

    quitGame = input("Quit Game?(Y/N)\n")
    while quitGame not in ("Y", "N"):
        quitGame = input("Please enter a valid input(Y/N)\n")

    if quitGame == "Y":
        game_state = False
    else:
        game_state = True
        player1_choice = input(f"{player1} - Rock, Paper, or Scissors: ")
        player2_choice = input(f"{player2} - Rock, Paper, or Scissors: ")
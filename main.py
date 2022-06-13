import random
def RPSgame():
    print("Rock Paper Scissors Game")
    print("R for Rock \nP for Paper \nS for Scissors")
    user_action = input("Press R, P or S : ")
    choice = user_action.lower()
    if choice in ('r', 'p', 's'):
        print("loading....")
        cpu_choices = ["r", "p", "s"]
        cpu_action = random.choice(cpu_choices)

        print(f"\nYou chose {user_action}, computer chose {cpu_action}.\n")

        if user_action == cpu_action:
            print(f"Both Players Selected {user_action}. It's a Tie!")
            RPSgame()
        elif user_action == "r":
            if cpu_action == "s":
                print("Rock Smashes Scissors! You win")
            else:
                print("Paper covers rock! You lose.")
        elif user_action == "p":
            if cpu_action == "r":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user_action == "s":
            if cpu_action == "p":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

        game_over = input("Play again? Y/N: ")
        if game_over.lower()== "y":
            RPSgame()
        else:
            print("Game Over")
    else:
        print("Invalid Input")
        print("Pick Again")
        RPSgame()


RPSgame()
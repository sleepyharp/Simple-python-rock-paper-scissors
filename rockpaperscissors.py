import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("Enter rock, paper, scissors, or 'end' to exit: ").lower()
        if user_choice == "end":
            print("Exiting the game. Goodbye!")
            break
        elif user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        bot_choice = random.choice(choices)
        print(f"Bot chose: {bot_choice}")

        if user_choice == bot_choice:
            print("It's a draw!")
        elif (user_choice == "rock" and bot_choice == "scissors") or \
             (user_choice == "paper" and bot_choice == "rock") or \
             (user_choice == "scissors" and bot_choice == "paper"):
            print("You win!")
        else:
            print("Bot wins!")

        rerun = input("Type 'rerun' to play again or 'end' to exit: ").lower()
        if rerun == "end":
            print("Exiting the game. Goodbye!")
            break
        elif rerun != "rerun":
            print("Invalid input. Exiting the game.")
            break

if __name__ == "__main__":
    play_game()
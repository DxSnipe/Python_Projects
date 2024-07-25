import random


def get_user_choice():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Please choose rock, paper, or scissors: ")
    while user_choice not in choices:
        print("Invalid choice. Please try again")
        user_choice = input("Please choose rock, paper, or scissors: ")
    return user_choice


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or (
            user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"


def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    print(f"User chose: {user_choice}")
    winner = determine_winner(user_choice, computer_choice)
    if winner == "user":
        print("You won!")
    elif winner == "computer":
        print("You lost!")
    else:
        print("It's a draw!")
    return winner


def main():
    user_score = 0
    computer_score = 0
    draw_count = 0
    while True:
        winner = play_game()
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        else:
            draw_count += 1

        print(f"Scores: You - {user_score}, Computer - {computer_score}, Draw - {draw_count}")

        play_again = input("Would you like to play again? (y/n): ")
        if play_again != "y":
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    main()

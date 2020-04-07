"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

user_attempt = []


def display_score():
    if len(user_attempt) <= 0:
        print("Great news! There is no currenly high score on the table. You could be the first!")
    else:
        print("The current high score is {} attempts".format(min(user_attempt)))
        
def start_game():
    computer_num = int(random.randint(1,10))
    greetings = print("""
    ----------------------------------------------
    Welcome to the Number Guessing Game!
    ----------------------------------------------
    """)

    play = input("Do you want to play the Guessing Game? (Yes/No)")
    attempt = 0

    while play.lower() == 'yes':
        try:
            guess  = int(input("Please pick a number between 1 and 10: "))
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("ohh no! please pick a number between 1 - 10")
            if guess == computer_num:
                print("You got it! My number was {}".format(computer_num))
                attempt += 1
                user_attempt.append(attempt)
                print("It took you {} tries to guessed the number".format(attempt))
                play_again = input("Would you like to play again? (Yes/No) ")
                attempt = 0
                display_score()
                computer_num = int(random.randint(1,10))
                if play_again.lower() == 'no':
                    print("That's Ok, thanks for playing!")
                    break
            elif guess > computer_num:
                print("It's lower than {}".format(guess))
                attempt += 1
            elif guess < computer_num:
                print("It's higher than {}".format(guess))
                attempt += 1
        except ValueError as err:
            print("Oh no, You need to enter a number! try again!")
    else:
        print("That's OK, Thanks for playing!")
if __name__ == '__main__':
    start_game()

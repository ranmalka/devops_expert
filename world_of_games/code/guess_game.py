
import random
import time
from utils import clear_screen

#Guess a number Game functions
def play(difficulty):
    clear_screen()
    print("*" * 10)
    print("Welcome to Guess the Number Game")
    print("*" * 10)
    time.sleep(2)
    clear_screen()
    if difficulty == "1":
        last_number = 1
        score = compare_results(last_number)

    if difficulty == "2":
        last_number = 2
        score = compare_results(last_number)

    if difficulty == "3":
        last_number = 3
        score = compare_results(last_number)

    if difficulty == "4":
        last_number = 4
        score = compare_results(last_number)

    if difficulty == "5":
        last_number = 5
        score = compare_results(last_number)

    print(f"Game Over! Your final score was: {score}")
    if score == 3:
        print("You Win !! Back to the Main Menu")
        time.sleep(4)
        clear_screen()
        return True
    else:
        print("You Lose !! Back to the Main Menu")
        time.sleep(4)
        clear_screen()
        return False
def generate_number(last_number):
    secret_number = random.randint(0, last_number)
    return secret_number

def get_guess_from_user(last_number):
    print(f"Try to guess the number between 0 to {last_number}:")
    time.sleep(1)
    user_secret_number = input(f"Enter Your Guess Number: ")
    return user_secret_number

def compare_results(last_number):
    score = 0
    tries = 0
    while score < 3 and tries < 5:
        if int(get_guess_from_user(last_number)) == int(generate_number(last_number)):
            print("Congrats!")
            score += 1
            tries += 1
        else:
            print("You Wrong please try again")
            tries += 1
            time.sleep(2)

        print(f"Your score is: {score}")
        time.sleep(2)
        clear_screen()
    return score

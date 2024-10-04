import app
import random
import time
from utils import clear_screen

#Memory Game functions
def play(difficulty):
    clear_screen()
    print("*" * 10)
    print("Welcome to Memory Game")
    print("*" * 10)
    time.sleep(2)
    clear_screen()
    score = 0
    tries = 0
    if difficulty == "1":
        length = 1
        is_list_equal(length)
    if difficulty == "2":
        length = 2
        is_list_equal(length)
    if difficulty == "3":
        length = 3
        is_list_equal(length)
    if difficulty == "4":
        length = 4
        is_list_equal(length)
    if difficulty == "5":
        length = 5
        is_list_equal(length)

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

def get_sequence(length,last_number):
    sequence = [random.randint(0, last_number) for _ in range(length)]
    return sequence
def get_list_from_user(length):
    print("Try to remember this sequence:")
    time.sleep(2)
    sequence = get_sequence(length,100)
    print(sequence)
    time.sleep(0.7)
    clear_screen()
    user_sequence = input(f"Enter the sequence of {length} numbers PLEASE USE SPACE BETWEEN THE NUMBERS: ")
    user_guess = list(map(int, user_sequence.split()))
    return user_guess, sequence

def is_list_equal(length):
    score = 0
    tries = 0
    while score < 3 and tries < 5:
        user_list_and_sequence = (get_list_from_user(length))
        if user_list_and_sequence[0] == user_list_and_sequence[1]:
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

play("1")
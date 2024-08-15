import random
import time
import os
import requests
from bs4 import BeautifulSoup


def welcome():
    username = input("Please Enter Your Username:")
    clear_screen()
    print("*" * 15)
    print("Hi " + username + " and welcome to the World of Games:")
    print("*" * 15)

def clear_screen():
    # Clears the screen depending on the OS
    os.system('cls' if os.name == 'nt' else 'clear')
def start_play():
    print("Here the list of Games")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back. ")
    print("2. Guess Game - guess a number and see if you chose like the computer.")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    print("4. Quit")
    game_choice = input("Please choose a Game:")

    if int(game_choice) < 1 or int(game_choice) > 4:
        print("Please choose an option only between 1 and 4")
        time.sleep(2)
        clear_screen()
        start_play()

    difficulty = input("Please choose a difficulty, 1 is the easiest and 5 is the hardest:")

    if int(difficulty) < 1 or int(difficulty) > 5:
        print("Please choose difficulty only between 1 and 5")
        time.sleep(2)
        clear_screen()
        start_play()

    elif game_choice == "1":
        memory_game(difficulty)
    elif game_choice == "2":
        guess_game(difficulty)
    elif game_choice == "3":
        currency_roulette(difficulty)
    else:
        print("Thank you for playing!")
        time.sleep(2)
        exit(1)

#Memory Game functions
def memory_game(difficulty):
    clear_screen()
    print("*" * 10)
    print("Welcome to Memory Game")
    print("*" * 10)
    time.sleep(2)
    clear_screen()
    score = 0
    tries = 0
    if difficulty == "1":
        while score < 3 and tries < 5:
            print(score)
            length = 3
            last_number = 5
            user_guess_and_sequence = get_sequence(length,last_number)
            if user_guess_and_sequence[0] == user_guess_and_sequence[1]:
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

    if difficulty == "2":
        while score < 3 and tries < 5:
            length = 5
            last_number = 5
            user_guess_and_sequence = get_sequence(length, last_number)
            if user_guess_and_sequence[0] == user_guess_and_sequence[1]:
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

    if difficulty == "3":
        while score < 3 and tries < 5:
            length = 7
            last_number = 9
            user_guess_and_sequence = get_sequence(length, last_number)
            if user_guess_and_sequence[0] == user_guess_and_sequence[1]:
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

    if difficulty == "4":
        while score < 3 and tries < 5:
            length = 7
            last_number = 15
            user_guess_and_sequence = get_sequence(length, last_number)
            if user_guess_and_sequence[0] == user_guess_and_sequence[1]:
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

    if difficulty == "5":
        while score < 3 and tries < 5:
            length = 7
            last_number = 20
            user_guess_and_sequence = get_sequence(length,last_number)
            if user_guess_and_sequence[0] == user_guess_and_sequence[1]:
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

    print(f"Game Over! Your final score was: {score}")
    print("Back to the Main Menu")
    time.sleep(4)
    clear_screen()
    start_play()
def get_sequence(length,last_number):
    sequence = [random.randint(0, last_number) for _ in range(length)]
    print("Try to remember this sequence:")
    time.sleep(2)
    print(sequence)
    time.sleep(1)
    clear_screen()
    user_sequence = input(f"Enter the sequence of {length} numbers PLEASE USE ENTER BETWEEN THE NUMBERS: ")
    user_guess = list(map(int, user_sequence.split()))
    return [user_guess, sequence]

#Guess a number Game functions
def guess_game(difficulty):
    clear_screen()
    print("*" * 10)
    print("Welcome to Guess the Number Game")
    print("*" * 10)
    time.sleep(2)
    clear_screen()
    score = 0
    tries = 0
    if difficulty == "1":
        while score < 3 and tries < 5:
            last_number = 5
            user_guess_and_number = get_random_number(last_number)
            if int(user_guess_and_number[0]) == int(user_guess_and_number[1]):
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

    if difficulty == "2":
        while score < 3 and tries < 5:
            last_number = 10
            user_guess_and_number = get_random_number(last_number)
            if int(user_guess_and_number[0]) == int(user_guess_and_number[1]):
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

    if difficulty == "3":
        while score < 3 and tries < 5:
            last_number = 20
            user_guess_and_number = get_random_number(last_number)
            if int(user_guess_and_number[0]) == int(user_guess_and_number[1]):
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

    if difficulty == "4":
        while score < 3 and tries < 5:
            last_number = 36
            user_guess_and_number = get_random_number(last_number)
            if int(user_guess_and_number[0]) == int(user_guess_and_number[1]):
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

    if difficulty == "5":
        while score < 3 and tries < 5:
            last_number = 100
            user_guess_and_number = get_random_number(last_number)
            if int(user_guess_and_number[0]) == int(user_guess_and_number[1]):
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

    print(f"Game Over! Your final score was: {score}")
    print("Back to the Main Menu")
    time.sleep(4)
    clear_screen()
    start_play()
def get_random_number(last_number):
    random_number = random.randint(0, last_number)
    print(f"Try to guess the number between 0 to {last_number}:")
    time.sleep(1)
    user_random_number = input(f"Enter Your Guess Number: ")
    return [random_number, user_random_number]

#Currency Roulette game functions
def currency_roulette(difficulty):
    clear_screen()
    print("*" * 10)
    print("Welcome to Guess the Currency roulette Game")
    print("*" * 10)
    time.sleep(2)
    clear_screen()
    score = 0
    tries = 0
    if difficulty == "1":
        while score < 3 and tries < 5:
            start_number = 0
            last_number = 10
            user_guess_and_number = get_random_usd(last_number,start_number)
            if int(user_guess_and_number[0]) == int(user_guess_and_number[1]):
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

    if difficulty == "2":
        while score < 3 and tries < 5:
            start_number = 10
            last_number = 50
            user_guess_and_number = get_random_usd(last_number,start_number)
            print(user_guess_and_number[0])
            if int(user_guess_and_number[0]) == int(user_guess_and_number[1]):
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

    if difficulty == "3":
        while score < 3 and tries < 5:
            start_number = 50
            last_number = 150
            user_guess_and_number = get_random_usd(last_number,start_number)
            print(user_guess_and_number[0])
            if int(user_guess_and_number[0]) == int(user_guess_and_number[1]):
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

    if difficulty == "4":
        while score < 3 and tries < 5:
            start_number = 150
            last_number = 500
            user_guess_and_number = get_random_usd(last_number,start_number)
            print(user_guess_and_number[0])
            if int(user_guess_and_number[0]) == int(user_guess_and_number[1]):
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

    if difficulty == "5":
        while score < 3 and tries < 5:
            start_number = 500
            last_number = 1000
            user_guess_and_number = get_random_usd(last_number,start_number)
            print(user_guess_and_number[0])
            if int(user_guess_and_number[0]) == int(user_guess_and_number[1]):
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

    print(f"Game Over! Your final score was: {score}")
    print("Back to the Main Menu")
    time.sleep(4)
    clear_screen()
    start_play()
def get_usd_to_ils_rate():
    url = "https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=ILS"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the exchange rate on the page
    rate_element = soup.find("p", class_="sc-e08d6cef-1 fwpLse")
    if rate_element:
        exchange_rate_text = rate_element.text.strip()
        exchange_rate = exchange_rate_text.split()[0]
        #print(f"1 USD is equal to {exchange_rate} ILS")
        return exchange_rate
    else:
        print("Failed to retrieve exchange rate data.")
        return None
def get_random_usd(last_number,start_number):
    random_number = random.randint(start_number, last_number)
    usd_to_ils_rate = get_usd_to_ils_rate()
    ils_rate = round(float(usd_to_ils_rate)*int(random_number))
    print(f"How many ILS worth {random_number}$? PLEASE USE INTEGER NUMBER")
    print("Please note the number is rounded by 0.5")
    print("for Exmaple: 1.2 will be 1 and 1.6 will be 2")
    time.sleep(3)
    user_random_number = input(f"Enter Your Guess: ")
    while not user_random_number.isdigit():
        print("That's not a whole number. Try again.")
        user_random_number = input("Enter an integer: ")
    user_random_number = int(user_random_number)
    return [ils_rate, user_random_number]








import requests
import time
import random
from bs4 import BeautifulSoup
from utils import clear_screen

#Currency Roulette game functions
def play(difficulty):
    clear_screen()
    print("*" * 10)
    print("Welcome to Guess the Currency roulette Game")
    print("*" * 10)
    time.sleep(2)
    clear_screen()
    if difficulty == 1:
        score = compare_results(difficulty)

    if difficulty == 2:
        score = compare_results(difficulty)

    if difficulty == 3:
        score = compare_results(difficulty)

    if difficulty == 4:
        score = compare_results(difficulty)

    if difficulty == 5:
        score = compare_results(difficulty)

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

def get_money_interval():
    url = "https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=ILS"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the exchange rate on the page
    rate_element = soup.find("p", class_="sc-48043a1-1 hjTGVC")
    if rate_element:
        exchange_rate_text = rate_element.text.strip()
        exchange_rate = exchange_rate_text.split()[0]
        #print(f"1 USD is equal to {exchange_rate} ILS")
        random_number = random.randint(1, 100)
        ils_random_rate = round(float(exchange_rate) * int(random_number))

        return random_number, ils_random_rate
    else:
        print("Failed to retrieve exchange rate data.")
        return None

def get_guess_from_user():
    rate_and_random_number = get_money_interval()
    usd_random_number = rate_and_random_number[0]
    ils_random_rate = rate_and_random_number[1]
    print(f"How many ILS worth {usd_random_number}$? PLEASE USE INTEGER NUMBER")
    print("Please note the number is rounded by your difficulty level")
    print("for Exmaple: 10 in difficulty 1 can be any number between 1-19 (+-9")
    time.sleep(3)
    user_random_number = input(f"Enter Your Guess: ")
    while not user_random_number.isdigit():
        print("That's not a whole number. Try again.")
        user_random_number = input("Enter an integer: ")
    user_random_number = int(user_random_number)
    return ils_random_rate, user_random_number

def compare_results(difficulty):
    score = 0
    tries = 0
    while score < 3 and tries < 5:
        get_guess_from_user_list = get_guess_from_user()
        ils_random_rate = get_guess_from_user_list[0]
        user_random_number = get_guess_from_user_list[1]
        base = 10 - difficulty
        ils_random_rate_min = ils_random_rate - base
        ils_random_rate_max = ils_random_rate + base
        ils_correct_numbers = []
        for i in range(ils_random_rate_min, ils_random_rate_max):
            ils_correct_numbers.append(i)
        if int(user_random_number) in ils_correct_numbers:
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





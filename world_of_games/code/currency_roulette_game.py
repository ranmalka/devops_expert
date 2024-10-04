import app
import requests
import time
from bs4 import BeautifulSoup
from utils import clear_screen

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
    base = 0
    if difficulty == "1":
        while score < 3 and tries < 5:
            start_number = 1
            last_number = 100
            base = 10 - difficulty
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
            start_number = 1
            last_number = 100
            base = 10 - difficulty
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
            start_number = 1
            last_number = 100
            base = 10 - difficulty
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
            start_number = 1
            last_number = 100
            base = 10 - difficulty
            user_guess_and_number = get_random_usd(last_number,start_number)
            #add here the round function
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
            start_number = 1
            last_number = 100
            base = 10 - difficulty
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
    app.start_play()
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
def myround(x, base):
    return base * round(x/base)


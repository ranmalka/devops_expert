import time
from utils import clear_screen
import guess_game
import memory_game
import currency_roulette_game
from main_score import score_server
from score import add_score
import random, threading, webbrowser





def welcome():
    username = input("Please Enter Your Username:")
    clear_screen()
    print("*" * 15)
    print("Hi " + username + " and welcome to the World of Games:")
    print("*" * 15)
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
        if memory_game.play(difficulty) == True:
            print("lets see your final score!!")
            add_score(difficulty)
            start_play()
        else:
            start_play()
    elif game_choice == "2":
        if guess_game.play(difficulty) == True:
            print("lets see your final score!!")
            add_score(difficulty)
            start_play()
        else:
            start_play()
    elif game_choice == "3":
        if currency_roulette_game.play(difficulty) == True:
            print("lets see your final score!!")
            add_score(difficulty)
            start_play()
        else:
            start_play()
    else:
        print("Thank you for playing!")
        time.sleep(2)
        exit(1)












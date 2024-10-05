import os
def clear_screen():
    # Clears the screen depending on the OS
    os.system('cls' if os.name == 'nt' else 'clear')

SCORES_FILE_NAME = "score.txt"


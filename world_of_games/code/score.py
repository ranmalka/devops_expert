from utils import SCORES_FILE_NAME


def add_score(difficulty):
    file = open(SCORES_FILE_NAME,"r")
    POINTS_OF_WINNING = (int(file.read()))
    POINTS_OF_WINNING += (int(difficulty)*3) + 5
    file.close()
    file = open(SCORES_FILE_NAME,"w")
    file.write(str(POINTS_OF_WINNING))
    file.close()
    file = open(SCORES_FILE_NAME,"r")
    POINTS_OF_WINNING = (int(file.read()))
    file.close()
    print(POINTS_OF_WINNING)

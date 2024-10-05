from utils import SCORES_FILE_NAME


def add_score(difficulty):
    file = open(SCORES_FILE_NAME,"r+")
    POINTS_OF_WINNING = file.read()
    if POINTS_OF_WINNING == '':
        POINTS = 0
        POINTS += (int(difficulty) * 3) + 5
        POINTS_OF_WINNING = POINTS
        file.close()
        file = open(SCORES_FILE_NAME, "w")
        file.write(str(POINTS_OF_WINNING))
        file.close()
        return POINTS_OF_WINNING
    else:
        try:
            POINTS_OF_WINNING = int(POINTS_OF_WINNING)
            POINTS_OF_WINNING += (int(difficulty)*3) + 5
            file.close()
            file = open(SCORES_FILE_NAME,"w")
            file.write(str(POINTS_OF_WINNING))
            file.close()
            file = open(SCORES_FILE_NAME,"r")
            POINTS_OF_WINNING = file.read()
            file.close()
            return POINTS_OF_WINNING
        except ValueError:
            return "ERROR"




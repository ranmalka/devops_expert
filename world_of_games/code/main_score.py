from flask import Flask, Response, render_template, request
from score import add_score

import random, threading, webbrowser

app = Flask(__name__, template_folder='.')


def score_server(difficulty):
    score_file = add_score(difficulty)
    if score_file == "ERROR":
        @app.route('/')
        def home():
            return render_template('error.html', ERROR = "Score not found")

        port = 5000 + random.randint(0, 999)
        url = f"http://127.0.0.1:{port}?difficulty={difficulty}".format(port)  # Example difficulty of 3
        threading.Timer(1, lambda: webbrowser.open(url)).start()
        app.run(port=port, debug=False)

    else:
        @app.route('/')
        def home():
            difficulty = request.args.get('difficulty', default=1, type=int)
            return render_template('index.html', SCORE=score_file)

        port = 5000 + random.randint(0, 999)
        url = f"http://127.0.0.1:{port}?difficulty={difficulty}".format(port)  # Example difficulty of 3
        threading.Timer(1, lambda: webbrowser.open(url)).start()
        app.run(port=port, debug=False)

# score_file = add_score(difficulty)
# if add_score(difficulty) == '':
#     @app.route('/')
#     def home():
#        difficulty = request.args.get('difficulty', default=1, type=int)
#        print(difficulty)
#        return render_template('index.html', SCORE = add_score(difficulty))
#
# else:
#     @app.route('/')
#     def home():
#        difficulty = request.args.get('difficulty', default=1, type=int)
#        print(difficulty)
#        return render_template('index.html', SCORE = add_score(difficulty))


# if  __name__ == '__main__':
#     app.run('0.0.0.0', debug=True, port=3000)

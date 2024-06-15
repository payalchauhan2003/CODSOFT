from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Initialize scores
user_score = 0
computer_score = 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/play', methods=['POST'])
def play():
    global user_score, computer_score
    user_choice = request.form['choice']
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    result = determine_winner(user_choice, computer_choice)

    if result == 'win':
        user_score += 1
    elif result == 'lose':
        computer_score += 1

    return render_template('result.html', user_choice=user_choice, computer_choice=computer_choice, result=result,
                           user_score=user_score, computer_score=computer_score)


def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or (user == 'scissors' and computer == 'paper') or (
            user == 'paper' and computer == 'rock'):
        return 'win'
    else:
        return 'lose'


@app.route('/play_again', methods=['POST'])
def play_again():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

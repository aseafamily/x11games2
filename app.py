from flask import Flask, render_template_string, render_template
import os

app = Flask(__name__)

@app.route('/')
def read_index():
    return render_template('index.html')

@app.route('/games/hangman')
def hangman():
    return render_template('games_hangman2.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000) 

    
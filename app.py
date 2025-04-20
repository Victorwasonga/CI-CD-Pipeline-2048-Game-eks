from flask import Flask, render_template, session, redirect, request, url_for
from game_logic import Game2048
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    if 'game' not in session:
        session['game'] = Game2048().__dict__
    game = Game2048()
    game.__dict__ = session['game']
    return render_template('index.html', grid=game.get_grid())

@app.route('/move/<direction>', methods=['POST'])
def move(direction):
    game = Game2048()
    game.__dict__ = session['game']
    game.move(direction)
    session['game'] = game.__dict__
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session.pop('game', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
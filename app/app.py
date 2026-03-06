# app.py
import os
import sys

from flask import Flask, jsonify, render_template, request

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.minesweeper import Minesweeper

app = Flask(__name__)

game = Minesweeper(9, 9, 10)


def board_state():
    if game.game_over:
        board = game.get_full_board()
    else:
        board = game.get_board()
    return {
        "board": board,
        "flags_left": game.remaining_mines,
        "game_over": game.game_over,
        "won": game.won,
        "rows": game.rows,
        "cols": game.cols,
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/state")
def state():
    return jsonify(board_state())


@app.route("/api/new-game", methods=["POST"])
def new_game():
    data = request.get_json()
    rows = int(data.get("rows", 9))
    cols = int(data.get("cols", 9))
    mines = int(data.get("mines", 10))
    rows = max(2, min(rows, 30))
    cols = max(2, min(cols, 50))
    mines = max(1, min(mines, rows * cols - 1))
    global game
    game = Minesweeper(rows, cols, mines)
    return jsonify(board_state())


@app.route("/api/reveal", methods=["POST"])
def reveal():
    data = request.get_json()
    row = int(data["row"])
    col = int(data["col"])
    if 0 <= row < game.rows and 0 <= col < game.cols:
        game.reveal(row, col)
    return jsonify(board_state())


@app.route("/api/flag", methods=["POST"])
def flag():
    data = request.get_json()
    row = int(data["row"])
    col = int(data["col"])
    if 0 <= row < game.rows and 0 <= col < game.cols:
        game.toggle_flag(row, col)
    return jsonify(board_state())


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 8082)))

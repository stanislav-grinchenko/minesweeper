# tests/test_minesweeper.py

import pytest
import minesweeper

def test_module_exists():
    assert minesweeper

def test_place_mines():
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    # TODO : Add assertions
    assert len(game.mines) == 2
    assert game.rows ==3
    assert game.cols ==3

def test_reveal():
    import random
    random.seed(0)
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    revealing = game.reveal(2, 2)
    if game.board[2][2] == "💣":
        assert (revealing=="Game Over")
    else:
        assert revealing=="Continue"
        assert (2,2) in game.revealed
        if game.board[1][1] == "":
            assert(1,1) in game.revealed
        else:
            assert(1,1) not in game.revealed

def test_get_board():
    import random
    random.seed(0)
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    revealing = game.reveal(2, 2)
    board = game.get_board()
    assert board[2][2] != ""
    assert board [0][0] == ""
    
def test_is_winner():
    import random
    random.seed(0)
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    for r in range(game.rows):
        for c in range(game.cols):
            if (r,c) not in game.mines:
                game.reveal(r,c)
    assert game.is_winner() == True
"""This module implements the Minesweeper game."""

# minesweeper.py
import random


class Minesweeper:
    """Minesweeper game"""

    def __init__(self, rows: int, cols: int, num_mines: int):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.board = [["" for _ in range(cols)] for _ in range(rows)]
        self.mines = set()
        self.revealed = set()
        self.place_mines()

    def place_mines(self):
        """Randomly place mines on the board, updating adjacent cells with mine counts."""
        self.mines = set()
        self.board = [["" for _ in range(self.cols)] for _ in range(self.rows)]
        self.revealed = set()
        for _ in range(self.num_mines):
            mine_placed = False
            while not mine_placed:
                col = random.randint(0, self.cols - 1)
                row = random.randint(0, self.rows - 1)
                if (row, col) not in self.mines:
                    mine_placed = True
                    self.mines.add((row, col))
                    self.board[row][col] = "💣"
        for r, c in self.mines:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    cell_i = r + i
                    cell_j = c + j
                    if (
                        cell_i < 0
                        or cell_j < 0
                        or cell_i >= self.rows
                        or cell_j >= self.cols
                        or self.board[cell_i][cell_j] == "💣"
                    ):
                        continue
                    if self.board[cell_i][cell_j] == "":
                        self.board[cell_i][cell_j] = 1
                    else:
                        self.board[cell_i][cell_j] += 1

    def reveal(self, row: int, col: int) -> str:
        """Reveal a cell on the board.
        Any adjacent cells with no mines are also revealed.
        Returns "Game Over" if a mine is revealed, "Continue" otherwise.
        """
        if self.board[row][col] == "💣":
            return "Game Over"
        self.revealed.add((row, col))
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < self.rows and 0 <= j < self.cols and (i, j) != (row, col):
                    if self.board[i][j] == "":
                        self.revealed.add((i, j))
        return "Continue"

    def get_board(self) -> list:
        """Return the current state of the board."""
        board = [
            [
                self.board[i][j] if (i, j) in self.revealed else ""
                for j in range(self.cols)
            ]
            for i in range(self.rows)
        ]
        return board

    def is_winner(self) -> bool:
        """Check if the game has been won."""
        return len(self.revealed) == self.rows * self.cols - len(self.mines)

    def restart(self) -> None:
        """Restart the game with the same parameters."""
        self.__init__(self.rows, self.cols, self.num_mines)

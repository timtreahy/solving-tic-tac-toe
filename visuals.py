# DESCRIPTION: This file is responsible for rendering the gui, and rendering moves that have been done on the board

import tkinter as tk


class Board:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.create_board()

    def create_board(self):
        # Create the Tic-Tac-Toe board using a 3x3 grid of buttons
        self.board = [[tk.Button() for j in range(3)] for i in range(3)]
        for i in range(3):
            for j in range(3):
                self.board[i][j].grid(row=i, column=j)

    def update_board(self, move, symbol):
        # code to update the board on the GUI with the latest move
        pass

    def display_result(self, winner):
        # code to display the result of the game on the GUI
        pass

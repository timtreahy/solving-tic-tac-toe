# DESCRIPTION: This file coordinates visuals, game_state, and the agents
from visuals import Board
from game_state import GameState
from config import select_agents
import tkinter as tk

player_1, player_2 = select_agents()
root = tk.Tk()
# root.title("Tic-Tac-Toe")
board = Board(root)
root.mainloop()

game = GameState()
# board = Board()
while not game.is_over():
    # get the next move from player 1
    move = player_1.get_move(game.legal_moves())
    if game.validate_action(player_1, move):
        game.record_action(player_1, move)
        board.update_board(move, player_1.symbol)
    else:
        # handle invalid move
        pass

    if game.is_over():
        break

    # get the next move from player 2
    move = player_1.get_move(game.legal_moves())
    if game.validate_action(player_2, move):
        game.record_action(player_2, move)
        board.update_board(move, player_2.symbol)
    else:
        # handle invalid move
        pass

# display the result on the GUI
board.display_result(game.winner)

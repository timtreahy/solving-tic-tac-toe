# DESCRIPTION: This file keeps track of moves played by which player, and contains a list of remaining legal moves

class GameState:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.winner = None

    def validate_action(self, player, action):
        # code to check if the action is valid
        pass

    def record_action(self, player, action):
        # code to record the action
        pass
    def legal_moves(self):
        # code to return a list of legal moves
        pass
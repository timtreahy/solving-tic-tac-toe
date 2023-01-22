# DESCRIPTION: This agent looks at the list of remaining legal moves, and chooses a random one.

import random


class RandomAgent:
    def __init__(self):
        pass

    def get_move(self, legal_moves):
        return random.choice(legal_moves)

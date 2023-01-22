import argparse

# from agents/human import HumanAgent
# from agents/random import RandomAgent
# from agents/decision_tree import DecisionTreeAgent

# from agents.my_agent import MyAgent

from human_agent import HumanAgent
from random_agent import RandomAgent
from decision_tree_agent import DecisionTreeAgent

def parse_args():
    parser = argparse.ArgumentParser(description='Select agents for the game')
    parser.add_argument('--player1', type=str, default='human',
                        choices=['human', 'random', 'my_agent'], help='Select agent for player 1')
    parser.add_argument('--player2', type=str, default='random',
                        choices=['human', 'random', 'my_agent'], help='Select agent for player 2')

    return parser.parse_args()


def select_agents():
    args = parse_args()
    player1 = args.player1
    player2 = args.player2

    if player1 == 'human':
        player1 = Human()
    elif player1 == 'random':
        player1 = RandomAgent()
    # elif player1 == 'my_agent':
        # player1 = MyAgent()

    if player2 == 'human':
        player2 = Human()
    elif player2 == 'random':
        player2 = RandomAgent()
    # elif player2 == 'my_agent':
        # player2 = MyAgent()

    return player1, player2

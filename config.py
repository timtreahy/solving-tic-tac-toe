import argparse
from human_agent import HumanAgent
from random_agent import RandomAgent
from decision_tree_agent import DecisionTreeAgent

agents = {
    "decision_tree": DecisionTreeAgent,
    "random": RandomAgent,
    "human": HumanAgent
}


def parse_args():
    parser = argparse.ArgumentParser(description='Select agents for the game')
    parser.add_argument('--player1', type=str, default='human',
                        choices=list(agents.keys()), help='Select agent for player 1')
    parser.add_argument('--player2', type=str, default='random',
                        choices=list(agents.keys()), help='Select agent for player 2')
    return parser.parse_args()


def select_agents():
    args = parse_args()
    cliPlayerArgs1 = args.player1
    cliPlayerArgs2 = args.player2
    player1 = agents[cliPlayerArgs1]()
    player2 = agents[cliPlayerArgs2]()
    return player1, player2

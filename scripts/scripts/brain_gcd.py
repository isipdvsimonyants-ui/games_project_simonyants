import sys
import os

project_root = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, os.path.abspath(project_root))

from games_project_simonyants.engine import run_game
from games_project_simonyants.games.gcd import generate_round, DESCRIPTION

def main():
    class GcdGame:
        DESCRIPTION = DESCRIPTION
        generate_round = staticmethod(generate_round)

    run_game(GcdGame)

if __name__ == '__main__':
    main()

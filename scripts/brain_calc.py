import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from games_project_simonyants.engine import run_game
from games_project_simonyants.games import calc

def main():
    print("VD-calc")
    run_game(calc)

if __name__ == "__main__":
    main()


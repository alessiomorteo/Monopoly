from game_resources.monopoly_game import MonopolyGame
from game_resources.monopoly_board import MonopolyBoard
from game_resources.monopoly_bank import MonopolyBank
from game_resources.utils import (
    create_players, setup_properties_from_json
)
from typing import List

# game settings
NUM_PLAYERS = 4
START_BALANCE = 1500
PROPERTIES_PATH = "src/resources/monopoly_properties.json"
PROPERTIES_KEY = "property_type"
BANK = MonopolyBank()

def main():
    players = create_players(NUM_PLAYERS, START_BALANCE)
    game_properties = setup_properties_from_json(PROPERTIES_PATH, PROPERTIES_KEY)
    board = MonopolyBoard(game_properties)
    game = MonopolyGame(bank=BANK, players=players, board=board)
    print("Game is about to start...")
    game.play()
    print("Game has finished! The winner is x!")

if __name__ == "__main__":
    main()
from game_resources.monopoly_game import MonopolyGame
from game_resources.monopoly_property import MonopolyProperty
from game_resources.monopoly_player import MonopolyPlayer
from game_resources.monopoly_board import MonopolyBoard

START_BALANCE = 1500

def main():
    players = [MonopolyPlayer(f"player_{i}", START_BALANCE) for i in range(1,4)]
    board = MonopolyBoard(MonopolyProperty("test", 350, 25))
    game = MonopolyGame(players=players, board=board)
    print("Game is starting...")
    print("Game has finished! The winner is x!")

if __name__ == "__main__":
    main()
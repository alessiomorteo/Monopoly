from monopoly_game import MonopolyGame
from monopoly_property import MonopolyProperty
from monopoly_player import MonopolyPlayer
from monopoly_board import MonopolyBoard

START_BALANCE = 500

def main():
    players = [MonopolyPlayer(f"player_{i}", START_BALANCE) for i in range(1,4)]
    game = MonopolyGame(players=players, board=MonopolyBoard())
    print("Game is starting...")
    print("Game has finished! The winner is x!")

if __name__ == "__main__":
    main()
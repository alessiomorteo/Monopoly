from monopoly_board import MonopolyBoard
from monopoly_player import MonopolyPlayer
from typing import List
from random import randint

class MonopolyGame:
    def __init__(self, board:MonopolyBoard, players:List[MonopolyPlayer])->None:
        """Initialise the game board and player list."""
        self.board = board
        self.players = players
    
    def roll_dice(self)->None:
        """Function to mimic the rolling of two dice.
        Sets a list of the outcome of each of the two rolls.
        """
        self.roll_outcomes = [randint(1,6) for i in range(2)]

    def take_turn(self)->None:
        """Function to have the current player take their turn.
        """
        pass

    def play(self)->None:
        """The main loop for the game to be played out until it is game over.
        """
        while not self.game_over:
            self.take_turn()
    
    def game_over(self):
        """Function to check if the game is over, i.e. only one player has
        a balance greater than zero.
        """
        pass

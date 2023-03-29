from monopoly_board import MonopolyBoard
from monopoly_player import MonopolyPlayer
from monopoly_bank import MonopolyBank
from typing import List
from random import randint
import time

class MonopolyGame:
    def __init__(self, bank:MonopolyBank, board:MonopolyBoard, players:List[MonopolyPlayer])->None:
        """Initialise the game board and player list."""
        self.bank = bank
        self.board = board
        self.players = players
        self.player_index = 0
        self.player_turn = self.players[self.player_index].name
        self.game_over = False
    
    def play(self)->None:
        """The main loop for the game to be played out until it is game over.
        """
        while not self.game_over:
            self.take_turn()
            self.__set_player_active_status()
            self.check_is_game_over()
    
    def _roll_dice(self)->List[int]:
        """
        Function to mimic the rolling of two dice.
        Sets a list of the outcome of each of the two rolls.

        Returns:
            List[int]: A list of two dice roll outcomes.
        """
        return [randint(1,6) for i in range(2)]

    def take_turn(self)->None:
        """Function to have the current player take their turn.
        """
        self.player_turn = self.players[self.player_index]
        print(f"{self.player_turn.name} is taking their turn.")
        print(f"{self.player_turn.name} is on tile {self.player_turn.position}.")
        roll_total = sum(self._roll_dice())
        print(f"{self.player_turn.name} has rolled a {roll_total}.")
        raw_new_position = self.player_turn.position + roll_total
        if raw_new_position > 39:
            raw_new_position = abs(raw_new_position - 39)
        self.player_turn.position = raw_new_position

        print(f"{self.player_turn.name} has moved to tile {self.player_turn.position}.")
        #TODO:
        # - Give player actions
        # - Take action
        # Ending turn with the block below
        
        if self.player_index < (len(self.players) - 1):
            self.player_index += 1
        else:
            self.player_index = 0
        
        time.sleep(5)

    def __set_player_active_status(self):
        """
        Set the 'active' attribute of the players that do not have a positive balance to 'False' .
        """
        _ = [player.__setattr__("active", False) for player in self.players if player.balance < 0]

    def __check_players_active(self):
        """
        Filter the list of players to get only those with a positive active status.
        """
        return [player for player in self.players if player.active]

    def check_is_game_over(self):
        """Function to check if the game is over, i.e. only one player has
        a balance greater than zero.
        """
        if not self.__check_players_active():
            self.game_over = True
        
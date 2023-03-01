
class MonopolyGame:
    def __init__(self)->None:
        """Initialise the game board and player list."""
        self.board = []
        self.players = []

    def add_player(self, player):
        """Adds an individual player to the list of players involved 
        in the given game.

        Args:
            player (MonopolyPlayer): An instance of the class MonopolyPlayer, representing one player.
        """
        self.players.append(player)
    
    def roll_dice(self):
        """Function to mimic the rolling of two dice.
        Sets a tuple of the outcome of each of the two rolls.
        """
        pass

    def take_turn(self):
        """Function to have the current player take their turn.
        """
        pass

    def play(self):
        """The main loop for the game to be played out until it is game over.
        """
        while not self.game_over:
            self.take_turn()
    
    def game_over(self):
        """Function to check if the game is over, i.e. only one player has
        a balance greater than zero.
        """
        pass

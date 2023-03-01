
class MonopolyGame:
    def __init__(self) -> None:
        self.board = []
        self.players = []

    def add_player(self, player):
        self.players.append(player)
    
    def roll_dice(self):
        pass

    def take_turn(self):
        pass

    def play(self):
        while not self.game_over:
            self.take_turn()
    
    def game_over(self):
        pass

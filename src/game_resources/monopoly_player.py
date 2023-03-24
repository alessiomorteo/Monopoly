
class MonopolyPlayer:
    def __init__(self, name:str, starting_balance:int):
        """Instantiate a Monopoly player.

        Args:
            name (str): The name of the player.
            starting_balance (int): The balance that the player will start with.
        """
        self.name = name # player's name
        self.balance = starting_balance # balance player has
        self.position = 0 # index of position on the board
        self.properties = [] # properties owned by the player

    def player_status(self)->dict:
        """Gives a summary of the player's status.

        Returns:
            dict: _description_
        """
        return {
            "player_name": self.name,
            "balance": self.balance,
            "properties": self.properties
            }


    def buy_property(self, property)->None:
        """Function to handle the purchase of a property by the player.

        Args:
            property (_type_): The property to be purchased.
        """
        self.balance -= property.price
        self.properties.append(property)
        property.set_owner(self)

    def pay_rent(self, amount:int)->None:
        """Function to handle the payment of rent.

        Args:
            amount (int): The value of the rent to be charged.
        """
        self.balance -= amount

    def receive_rent(self, amount:int)->None:
        """Function to handle the receipt of rent from another player.

        Args:
            amount (int): The value of the rent to be received.
        """
        self.balance += amount

    def can_afford(self, amount:int)->bool:
        """Function to check if the player can afford to purchase a property.

        Args:
            amount (int): The cost of the property that the player wishes to purchase.

        Returns:
            bool: Boolean to represent 
        """
        return self.balance >= amount
    
    
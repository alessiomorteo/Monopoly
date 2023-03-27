class MonopolyProperty:
    def __init__(self, position: int, name:str, price:int, rent:int):
        """Initialise a Monopoly property.

        Args:
            position (int): The position of the property on the board.
            name (str): The name of the property.
            price (int): The purchase price of the property.
            rent (int): The rental cost charged of the property.
        """
        self.pos = position
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None

    def set_owner(self, owner:str) -> bool:
        """Handle the purchasing of a property by a player.
        Will set the player that is the owner of the property.

        Args:
            owner (str): The name of the player that is to become the owner.
        
        Returns:
            bool: A boolean to indicate the status of the ownership change.
        """
        if self.owner is not None:
            print(f"This property is already owned by {self.owner}.")
            return False
        else:
            self.owner = owner
            return True

    def get_rent(self)->None:
        """Function to handle the receipt of rent payment from another player.
        """
        pass


class RailStationProperty(MonopolyProperty):
    def __init__(self, name, price, rent):
        super().__init__(name, price, rent)
    
    def get_rent(self)->None:
        pass


class UtilityProperty(MonopolyProperty):
    def __init__(self, name, price, rent):
        super().__init__(name, price, rent)
    pass
    

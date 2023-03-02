class MonopolyProperty:
    def __init__(self, name:str, price:int, rent:int):
        """Initialise a Monopoly property.

        Args:
            name (str): The name of the property.
            price (int): The purchase price of the property.
            rent (int): The rental cost charged of the property.
        """
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None

    def set_owner(self, owner:str)->None:
        """Set the player that is the owner of the property.

        Args:
            owner (str): The name of the player that is to become the owner.
        """
        self.owner = owner

    def get_rent(self)->None:
        """Function to handle the receipt of rent payment from another player.
        """
        pass

    

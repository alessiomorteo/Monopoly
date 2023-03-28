class SpecialTile:
    def __init__(self, position: int, name:str):
        """Initialise a Monopoly tile.

        Args:
            position (int): The position of the tile on the board.
            name (str): The name of the tile.
        """
        self.pos = position
        self.name = name

class EventTile(SpecialTile):
    def __init__(self, position, name):
        super().__init__(position, name)

class TaxationTile(SpecialTile):
    def __init__(self, position, name, rent):
        super().__init__(position, name)
        self.rent = rent

    def get_tax_owed(self):
        return self.rent

class BaseProperty:
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
        self.base_rent = rent
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

    def get_rent_price(self)->int:
        """Function to handle the receipt of rent payment from another player.

        Returns:
            int: The value of rent that is due.
        """
        return self.base_rent

class MonopolyProperty(BaseProperty):
    def __init__(self, position, name, price, rent):
        super().__init__(position, name, price, rent)
        self.houses = 0
        self.hotels = 0
        self._set_rent()

    def _set_rent(self):
        """Calculate and set the value of the rent that is owed.
        """
        if self.hotels == 0:
            self.rent = self.base_rent * (self.houses + 1)
        else:
            self.rent = self.base_rent * 5

    def add_house(self):
        """Function to handle the addition of a house to the property.
        """
        self.houses += 1
        self._set_rent()
    
    def reset_house(self):
        """Function to handle the resetting of the properties' houses.
        """
        self.houses = 0
        self._set_rent()
    
    def add_hotel(self):
        """Function to handle the addition of a hotel to the property.
        """
        self.reset_house()
        self.hotels = 1
        self._set_rent()
    
    def reset_hotel(self):
        """Function to handle the resetting of the properties' hotels.
        """
        self.hotels = 0
        self._set_rent()

class RailStationProperty(BaseProperty):
    def __init__(self, position, name, price, rent):
        super().__init__(position, name, price, rent)

class UtilityProperty(BaseProperty):
    def __init__(self, position, name, price, rent):
        super().__init__(position, name, price, rent)
    

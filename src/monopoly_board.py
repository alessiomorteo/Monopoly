
class MonopolyBoard:
    def __init__(self):
        """Initialise the Monopoly board.
        """
        self.properties = []
        self.chance_cards = []
        self.community_chest_cards = []

    def add_property(self, property)->None:
        """Function to add a property to the board.

        Args:
            property: A property
        """
        self.properties.append(property)

    def get_property(self, name:str):
        """Getter function a property on the board.

        Args:
            name (str): The name of the property to be fetched.

        Returns:
            _type_: The monopoly property that was requested.
        """
        for property in self.properties:
            if property.name == name:
                return property
            return None
        
    def add_chance(self, card)->None:
        self.chance_cards.append(card)
    
    def add_community_chest(self, card)->None:
        self.community_chest_cards.append(card)

    def pick_card(self, card_type):
        if card_type == "chance":
            return self.__get_card(self.chance_cards)
        elif card_type == "community_chest":
            return self.__get_card(self.community_chest_cards)
        else:
            raise ValueError()

    def __get_card(self, card_type_list:list)->None:
        selected_card = self.card_type_list[:-1]
        # put the card to the bottom of the pile
        self.card_type_list.insert(0, self.card_type_list.pop(-1))
        return selected_card

        
    
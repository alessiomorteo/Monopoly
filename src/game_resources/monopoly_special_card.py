
class SpecialCard:
    def __init__(self, name:str, description: str)->None:
        """Initialise an instance of the SpecialCard to
        represent a card.

        Args:
            name (str): The name of the card
            description (str): The full description of the card.
        """
        self.name = name
        self.description = description

    def execute_card_action(self)->None:
        """Function for executing the action defined by the card.
        Includes actions such as financial and positional.
        """
        pass
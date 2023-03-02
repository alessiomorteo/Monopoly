
class MonopolyBoard:
    def __init__(self):
        """Initialise the Monopoly board.
        """
        self.properties = []

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
        
    
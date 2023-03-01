
class MonopolyBoard:
    def __init__(self):
        self.properties = []

    def add_property(self, property):
        self.properties.append(property)

    def get_property(self, name):
        for property in self.properties:
            if property.name == name:
                return property
            return None
        
    
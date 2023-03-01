class MonopolyProperty:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None

    def set_owner(self, owner):
        self.owner = owner

    def get_rent(self):
        pass

    

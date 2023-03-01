
class MonopolyPlayer:
    def __init__(self,name,starting_balance):
        self.name = name
        self.balance = starting_balance
        self.properties = []

    def buy_property(self, property):
        self.balance -= property.price
        self.properties.append(property)
        property.set_owner(self)

    def pay_rent(self, property, amount):
        self.balance -= amount
        property.owner.balance += amount

    def can_afford(self, amount):
        return self.balance >= amount
    
    
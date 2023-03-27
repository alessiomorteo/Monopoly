from monopoly_property import MonopolyProperty
from monopoly_bank import MonopolyBank

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
        self.active = True
        self.has_get_out_of_jail_card = False

    def player_status(self)->dict:
        """Gives a summary of the player's status.

        Returns:
            dict: A dictionary summarising the player's status
        """
        return {
            "player_name": self.name,
            "balance": self.balance,
            "active_status": self.active,
            "jail_release_card": self.has_get_out_of_jail_card
            }

    def buy_property(self, owner_obj:MonopolyBank, property_obj:MonopolyProperty)->bool:
        """Function to handle the purchase of a property by the player.

        Args:
            property_obj (MonopolyProperty): The property to be purchased.
        """
        if self.can_afford_purchase(property_obj.price):
            self.balance -= property_obj.price
            owner_obj.balance += property_obj.price
            property_obj.set_owner(self.name)
            return True
        else:
            print(f"The player's balance is insufficient to purchase the property.")
            return False

    def pay_rent(self, amount:int)->bool:
        """Function to handle the payment of rent.

        Args:
            amount (int): The value of the rent to be charged.
        
        Return:
            bool: A boolean to reflect the success of the operation.
        """
        payment_sent = self.debit_player(amount=amount)
        if not payment_sent:
            print(f"The player does not have a sufficient balance to pay the rent.")
            # Remove player from the game as balance hits zero
            self.inactivate_player_activity_status()
        
        return payment_sent

    def receive_rent(self, amount:int)->bool:
        """Function to handle the receipt of rent from another player.

        Args:
            amount (int): The value of the rent to be received.
        
        Returns:
            bool: Boolean to reflect the success of the operation.
        """
        received = self.credit_player(amount=amount)
        return received

    def credit_player(self, amount:int)->bool:
        """Function to increase the player's balance.

        Args:
            amount (int): The value of money to credit the player.
        
        Returns:
            bool: Boolean to reflect the success of the operation.
        """
        if amount > 0:
            self.balance += amount
            return True
        else:
            print("The balance to be credited must be greater than zero.")
            return False
    
    def debit_player(self, amount:int)->bool:
        """Function to decrease the player's balance.

        Args:
            amount (int): The value of money to credit the player.
        
        Returns:
            bool: Boolean to reflect the success of the operation.
        """
        if amount > 0:
            self.balance -= amount
            return True
        else:
            print("The balance to be debited must be greater than zero.")
            return False
        

    def can_afford_purchase(self, amount:int)->bool:
        """Function to check if the player can afford to purchase a property.

        Args:
            amount (int): The cost of the property that the player wishes to purchase.

        Returns:
            bool: Boolean to represent if can afford.
        """
        return self.balance > amount # balance can't hit zero
    
    def receive_get_out_of_jail_card(self):
        """Give the player a get out of jail free card.
        """
        self.has_get_out_of_jail_card = True
        return 
    
    def return_get_out_of_jail_card(self):
        """Take away the player's get out of jail free card.
        """
        if self.has_get_out_of_jail_card:
            self.has_get_out_of_jail_card = False
        return
    
    def inactivate_player_activity_status(self)->None:
        """Set the player's active status to False, i.e. out of the game. 
        """
        self.active = False
        return
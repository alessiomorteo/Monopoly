class MonopolyBank:
    def __init__(self):
        self.balance: int = 25000 # The bank starts with this amount
    
    def deposit(self, amount:int) -> None:
        """Function to handle a player depositing money into the bank. 

        Args:
            amount (int): The amount of money that a player wishes to deposit.
        """
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit failed. Amount must be positive.")

        
    def withdraw(self, amount: int) -> int:
        """Class function to withdraw money from the bank for a player.

        Args:
            amount (int): The desired amount of money required.

        Returns:
            int: The total amount of money provided.
        """
        if amount > self.balance:
            print("The bank does not have enough funds to complete this transaction.")
            return 0
        else:
            self.balance -= amount
            return amount
    
    def get_bank_balance(self) -> int:
        """Class function to get the funds available from the bank.

        Returns:
            int: The total balance available from the bank.
        """
        return self.balance
    
    def reset_bank_balance(self) -> None:
        """Resets the bank balance to its original value."""
        self.balance = 25000

    def __str__(self) -> str:
        """Returns a string representation of the bank balance.
        
        Returns:
            str: A formatted string presenting the bank's balance.
        """
        return f"Bank balance: {self.balance}"

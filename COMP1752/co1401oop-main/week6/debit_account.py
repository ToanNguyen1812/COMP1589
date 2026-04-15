
from account import Account


class DebitAccount(Account): 
    def __init__(self, acc_no, limit):
        super().__init__(acc_no)
        self.limit = limit
        self.debit = 0

    @property
    def debit(self):
        return self.__debit

    @property
    def limit(self):
        return self.__limit
    
    @limit.setter
    def limit(self, value):
        if value < 0:
            raise ValueError("Limit must be non-negative.")
        self.__limit = value

    # No need to override deposit method, it works the same as in Account

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance + self.limit:
            raise ValueError("Withdrawal exceeds balance and limit.")
        if amount > self.balance:
            self.__debit = amount - self.balance
            self.withdraw(self.balance)  # Withdraw all balance first
        else:
            super().withdraw(amount)  # Withdraw from balance

    def pay_debit(self, amount):
        if amount <= 0:
            raise ValueError("Payment amount must be positive.")
        if amount > self.debit:
            self.__debit = 0
            self.deposit(amount - self.debit)  # Pay off debit and deposit excess
        else:   
            self.__debit -= amount
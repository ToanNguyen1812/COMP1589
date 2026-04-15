class Account:
    def __init__(self, acc_no):
        self.acc_no = acc_no
        self.__balance = 0

    @property
    def acc_no(self):
        return self.__acc_no
    
    @acc_no.setter
    def acc_no(self, value):
        if value < 0:
            raise ValueError("Account number must be non-negative.")
        self.__acc_no = value

    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient balance.")
        self.__balance -= amount

    def __str__(self):
        return f"Account No: {self.acc_no}, Balance: ${self.balance:.2f}"
    
if __name__ == "__main__":
    acc = Account(12345)
    print(acc)
    acc.deposit(1000)
    print(acc)
    acc.withdraw(250)
    print(acc)

    # try invalid account number
    try:
        acc02 = Account(-1)
    except ValueError as e:
        print(e)

    # try invalid deposit
    try:
        acc.deposit(-500)
    except ValueError as e:
        print(e)

    # try invalid withdrawal
    try:
        acc.withdraw(1500)
    except ValueError as e:
        print(e)

    # invalid withdrawal amount
    acc.withdraw(-10)
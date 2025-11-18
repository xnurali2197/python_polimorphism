class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance.")
    
    def get_balance(self):
        return self.__balance



class SavingsAccount(BankAccount):
    def __init__(self, initial_balance=0, interest_rate=0.05):
        super().__init__(initial_balance)
        self.interest_rate = interest_rate
    
    def withdraw(self, amount):
        if amount <= self.get_balance():
            bonus = amount * self.interest_rate
            super().withdraw(amount)
            print(f"Savings account bonus (interest added): {bonus}")
        else:
            print("Insufficient balance in savings account.")


class CheckingAccount(BankAccount):
    def __init__(self, initial_balance=0, overdraft_limit=100):
        super().__init__(initial_balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount <= self.get_balance() + self.overdraft_limit:
            new_balance = self.get_balance() - amount

            if new_balance < 0:
                print(f"Overdraft used: {-new_balance}")
            super()._BankAccount__balance = new_balance
            print(f"Withdrew: {amount}")
        else:
            print("Exceeded overdraft limit.")



acc1 = SavingsAccount(1000)
acc2 = CheckingAccount(500)


accounts = [acc1, acc2]


for account in accounts:
    account.withdraw(200)
    print(f"Balance now: {account.get_balance()}\n")

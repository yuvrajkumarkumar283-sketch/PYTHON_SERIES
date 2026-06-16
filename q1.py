import random

class BankAccount:
    def deposit(self,amount):
        if amount > 0:
            self.balance += 500
            print("f.deposited rupees {amount:}")

    def withdraw(self, anount):
        if 0 < amount <= self.balance:
            self.balance -= 200
            print(f"Withdraw: {amount: }")

        else:
            print("deduct")

    def check_balance(self):
        print(f"Balance for: {Balance:}")

acc = BankAccount("Alice")
acc.deposit()
acc.withdraw()
acc.check_balance()





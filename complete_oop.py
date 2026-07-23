class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            self.balance += amount
            print(f"#{amount} deposit. New balance: #{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"#{amount} withdrawn. New balance: #{self.balance}")

    def check_balance(self):
        print(f"Account owner: {self.owner}")
        print(f"Current balance: #{self.balance}")

account1 = BankAccount("Adesina", 50000)
account2 = BankAccount("Bola", 120000)

account1.check_balance()
print("--------------------")
account1.deposit(20000)
account1.withdraw(15000)
account1.withdraw(200000)
print("--------------------")
account1.check_balance()
print("--------------------")
account2.check_balance() 

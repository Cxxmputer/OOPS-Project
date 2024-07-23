class BankAccount:
    # Using the 'init' constructor to initialize instances as soon as they are created.
    def __init__(self, name, balance=0):
        # Assigning the provided values to the instance's variable.
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        # Deposits money in the account ONLY if it is greater than or equal to zero.
        # Because what are you going to do with negative values. XD
        if amount >= 0:
            self.balance += amount
        else:
            print('Invalid funds!')

    def withdraw(self, amount):
        # Takes out the money from Account only if the amount is valid.
        # For instance, you have 100 Balance and you are withdrawing 1000; Are you okay?
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        # Prints the updated balance.
        print(f"Name: {self.name}, Balance: {self.balance}")


# Testing the template.
myAccount = BankAccount("David", 144)
myAccount.get_balance()
myAccount.deposit(15)
myAccount.get_balance()
myAccount.withdraw(150)
myAccount.get_balance()

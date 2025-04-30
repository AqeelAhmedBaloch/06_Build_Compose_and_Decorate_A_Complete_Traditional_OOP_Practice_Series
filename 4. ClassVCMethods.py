"""Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances."""

class Bank:
    bank_name = "Default Bank"  # Class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print("-" * 40)
        print("Bank Information:")
        print(f"Account Holder: {self.account_holder}, Bank: {Bank.bank_name}")

# Create instances
acc1 = Bank("Aqeel")
acc2 = Bank("Waseem")

# Display initial state
acc1.display()
acc2.display()

# Change bank name using class method
Bank.change_bank_name("Bank Al Habib")

# Display after change
acc1.display()
acc2.display()
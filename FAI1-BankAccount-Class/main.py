# BankAccount class
class BankAccount:

  # __init__() method
  def __init__(self, owner, ir):
    self.owner = owner
    self.balance = 0
    self.interest_rate = ir #as a decimal

  # instance methods
  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    if amount <= self.balance:
      self.balance -= amount
    else:
      print("Invalid Transaction: Not enough balance in account.")

  def calculate_interest(self):
    interest = self.balance*self.interest_rate
    self.balance += interest

  # __ str__() method
  def __str__(self):
    return "Owner: " + self.owner + "\nBalance: " + str(self.balance)

# test the Bank Account class
print("Creating BankAccount object...")
account1 = BankAccount("Bill", 0.10)
print(account1.owner)
print(account1.balance)
print(account1.interest_rate)
print(account1)
print()

print("Depositing $1000...")
account1.deposit(1000)
print(account1)
print()

print("Calculating Interest...")
account1.calculate_interest()
print(account1)
print()

print("Withdrawing $1000...")
account1.withdraw(1000)
print(account1)
print()

print("Withdrawing $150...")
account1.withdraw(150)
print(account1)
print()

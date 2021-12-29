#class
class Account:
  
  def __init__(self, filepath):
    self.filepath = filepath
    with open(filepath, "r") as file:
      self.balance = int(file.read())
      
  def withdraw(self, amount):
    self.balance = self.balance - amount
    
  def deposit(self, amount):
    self.balance = self.balance + amount
      
  def commit(self):
    with open(self.filepath, 'w') as file:
      file.write(str(self.balance))
    
    
account = Account("account//balance.txt")
print(account.balance)
account.withdraw(100)
print(account.balance)
account.deposit(400)
account.commit()
print(account.balance)


#class inheritance
class Checking(Account):
  
  def __init__(self, filepath):
      Account.__init__(self, filepath)
      
  def transfer(self, amount, fee):
      # self.fee = fee
      self.balance = self.balance - amount - fee
      
checking =Checking("account//balance.txt")
checking.deposit(10)
checking.commit()
checking.transfer(250, 1)
checking.commit()

print(checking.balance)
      
      

from abc import ABC


class VirtualWallet:

  def __init__(self):
    self.accounts = {}
  
  def create_account(self,username):
    if username in self.accounts.keys():
      raise Exception("Account already exists.")
    self.accounts[username]=0

  def deposit_money(self,username,amount):
    if username not in self.accounts.keys():
      raise Exception("Invalid username - Please create before an account.")
    if amount <= 0 :
      raise Exception("Negative amount - Invalid value.")
    self.accounts[username] += amount

  def withdrawal_money(self,username,amount):
    if username not in self.accounts.keys():
      raise Exception("Invalid username - Please create before an account.")
    if self.accounts[username] < amount:
      return False
    self.accounts[username] -= amount
    return True

  # por fines practicos la logica de un pago es la de una extraccion.
  def payment_transaction(self,username,amount):
    return self.withdrawal_money(username,amount)

  def get_balance_available(self,username):
    if username not in self.accounts.keys():
      raise Exception("Invalid username - Please create before an account.")
    return self.accounts[username]

  def delete_account(self,username):
    if username not in self.accounts.keys():
      raise Exception("Account did not exists.")
    if self.accounts[username] > 0:
      raise Exception("Can not delete, first withdrawal all the money.")
    del self.accounts[username]

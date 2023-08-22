#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.price_history = [0.0]
    self.transaction_history = []
  

  def add_item(self, item, price, quantity=1):
    self.items += [item] *quantity
    self.total += price*quantity
    self.transaction_history.append((item, price, quantity))
  
  # def get_total(self):
  #   return sum([transaction[1]*transaction[2] for transaction in self.transaction_history])

  # def set_total(self,_):
  #   pass
  
  # total = property(get_total, set_total)


  def apply_discount(self):
    if self.discount > 0:
      self.total -= self.total * self.discount / 100
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    last_transaction = self.transaction_history.pop()
    price = last_transaction[1]
    quantity = last_transaction[2]
    self.total -= price*quantity
    for i in range(quantity):
      self.items.pop()
    pass

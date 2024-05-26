#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
    def add_item(self, title, price, quantity=1):
        # Add item to the register and update total
        self.items.append((title, price, quantity))
        self.total += price * quantity
    def add_item(self, item, price, quantity=1):
        # Add item to the register and update total
        self.items.append((item, price, quantity))
        self.total += price * quantity
        self.last_transaction_amount = price * quantity

    def apply_discount(self):
        # Apply discount to the total
        if self.discount > 0:
           discount_amount = (self.discount / 100) * self.total
           self.total -= discount_amount
           print(f"After the discount, the total comes to ${self.total:.2f}.")
           return self.total
        else:
           return "No discount applied."

    def void_last_transaction(self):
        # Remove last transaction from the total
        if self.last_transaction_amount > 0:
            self.total -= self.last_transaction_amount
            self.last_transaction_amount = 0
        else:
            return "No transactions to void."

pass

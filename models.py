class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def add_stock(self, amount):
        self.quantity += amount
        print(f"{amount} items added. New quantity: {self.quantity}")

    def remove_stock(self, amount):
        if amount > self.quantity:
            print("Lesser quantity detected.")
        else:
            self.quantity -= amount
            print(f"{amount} items removed. Remaining quantity: {self.quantity}")

    def display_info(self):
        print("Item Information")
        print(f"Name: {self.name}")
        print(f"Quantity: {self.quantity}")
        print(f"Price: ${self.price}")
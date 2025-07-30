# order.py

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total_price(self):
        return sum([item.price for item in self.items])

    def display_order(self):
        return "\n".join([item.display() for item in self.items])

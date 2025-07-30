# menu_items.py

class MakeupItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        return f"{self.name} - ${self.price}"

class Lipstick(MakeupItem):
    def __init__(self, name, price):
        super().__init__(name, price)

class Foundation(MakeupItem):
    def __init__(self, name, price):
        super().__init__(name, price)

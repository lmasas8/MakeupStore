# menu_items.py
# by: Almas Yahya Ali 443805688 , Noura mohaya 445803907 , Hanin Omar 444806869 , Ghaida Saeed 444810066

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

class Inventory:

    def __init__(self):
        self.inv = {}

    def set_item_quantity(self, item_type, quantity):
        self.inv[item_type] = quantity

    def add_items(self, item_type, quantity):
        if item_type in self.inv:
            self.inv[item_type] = self.inv[item_type] + quantity
        else:
            self.set_item_quantity(item_type, quantity)

    def get_item_quantity(self, item_type) -> int:
        return self.inv[item_type]
class Market: 

    def __init__(self, market_id: int, name: str):
        self.market_id = market_id
        self.name = name
        self.storage = {}

    def add_item(self, item, quantity):
        if item in self.storage:
            self.storage[item] += quantity
        else:
            self.storage[item] = quantity

    def remove_item(self, item, quantity):
        if item in self.storage:
            if self.storage[item] >= quantity:
                self.storage[item] -= quantity
            else:
                print(f"Not enough {item} in storage.")
        else:
            print(f"{item} not found in storage.")
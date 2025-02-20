class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
        self.items = {}
        self.hunger = 0

    def work(self):
        if self.job == "Engineer":
            self.add_item("Gadget", 1)
        elif self.job == "Farmer":
            self.add_item("Raw_food", 1)

        self.hunger += 1

    def eat(self):
        pass

    def market_visit(self):
        pass


    def set_age(self):
        self.age += 1

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, Job: {self.job}, Items: {self.items}")

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, job={self.job})"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and self.job == other.job

    def __hash__(self):
        return hash((self.name, self.age, self.job))
    
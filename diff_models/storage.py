class Storage:
    def __init__(self):
        # Initialize an empty list
        self.persons = []
        

    def add_person(self, person):
        """Adds an person to the list."""
        self.persons.append(person)

    def get_average_age(self):
        """Calculates the average age of all persons in the list."""
        if self.persons:
            total_age = sum(person.age for person in self.persons)
            return total_age / len(self.persons)

    def remove_person(self, person):
        """Removes an person from the list if it exists."""
        if person in self.persons:
            self.persons.remove(person)
        else:
            print(f"Person '{person}' not found in storage.")

    def display_persons(self):
        """Displays all the persons in the list."""
        if self.persons:
            print("Persons in storage:")
            for person in self.persons:
                print(person)



    def age_persons(self):
        if self.persons:
            for person in self.persons:
                person.set_age()

        else:
            print("Storage is empty.")



    def do_work(self):
        if self.persons:
            for person in self.persons:
                person.work()

                person.eat()
                
                if person.hunger > 50:
                    
                    self.remove_person(person)
                    print("Person died of hunger.")

        else:
            print("Storage is empty.")


    def get_raw_food(self):
        
        if self.persons:
            total_raw_food = sum(person.items.get("Raw_food", 0) for person in self.persons)
            print(f"Total Raw Food: {total_raw_food}")
            return total_raw_food

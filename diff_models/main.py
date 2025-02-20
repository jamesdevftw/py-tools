import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import random


import person
import storage
import market

s1 = storage.Storage()
m1 = market.Market(1, "Market 1")
age_list = []
food_list = []
jobs = ["Engineer", "Farmer", "Teacher", "Artist", "Writer", "Scientist", "Lawyer", "Chef", "Athlete", "Musician"]
food = {"Raw_food": 0, "Cooked_food": 0, "Gadget": 0}   

def main():

    p1 = person.Person("Alice", 30, "Engineer")
    p2 = person.Person("Tyler", 20, "Cook")

    p1.add_item("Apple", 10)

    s1.add_person(p1)
    s1.add_person(p2)

    loop(1000)


def loop(n):
    for i in range(n):
        birth = random.random() > 0.75  # 25% chance of birth

        if birth:  # If there is a birth, add a new person to the storage
            name = "Person" + str(random.randint(1, 100))  # Random name
            age = random.randint(0, 1)
            job = jobs[random.randint(0, len(jobs) - 1)]

            s1.add_person(person.Person(name, age, job))


        do_work()
        market_visit()
        age_people()

        food['Raw_food'] += s1.get_raw_food()

        food_list.append(food["Raw_food"])

        age_list.append(s1.get_average_age())

    age_graph()
    raw_food_graph()


def age_graph():
    sns.lineplot(x=[len(age_list[:i+1]) + 1 for i in range(len(age_list))], y=age_list)
    plt.title('Average age over time')
    plt.show()

def raw_food_graph():
    sns.lineplot(x=[len(age_list[:i+1]) + 1 for i in range(len(age_list))], y=food_list)
    plt.title('Raw food storage')
    plt.show()


def age_people():
    s1.age_persons() 

def do_work():
    s1.do_work()

def market_visit():
    s1.market_visit()

main()
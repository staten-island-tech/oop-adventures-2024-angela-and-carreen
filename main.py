import json
import os

class main_charater:
    def __init__ (self, name, health= 100, currency=25):
        self.name = name
        self.health = health
        self.currency = currency
        self.inventory = []
    def user_input():
        user_name = input("Enter your character's name: ")
        return main_charater(user_name)
name = main_charater.user_input()

with open("./saves.json", "r") as f:
    data = json.load(f)
    data.append(name.__dict__)
new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data)
    f.write(json_string)
os.remove("saves.json")
os.rename(new_file, "saves.json")

""" def take_damage(self, damage):
        reduced_damage = max(damage - self.defense, 0)
        self.health -= reduced_damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} takes {reduced_damage} damage, {self.health} health remaining.") """
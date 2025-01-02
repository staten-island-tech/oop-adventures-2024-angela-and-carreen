import json
import classes
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
    def choosing_charater():
        charater_list = ("Archer", "Knight", "mage", "Healer")
        for idx, (charater) in enumerate(charater_list):
            print(f"{idx}.{charater}")
        try:
            choice = int(input("\n Enter the number corresponding to the class to choose it: "))
            
        except ValueError:
            print("Please enter a valid number.")

char = main_charater.user_input()

with open("./saves.json", "r") as f:
    data = json.load(f)
    data.append(char.__dict__)
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
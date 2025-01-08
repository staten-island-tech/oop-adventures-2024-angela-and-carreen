""" import user
import monster
import npcs
import items
import random

class Player:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has fallen in battle!")
        else:
            print(f"{self.name} now has {self.health} health left")
    def attack(self, monster):
        if self.weapon.durability > 0:
            damage = self.weapon.damage
            print(f"{self.name} attacks with {self.weapon.name} for {damage} damage!")
            self.weapon.durability -= 1
            monster.take_damage(damage)
        else:
            print(f"{self.weapon.name} is broken and cannot be used!")
    def collect_drops(self, drops):
        if drops:
            self.inventory.extend(drops)
            print(f"{self.name} collected the following items:")
            for item in drops:
                print(f"- {item}")
        else:
            print("No items to collect.")

def intro():
    choice = int(input('"do you want to go to \n1: forest \n2: village?"'))
    if choice == 1:
        enter_forest
    elif choice == 2:
        enter_village
    else:
        print('CHOOSE A VALID CHOICE')
def forest():
    print('You enter the forest and encounter a slime') """



""" import json
with open("./saves.json", "r") as f:
    data = json.load(f)
    data.append()
new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data, indent=4)
    f.write(json_string)
os.remove("saves.json")
os.rename(new_file, "saves.json") """
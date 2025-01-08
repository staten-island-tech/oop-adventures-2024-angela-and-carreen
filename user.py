from classes import Archer, Knight, Mage, Healer
import os
import json
import monster
from items import Weapons
from npcs import StoreClerk, Innkeeper, Trader
import random
class MainCharacter:
    def __init__(self, name, character_class, health=100, currency=25):
        self.name = name
        self.character_class = character_class
        self.health = health
        self.currency = currency
        self.inventory = []
    def user_input():
        user_name = input("Enter your character's name: ")
        return user_name
    def choosing_character():
        print("Choose your character class:")
        character_classes = {1: "Archer", 2: "Knight", 3: "Mage", 4: "Healer"}
        for idx, char_class in character_classes.items():
            print(f"{idx}: {char_class}")
        while True:
            try:
                choice = int(input("Enter the number corresponding to your choice: "))
                if choice in character_classes:
                    return character_classes[choice]
                else:
                    print("Invalid choice. Please choose a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    def create_character(name, character_class):
        character_mapping = {
            "Archer": Archer(name, mana=50, arrows=10, defense=5, inventory=("Lamp", "Map", "Arrow", "Bow")),
            "Knight": Knight(name, mana=30, defense=10, attacks=10, inventory=("Lamp", "Map", "Sword", "Shield")),
            "Mage": Mage(name, mana=70, defense=3, attacks=5, inventory=("Lamp", "Map")),
            "Healer": Healer(name, mana=60, defense=4, inventory=("Lamp", "Map"))}
        return character_mapping.get(character_class, None)
user_name = MainCharacter.user_input()
chosen_class = MainCharacter.choosing_character()
player_character = MainCharacter.create_character (user_name, chosen_class)
character_data = {"stats": player_character.__dict__,}
def monster_list():
    Monsters = [Monster("Werewolf", 100, 25, {"werewolf fur", "werewolf claws", "55 gold coins"}),
    Monster("Goblin", 50, 5, {"goblin skin", "wooden shield", "5 gold coins"}),
    Monster("Skeleton", 30, 10, {"bones", "rusty sword", "3 gold coins"}),
    Monster("Slime", 15, 1, {"1 gold coin"}),
    Monster("Dragon", 150, 80, {"dragon scales", "dragon tooth", "dragon heart", "100 gold coins"})]

def intro():
    print(f"\nWelcome, {player_character.name}!\nYou have chosen the {chosen_class} class.")
    print(f"Your starting stats are:\nHealth: {player_character.health}\nCurrency: {player_character.currency}\nInventory: {player_character.inventory}\n")
    choice = int(input("do you want to go to \n1: forest \n2: village?\n"))
    if choice == 1:
        print("you enter the forest...\nyou encounter a slime")
        if self.weapon.durability > 0:
            damage = self.weapon.damage
            print(f"{self.name} attacks with {self.weapon.name} for {damage} damage!")
            self.weapon.durability -= 1
            monster.take_damage(damage)
        else:
            print(f"{self.weapon.name} is broken and cannot be used!")
        if drops:
            self.inventory.extend(drops)
            print(f"{self.name} collected the following items:")
            for item in drops:
                print(f"- {item}")
        else:
            print("No items to collect.")
    elif choice == 2:
        print("you enter village...\n do you want to go to the inn or the armory")
        store=int(input("1: armory \n2: inn\n"))
        if store == 1:
            store_clerk = StoreClerk("Mia", 50, [('lamp', 5), ('Map', 3), ('sword', 15), ('shield', 10), ('bow', 15), ('arrows', 1)])
            store_clerk.interact(player_character)
        elif store==2:
            innkeeper = Innkeeper("Alya", 0, 15)
            innkeeper.interact(player_character)
    else:
        print('CHOOSE A VALID CHOICE')
intro()

with open("./saves.json", "r") as f:
    data = json.load(f)
    data.append(character_data)
new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data, indent=4)
    f.write(json_string)
os.remove("saves.json")
os.rename(new_file, "saves.json")
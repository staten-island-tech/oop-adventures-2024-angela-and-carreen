import json
from classes import Archer, Knight, Mage, Healer
import os
class MainCharacter:
    def __init__(self, name, character_class, health, currency):
        self.name = name
        self.character_class = character_class
        self.health = health
        self.currency = currency
        self.inventory = []
    health=100
    currency=25
    def user_input():
        user_name = input("Enter your character's name: ")
        return user_name
    def choosing_character():
        print("Choose your character class:")
        character_classes = {
            1: "Archer",
            2: "Knight",
            3: "Mage",
            4: "Healer"}
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
        if character_class == "Archer":
            return Archer(name, mana=50, arrows=10, defense=5)
        elif character_class == "Knight":
            return Knight(name, mana=30, defense=10, attacks=10)
        elif character_class == "Mage":
            return Mage(name, mana=70, defense=3, attacks=5)
        elif character_class == "Healer":
            return Healer(name, mana=60, defense=4)
        else:
            raise ValueError("Invalid character class selected.")

user_name = MainCharacter.user_input()
chosen_class = MainCharacter.choosing_character()
player_character = MainCharacter.create_character(user_name, chosen_class, health, currency, inventory)
character_data = {
    "name": player_character.name,
    "class": chosen_class,
    "stats": player_character.__dict__}
with open("./saves.json", "r") as f:
    data = json.load(f)
    data.append(character_data)
new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data, indent=4)
    f.write(json_string)
os.remove("saves.json")
os.rename(new_file, "saves.json")
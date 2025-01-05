from classes import Archer, Knight, Mage, Healer
import os
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
print(f"\nWelcome, {player_character.name}!\nYou have chosen the {chosen_class} class.")
print(f"Your starting stats are:\nHealth: {player_character.health}\nCurrency: {player_character.currency}\nInventory: {player_character.inventory}\n")
character_data = {"stats": player_character.__dict__,}
import json
with open("./saves.json", "r") as f:
    data = json.load(f)
    data.append(character_data)
new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data, indent=4)
    f.write(json_string)
os.remove("saves.json")
os.rename(new_file, "saves.json")
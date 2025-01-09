from classes import Archer, Knight, Mage, Healer
from monster import Monster
from items import Weapons
from npcs import StoreClerk, Innkeeper, Trader
import json
import os
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
def weapons():
    weapons_list = [
        Weapons("Sword", 15, 50, 20, "Common", "N/A", "N/A"),
        Weapons("Shield", 10, 75, 0, "Common", "N/A", "N/A"),
        Weapons("Bow", 15, 100, 0, "Common", "N/A", "N/A"),
        Weapons("Arrows", 1, 5, 10, "Common", "N/A", "N/A"),
        Weapons("Staff", 10, 100, 5, "Common", "N/A", "N/A")]
    return weapons(weapons_list)
def generate_random_monster():
    monster_list = [
        Monster("Werewolf", 100, 25, {"werewolf fur", "werewolf claws", "55 gold coins"}),
        Monster("Goblin", 50, 5, {"goblin skin", "wooden shield", "5 gold coins"}),
        Monster("Skeleton", 30, 10, {"bones", "rusty sword", "3 gold coins"}),
        Monster("Slime", 15, 1, {"1 gold coin"})]
    return random.choice(monster_list)
def generate_cave_monster():
    monster_list = [
        Monster("Werewolf", 200, 25, {"werewolf fur", "werewolf claws", "55 gold coins"}),
        Monster("Goblin", 100, 5, {"goblin skin", "wooden shield", "5 gold coins"}),
        Monster("Skeleton", 60, 10, {"bones", "rusty sword", "3 gold coins"}),
        Monster("Slime", 30, 1, {"1 gold coin"}),
        Monster("Dragon", 300, 99, {"dragon scales", "dragon tooth", "dragon heart", "100 gold coins"})]
    return random.choice(monster_list)
def intro():
    print(f"\nWelcome, {player_character.name}!\nYou have chosen the {chosen_class} class.")
    print(f"Your starting stats are:\nHealth: {player_character.health}\nCurrency: {player_character.currency}\nInventory: {player_character.inventory}\n")
    choice = int(input("do you want to go to \n1: forest \n2: village?\n"))
    if choice == 1:
        print('You enter the forest and encounter a slime')
        monster = Monster("Slime", 15, 1, {"1 gold coin"})
        while monster.health > 0 and player_character.health > 0:
            action = input("Do you want to [attack] the monster or [run]? ").lower()
            if action == "attack":
                if player_character.weapon.durability > 0:
                    damage = player_character.weapon.damage
                    print(f"{player_character.name} attacks with {player_character.weapon.name} for {damage} damage!")
                    player_character.weapon.durability -= 1
                    monster.take_damage(damage)
                else:
                    print(f"{player_character.weapon.name} is broken and cannot be used!")
                if monster.health > 0:
                    monster.attack(player_character)
                    self.health -= damage
                    if self.health <= 0:
                        print(f"{self.name} has fallen in battle!")
                    else:
                        print(f"{self.name} now has {self.health} health left")
            elif action == "run":
                print("You fled from the battle!")
                break
            else:
                print("Invalid choice. Try again.")
        if monster.health <= 0:
            print(f"You defeated the {monster.name}!")
            print(f"The {monster.name} dropped: {', '.join(monster.drops)}")
            player_character.inventory.extend(monster.drops)
            print(f"Your updated inventory: {player_character.inventory}")
        elif player_character.health <= 0:
            print("You have been defeated!")
        while player_character.health > 0:
            next_monster = generate_random_monster()
            print(f"A wild {next_monster.name} appears!")
            while next_monster.health > 0 and player_character.health > 0:
                action = input("Do you want to [attack] the monster or [run]? ").lower()
                if action == "attack":
                    if player_character.weapon.durability > 0:
                        damage = player_character.weapon.damage
                        print(f"{player_character.name} attacks with {player_character.weapon.name} for {damage} damage!")
                        player_character.weapon.durability -= 1
                        monster.take_damage(damage)
                    else:
                        print(f"{player_character.weapon.name} is broken and cannot be used!")
                    if monster.health > 0:
                        monster.attack(player_character)
                        self.health -= damage
                        if self.health <= 0:
                            print(f"{self.name} has fallen in battle!")
                        else:
                            print(f"{self.name} now has {self.health} health left")
                elif action == "run":
                    print("You fled from the battle!")
                    break
                else:
                    print("Invalid choice. Try again.")
            if next_monster.health <= 0:
                print(f"You defeated the {next_monster.name}!")
                print(f"The {next_monster.name} dropped: {', '.join(next_monster.drops)}")
                player_character.inventory.extend(next_monster.drops)
                print(f"Your updated inventory: {player_character.inventory}")
            elif player_character.health <= 0:
                print("You have been defeated!")
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

""" def save_game():
    try:
        with open("saves.json", 'r') as file:
            player_data=json.load(file)
    except FileNotFoundError:
        player_data={"name": user_name, "health": 100, "inventory": []}
    with open('saves.json', 'w') as file:
        json.dump(player_data, file, indent=4) """


""" with open("./saves.json", "r") as f:
    data = json.load(f)
    data.append()
new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data, indent=4)
    f.write(json_string)
os.remove("saves.json")
os.rename(new_file, "saves.json") """
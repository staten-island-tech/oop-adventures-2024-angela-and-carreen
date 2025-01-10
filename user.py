from classes import Archer, Knight, Mage, Healer
from monster import Monster
from items import Weapons
from npcs import StoreClerk, Innkeeper, Trader
import json
import os
import random
import time
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
            "Archer": Archer(name, mana=50, defense=5, arrows=10, inventory=["Lamp", "Map", "Arrow", "Bow"]),
            "Knight": Knight(name, mana=30, defense=10, inventory=["Lamp", "Map", "Sword", "Shield"]),
            "Mage": Mage(name, mana=70, defense=3, inventory=["Lamp", "Map"]),
            "Healer": Healer(name, mana=60, defense=4, inventory=["Lamp", "Map"])}
        player = character_mapping.get(character_class, None)
        if player:
            if character_class == "Archer":
                player.weapon = Weapons("Bow", price=15, durability=100, damage=10, rarity="Common", effect="N/A", effect_duration="N/A")
            elif character_class == "Knight":
                player.weapon = Weapons("Sword", price=15, durability=50, damage=20, rarity="Common", effect="N/A", effect_duration="N/A")
            elif character_class == "Mage":
                player.weapon = Weapons("Staff", price=10, durability=50, damage=5, rarity="Common", effect="N/A", effect_duration="N/A")
            elif character_class == "Healer":
                player.weapon = None
        return player
user_name = MainCharacter.user_input()
chosen_class = MainCharacter.choosing_character()
player_character = MainCharacter.create_character (user_name, chosen_class)
character_data = {"stats": player_character.__dict__,}
def generate_random_monster():
    monster_list = [
        Monster("Werewolf", 100, 25, {"werewolf fur", "werewolf claws", "55 gold coins"}),
        Monster("Goblin", 50, 5, {"goblin skin", "wooden shield", "5 gold coins"}),
        Monster("Skeleton", 30, 10, {"bones", "rusty sword", "3 gold coins"}),
        Monster("Slime", 15, 1, {"1 gold coin"})]
    return random.choice(monster_list)
def generate_cave_monster():
    cave_monster_list = [
        Monster("Werewolf", 200, 25, {"werewolf fur", "werewolf claws", "55 gold coins"}),
        Monster("Goblin", 100, 5, {"goblin skin", "wooden shield", "5 gold coins"}),
        Monster("Skeleton", 60, 10, {"bones", "rusty sword", "3 gold coins"}),
        Monster("Slime", 30, 1, {"1 gold coin"}),
        Monster("Dragon", 300, 99, {"dragon scales", "dragon tooth", "dragon heart", "100 gold coins"})]
    return random.choice(cave_monster_list)
def intro():
    print(f"\nWelcome, {player_character.name}!\nYou have chosen the {chosen_class} class.")
    print(f"Your starting stats are:\nHealth: {player_character.health}\nCurrency: {player_character.currency}\nInventory: {player_character.inventory}\n")
    choice = int(input("do you want to go to \n1: forest \n2: village?\n"))
    if choice == 1:
        print('You enter the forest and encounter a slime')
        forest_start_time = time.time()
        monster = Monster("Slime", 15, 1, {"1 gold coin"})
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
                player_character.health -= damage
                if player_character.health <= 0:
                    print(f"{player_character.health} has fallen in battle!")
                else:
                    print(f"{player_character.health} now has {player_character.health} health left")
        elif action == "run":
            print("You fled from the battle!")
        else:
            print("Invalid choice. Try again.")
        if monster.health <= 0:
            print(f"You defeated the {monster.name}!\nThe {monster.name} dropped: {', '.join(monster.drops)}\n")
            player_character.inventory.extend(monster.drops)
            print(f"Your updated inventory: {player_character.inventory}\n")
        elif player_character.health <= 0:
            print("You have been defeated!")
        while player_character.health > 0:
            next_monster = generate_random_monster()
            print(f"A wild {next_monster.name} appears!")
            while next_monster.health > 0 and player_character.health > 0:
                action = input(f"Do you want to [attack] {next_monster.name} or [run]? ").lower()
                if action == "attack":
                    if player_character.weapon.durability > 0:
                        damage = player_character.weapon.damage
                        print(f"{player_character.name} attacks with {player_character.weapon.name} for {damage} damage!")
                        player_character.weapon.durability -= 1
                        next_monster.take_damage(damage)
                    else:
                        print(f"{player_character.weapon.name} is broken and cannot be used!")
                    if next_monster.health > 0:
                        next_monster.attack(player_character)
                        player_character.health -= damage
                        if player_character.health <= 0:
                            print(f"{player_character.health} has fallen in battle!")
                        else:
                            print(f"{player_character.health} now has {player_character.health} health left")
                elif action == "run":
                    print("You fled from the battle!")
                else:
                    print("Invalid choice. Try again.")
                if next_monster.health <= 0:
                    print(f"You defeated the {next_monster.name}!\nThe {next_monster.name} dropped: {', '.join(next_monster.drops)}\n")
                    player_character.inventory.extend(next_monster.drops)
                    print(f"Your updated inventory: {player_character.inventory}\n")
                elif player_character.health <= 0:
                    print("You have been defeated!")
            elapsed_time = time.time()-forest_start_time
            if elapsed_time > 120:
                cave_choice = input("Do you want to go into the cave? [yes/no] ").lower()
                if cave_choice == "yes":
                    cave_monster = generate_cave_monster()
                    print(f"A {cave_monster.name} appears in the cave!")
                    while cave_monster.health > 0 and player_character.health > 0:
                        action = input("Do you want to [attack] the monster or [run]? ").lower()
                        if action == "attack":
                            if player_character.weapon.durability > 0:
                                damage = player_character.weapon.damage
                                print(f"{player_character.name} attacks with {player_character.weapon.name} for {damage} damage!")
                                player_character.weapon.durability -= 1
                                cave_monster.take_damage(damage)
                            else:
                                print(f"{player_character.weapon.name} is broken and cannot be used!")
                            if cave_monster.health > 0:
                                cave_monster.attack(player_character)
                                player_character.health -= cave_monster.attack_power
                                if player_character.health <= 0:
                                    print(f"{player_character.name} has fallen in battle!")
                                else:
                                    print(f"{player_character.name} now has {player_character.health} health left")
                        elif action == "run":
                            print("You fled from the cave!")
                        else:
                            print("Invalid choice. Try again.")
                    if cave_monster.health <= 0:
                        print(f"You defeated the {cave_monster.name}!")
                        print(f"The {cave_monster.name} dropped: {', '.join(cave_monster.drops)}")
                        player_character.inventory.extend(cave_monster.drops)
                        print(f"Your updated inventory: {player_character.inventory}")
                    elif player_character.health <= 0:
                        print("You have been defeated!")
                elif cave_choice == "no":
                    print("You decide not to enter the cave and continue your journey.")
                else:
                    print("Invalid choice. Please enter 'yes' or 'no'.")
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
from classes import Archer, Knight, Mage, Healer
from monster import Monster, Next_monster, Cave_monster
from items import Weapons
from npcs import StoreClerk, Innkeeper, Trader
import json
import os
import random
import time
class MainCharacter:
    def __init__(self, name, character_class, health=100, gold=25):
        self.name = name
        self.character_class = character_class
        self.health = health
        self.gold = gold
        self.inventory = []
        self.weapon = None
    def attack(self, monster):
        if self.weapon and self.weapon.durability > 0:
            damage = self.weapon.damage
            self.weapon.durability -= 1
        else:
            damage = 3
        monster.take_damage(damage)
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
            "Archer": Archer(name, mana=100, defense=5, arrows=10, inventory=["Lamp", "Map", "Arrow", "Bow"]),
            "Knight": Knight(name, mana=60, defense=10, inventory=["Lamp", "Map", "Sword", "Shield"]),
            "Mage": Mage(name, mana=140, defense=3, inventory=["Lamp", "Map", "staff"]),
            "Healer": Healer(name, mana=120, defense=4, inventory=["Lamp", "Map", "Dagger"])}
        player = character_mapping.get(character_class, None)
        if player:
            if character_class == "Archer":
                player.weapon = Weapons("Bow", price=15, durability=100, damage=15, rarity="Common", effect="N/A", effect_duration="N/A")
            elif character_class == "Knight":
                player.weapon = Weapons("Sword", price=20, durability=50, damage=20, rarity="Common", effect="N/A", effect_duration="N/A")
            elif character_class == "Mage":
                player.weapon = Weapons("Staff", price=10, durability=50, damage=10, rarity="Common", effect="N/A", effect_duration="N/A")
            elif character_class == "Healer":
                player.weapon = Weapons("Dagger", price=5, durability=25, damage=5, rarity="Common", effect="N/A", effect_duration="N/A")
        return player
user_name = MainCharacter.user_input()
chosen_class = MainCharacter.choosing_character()
player_character = MainCharacter.create_character(user_name, chosen_class)
character_data = {"stats": player_character.__dict__,}
def enter_cave(player_character):
    print("\nYou cautiously enter the dark cave.")
    cave_monster = generate_cave_monster()
    print(f"A {cave_monster.name} appears in the cave!\n{cave_monster.name} has {cave_monster.health} health.")
    while cave_monster.health > 0 and player_character.health > 0:
        action = input("Do you want to [attack] the monster or [run] (running will take you out of the cave)? ").lower()
        if action == "attack":
            while cave_monster.health > 0:
                try:
                    print(f'You have {player_character.mana} mana')
                    if isinstance(player_character, Archer):
                        print("Choose your arrow type:\n1: Standard mana cost:0 \n2: Fire mana cost:7 \n3: Poison mana cost 5")
                        arrow_choice = int(input("Enter your choice: "))
                        player_character.attack(cave_monster, arrow_choice)
                    elif isinstance(player_character, Knight):
                        print("Choose your attack type:\n1: Slash mana cost:0 \n2: Charge Attack mana cost:10\n3: Power Slash mana: 15")
                        attack_choice = int(input("Enter your choice: "))
                        player_character.attack(cave_monster, attack_choice)
                    elif isinstance(player_character, Mage):
                        print("Choose your spell:\n1: Fireball mana cost 10\n2: Frostbolt mana cost 10")
                        spell_choice = int(input("Enter your choice: "))
                        player_character.attack(cave_monster, spell_choice)
                    elif isinstance(player_character, Healer):
                        player_character.attack(cave_monster)
                    if cave_monster.health > 0:
                        cave_attack = cave_monster.attack
                        player_character.health -= cave_attack
                        print(f"{cave_monster.name} attacks {player_character.name} for {cave_attack} damage")
                        if player_character.health <= 0:
                            print(f"{player_character.name} has fallen in battle!")
                            break
                        else:
                            print(f"{cave_monster.name} attacked {player_character.name} for {cave_monster.attack}\n{player_character.name} now has {player_character.health} health left")
                except ValueError:
                    print("Invalid choice. Please enter a number.")
        elif action == "run":
            print("You fled from the cave!")
        else:
            print("Invalid choice. Try again.")
    if cave_monster.health <= 0:
        print(f"You defeated the {cave_monster.name}!")
        gold_dropped = 0
        updated_drops = []
        for drop in cave_monster.drops:
            if "gold" in drop:
                try:
                    gold_value = int(drop.split()[0])
                    gold_dropped += gold_value
                except ValueError:
                    print()
            else:
                updated_drops.append(drop)
            player_character.gold += gold_dropped
        print(f"The {cave_monster.name} dropped: {', '.join(updated_drops)} and {gold_dropped} gold!")
        player_character.inventory.extend(updated_drops)
        print(f"Your updated inventory: {player_character.inventory}")
        print(f"Your total gold: {player_character.gold}")
    elif player_character.health <= 0:
        print("You have been defeated!")
def generate_random_monster():
    monster_list = [
        Next_monster("Slime", 15, 1, {"2 gold"}),
        Next_monster("Werewolf", 100, 15, {"werewolf fur", "werewolf claws", "55 gold"}),
        Next_monster("Goblin", 50, 8, {"goblin skin", "wooden shield", "5 gold"}),
        Next_monster("Skeleton", 30, 5, {"bones", "rusty sword", "3 gold"}),
        Next_monster("Orc", 80, 12, {"orc skin", "orc axe", "15 gold"}),
        Next_monster("Troll", 120, 10, {"troll skin", "troll club", "30 gold"})]
    return random.choice(monster_list)
def generate_cave_monster():
    cave_monster_list = [
        Cave_monster("Bat", 10, 2, {"bat wing", "1 gold"}),
        Cave_monster("Slime", 30, 1, {"2 gold"}),
        Cave_monster("Werewolf", 100, 25, {"werewolf fur", "werewolf claws", "55 gold"}),
        Cave_monster("Goblin", 50, 15, {"goblin skin", "wooden shield", "5 gold"}),
        Cave_monster("Skeleton", 30, 10, {"bones", "rusty sword", "3 gold"}),
        Cave_monster("Orc", 80, 25, {"orc skin", "orc axe", "15 gold"}),
        Cave_monster("Troll", 120, 20, {"troll skin", "troll club", "30 gold"}),
        Cave_monster("Spider", 20, 5, {"spider silk", "spider venom", "2 gold"}),
        Cave_monster("Dragon", 300, 99, {"dragon scales", "dragon tooth", "dragon heart", "100 gold"})]
    return random.choice(cave_monster_list)
def intro():
    print(f"\nWelcome, {player_character.name}!\nYou have chosen the {chosen_class} class.")
    print(f"Your starting stats are:\nHealth: {player_character.health}\nGold: {player_character.gold}\nInventory: {player_character.inventory}\n")
    while True:
        try:
            choice = int(input("do you want to go to \n1: forest \n2: village?\n"))
            if choice == 1:
                print('You enter the forest and encounter a slime')
                forest_start_time = time.time()
                monster = Monster("Slime", 15, 1, {"2 gold"})
                while monster.health > 0 and player_character.health > 0:
                    action = input("Do you want to [attack] the monster or [run]? ").lower()
                    if action == "attack":
                        while monster.health > 0:
                            try:
                                print(f'you have {player_character.mana} mana')
                                if isinstance(player_character, Archer):
                                    print("Choose your arrow type:\n1: Standard mana cost:0 \n2: Fire mana cost:7 \n3: Poison mana cost 5")
                                    arrow_choice = int(input("Enter your choice: "))
                                    player_character.attack(monster, arrow_choice)
                                elif isinstance(player_character, Knight):
                                    print("Choose your attack type:\n1: Slash mana cost:0 \n2: Charge Attack mana cost:10\n3: Power Slash mana: 15")
                                    attack_choice = int(input("Enter your choice: "))
                                    player_character.attack(monster, attack_choice)
                                elif isinstance(player_character, Mage):
                                    print("Choose your spell:\n1: Fireball mana cost 10\n2: Frostbolt mana cost 10")
                                    spell_choice = int(input("Enter your choice: "))
                                    player_character.attack(monster, spell_choice)
                                elif isinstance(player_character, Healer):
                                    player_character.attack(monster)
                                print(f'{player_character.name} attack {monster.name}\n {player_character.name} has {player_character.mana} mana left')
                                if monster.health > 0:
                                    attacks=monster.attack
                                    player_character.health -= attacks
                                    print(f"{monster.name} attacks {player_character} for {attacks} damage")
                                    if player_character.health <= 0:
                                        print(f"{player_character.name} has fallen in battle!")
                                        break
                                    else:
                                        print(f"{monster.name} had attack {player_character.name} for {monster.attack}\n{player_character.name} now has {player_character.health} health left")
                            except ValueError:
                                print("Invalid choice. Please enter a number.")
                    elif action == "run":
                        print("You fled from the battle!")
                    else:
                        print("Invalid choice. Try again.")
                if monster.health <= 0:
                    print(f"You defeated the {monster.name}!")
                    gold_dropped = 0
                    updated_drops = []
                    for drop in monster.drops:
                        if "gold" in drop:
                            try:
                                gold_value = int(drop.split()[0])
                                gold_dropped += gold_value
                            except ValueError:
                                print()
                        else:
                            updated_drops.append(drop)
                        player_character.gold += gold_dropped
                    print(f"The {monster.name} dropped: {', '.join(updated_drops)} and {gold_dropped} gold!")
                    player_character.inventory.extend(updated_drops)
                    print(f"Your updated inventory: {player_character.inventory}")
                    print(f"Your total gold: {player_character.gold}")
                elif player_character.health <= 0:
                    print("You have been defeated!")
                    break

                while player_character.health > 0:
                    next_monster = generate_random_monster()
                    print(f"\nA wild {next_monster.name} appears!\n{next_monster.name} has {next_monster.health} health.\n you have {player_character.health} health")
                    action = input(f"Do you want to [attack] {next_monster.name} or [run]? ").lower()
                    if action == "attack":
                        while next_monster.health > 0:
                            try:
                                print(f'you have {player_character.mana} mana')
                                if isinstance(player_character, Archer):
                                    print("Choose your arrow type:\n1: Standard mana cost:0 damage:10\n2: Fire mana cost:7 damage:15\n3: Poison mana cost 5 damage:12")
                                    arrow_choice = int(input("Enter your choice: "))
                                    player_character.attack(next_monster, arrow_choice)
                                elif isinstance(player_character, Knight):
                                    print("Choose your attack type:\n1: Slash mana cost:0 damage:10 \n2: Charge Attack mana cost:10 damage:15\n3: Power Slash mana: 15 damage:30")
                                    attack_choice = int(input("Enter your choice: "))
                                    player_character.attack(next_monster, attack_choice)
                                elif isinstance(player_character, Mage):
                                    print("Choose your spell:\n1: Fireball mana cost 10 damage:10\n2: Frostbolt mana cost 10 damage:10")
                                    spell_choice = int(input("Enter your choice: "))
                                    player_character.attack(next_monster, spell_choice)
                                elif isinstance(player_character, Healer):
                                    player_character.attack(next_monster)
                                if next_monster.health > 0:
                                    attack2=next_monster.attack
                                    player_character.health -= attack2
                                    if player_character.health <= 0:
                                        print(f"{player_character.name} has fallen in battle!")
                                        break
                                    else:
                                        print(f"{next_monster.name} had attack {player_character.name} for {next_monster.attack}\n{player_character.name} now has {player_character.health} health left")
                            except ValueError:
                                print("Invalid choice. Please enter a number.")
                    elif action == "run":
                        print("You fled from the battle!")
                    else:
                        print("Invalid choice. Try again.")
                    if next_monster.health <= 0:
                        print(f"You defeated the {next_monster.name}!")
                        gold_dropped = 0
                        updated_drops = []
                        for drop in next_monster.drops:
                            if "gold" in drop:
                                try:
                                    gold_value = int(drop.split()[0])
                                    gold_dropped += gold_value
                                except ValueError:
                                    print()
                            else:
                                updated_drops.append(drop)
                            player_character.gold += gold_dropped
                        print(f"The {next_monster.name} dropped: {', '.join(updated_drops)} and {gold_dropped} gold!")
                        player_character.inventory.extend(updated_drops)
                        print(f"Your updated inventory: {player_character.inventory}")
                        print(f"Your total gold: {player_character.gold}")
                    elif player_character.health <= 0:
                        print("You have been defeated!")
                        break

            elapsed_time = time.time() - forest_start_time
            if elapsed_time > 15 and not cave_triggered:
                    cave_triggered = True
                    cave_choice = input("Do you want to go into the cave? [yes/no] ").lower()
                    if cave_choice == "yes":
                        enter_cave(player_character)
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
        except ValueError:
            print('CHOOSE A VALID CHOICE')
intro()
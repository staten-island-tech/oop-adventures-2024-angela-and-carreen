import random
class Monster:
    def __init__(self, name, health, attack_power, drops):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.drops = drops
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()
        else:
            print(f"\n{self.name} now has {self.health} health left")
    def die(self):
        print(f"{self.name} is now dead")
        self.drop_item()
    def drop_item(self):
        if self.drops:
            print(f"\n{self.name} drops:")
            num_drops = random.randint(1, len(self.drops))
            for _ in range(num_drops):
                dropped_item = random.choice(list(self.drops))
                print(f"- {dropped_item}")
        else:
            print("No drops available")
    def attack(self, player_character):
        print(f"{self.name} attacks {player_character.name} for {self.attack_power} damage!")
        player_character.health -= self.attack_power
        if player_character.health > 0:
            print(f"{player_character.name} now has {player_character.health} health left.")
        else:
            print(f"{player_character.name} has been defeated.")

werewolf = Monster("Werewolf", 100, 25, {"werewolf fur", "werewolf claws", "55 gold coins"})
goblin = Monster("Goblin", 50, 5, {"goblin skin", "wooden shield", "5 gold coins"})
skeleton = Monster("Skeleton", 30, 10, {"bones", "rusty sword", "3 gold coins"})
slime = Monster("Slime", 15, 1, {"1 gold coin"})
dragon = Monster("Dragon", 150, 80, {"dragon scales", "dragon tooth", "dragon heart", "100 gold coins"})
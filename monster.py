import random
class Monster:
    def __init__(self, name, health, attack, drops):
        self.name = name
        self.health = health
        self.attack = attack
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
        if self.health > 0:
            attacks=self.attack
            player_character.health -= attacks
class Next_monster(Monster):
    def __init__(self, name, health, attack, drops):
        super().__init__(name, health, attack, drops)
class Cave_monster(Monster):
    def __init__(self, name, health, attack, drops):
        super().__init__(name, health, attack, drops)

slime = Monster("Slime", 15, 1, {"2 gold"})

slime = Next_monster("Slime", 15, 1, {"2 gold"})
werewolf = Next_monster("Werewolf", 100, 15, {"werewolf fur", "werewolf claws", "55 gold"})
goblin = Next_monster("Goblin", 50, 8, {"goblin skin", "wooden shield", "5 gold"})
skeleton = Next_monster("Skeleton", 30, 5, {"bones", "rusty sword", "3 gold"})
orc = Next_monster("Orc", 80, 12, {"orc skin", "orc axe", "15 gold"})
troll = Next_monster("Troll", 120, 10, {"troll skin", "troll club", "30 gold"})

bat = Cave_monster("Bat", 10, 2, {"bat wing", "1 gold"})
slime = Cave_monster("Slime", 30, 1, {"2 gold"})
werewolf = Cave_monster("Werewolf", 100, 25, {"werewolf fur", "werewolf claws", "55 gold"})
goblin = Cave_monster("Goblin", 50, 15, {"goblin skin", "wooden shield", "5 gold"})
skeleton = Cave_monster("Skeleton", 30, 10, {"bones", "rusty sword", "3 gold"})
orc = Cave_monster("Orc", 80, 25, {"orc skin", "orc axe", "15 gold"})
troll = Cave_monster("Troll", 120, 20, {"troll skin", "troll club", "30 gold"})
spider = Cave_monster("Spider", 20, 5, {"spider silk", "spider venom", "2 gold"})
dragon = Cave_monster("Dragon", 300, 99, {"dragon scales", "dragon tooth", "dragon heart", "100 gold"})
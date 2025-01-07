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
    def interact(self, player):
        while self.health > 0 and player.health > 0:
            print(f"You are fighting a {self.name}!")
            action = input("Choose an action: [attack, run]: ").strip().lower()
            if action == "attack":
                player.attack(self)
                if self.health > 0:
                    print(f"{self.name} attacks you for {self.attack} damage!")
                    player.take_damage(self.attack)
            elif action == "run":
                print("You run away from the fight!")
                break
            else:
                print("Invalid action. Try again.")
        if player.health <= 0:
            print("You have been defeated...")

werewolf = Monster("Werewolf", 100, 25, {"werewolf fur", "werewolf claws", "55 gold coins"})
goblin = Monster("Goblin", 50, 5, {"goblin skin", "wooden shield", "5 gold coins"})
skeleton = Monster("Skeleton", 30, 10, {"bones", "rusty sword", "3 gold coins"})
slime = Monster("Slime", 15, 1, {"1 gold coin"})
dragon = Monster("Dragon", 150, 80, {"dragon scales", "dragon tooth", "dragon heart", "100 gold coins"})

werewolf.interact(MainCharacter)
goblin.interact(MainCharacter)
skeleton.interact(MainCharacter)
slime.interact(MainCharacter)
dragon.interact(MainCharacter)
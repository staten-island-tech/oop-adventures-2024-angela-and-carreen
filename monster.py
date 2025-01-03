import random

class Monster: 
    def __init__(self, name, hp, attack, drops):
        self.name=name
        self.hp=hp
        self.attack=attack
        self.drops=drops
    
    def attacking(self, target):
        if self.hp>0:
            print(f"{self.name} attacks {target.name} target take {self.attack} damage!")
            target.take_damage(self.attack)
        
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp<=0:
            self.die()
        else:
            print(f"{self.name} now has {self.hp} HP left")
    
    def die(self):
        if self.hp<=0:
            print(f"{self.name} is now dead")
            self.drop_item()
    
    def alive(self):
        return self.hp>0
        print (f"{self.name} takes {damage} damage, {self.hp} hp remaining")
    
    def drop_item(self):
        if self.drops:
            print (f"{self.name} drops these")
            num_drops = random.randint(1, len(self.drops))
            for _ in range(num_drops):
                dropped_item = random.choice(list(self.drops))
                print(f"- {dropped_item}")
        else:
            print("no drops availble")



werewolf = Monster("Werewolf", 100, 50, {"werewolf fur", "werewolf claws", "55 gold coins"})
goblin = Monster("Goblin", 50, 20, {"goblin skin", "wooden shield", "5 gold coins"})
skeleton = Monster("skeleton", 30, 10, {"bones", "rusty sword", "3 gold coins"})
dragon = Monster("Dragon", 150, 80, {"dragon scales", "dragon tooth", "dragon heart", '100 gold coins'})


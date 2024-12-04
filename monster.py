class Monster: 
    def __init__(self, name, hp, attack, defense, drops):
        self.name=name
        self.hp=hp
        self.attack=attack
        self.defense=defense
        self.drops=drops
    
    def attacking(self, target):
        print(f"{self.name} attacks {target.name} target take {self.attack} damage!")
        target.take_damage(self.attack)
        
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp<0:
            self.die()
        else:
            print(f"{self.name}now has {self.hp} HP left")
    
    def die(self):
        print(f"{self.name}is now dead")
    
    def alive(self):
        return self.hp>0
    
    def drop_item(self):
        if self.die():
            





skeleton = Monster("skeleton", 30, 10, 0, {"bones"})


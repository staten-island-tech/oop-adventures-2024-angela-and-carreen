class Items:
    def __init__(self, name, price, durability, effect):
        self.name=name
        self.price=price
        self.durability=durability
        self.effect=effect

    def activate_effect(self):
        if self.durability>=0:
            self.durability -=1
            return f"Durability is now {self.durability}"
        else:
            return f"{self.name} is now destroyed"
    
    def repair(self, amount):
        self.durability += amount
        return f"{self.name} has been fixed. durability has become {self.durability}"

    class Weapons:
        def __init__(self, name, rarity, price, durability, effect):
            self.name=name
            self.rarity=rarity
            self.price=price
            self.durability=durability
            self.effect=effect
        
        def activate_effect(self):
            if self.durability>=0:
                self.durability -=1
                return f"Durability is now {self.durability}"
            else:
                return f"{self.name} is now destroyed"
    
    def repair(self, amount):
        self.durability += amount
        return f"{self.name} has been fixed. durability has become {self.durability}"


lamp = Item("Lamp", 5, 100, "light")
map
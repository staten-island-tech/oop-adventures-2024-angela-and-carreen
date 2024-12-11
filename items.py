class Items:
    def __init__(self, name, price, durability, effect, effect_duration):
        self.name=name
        self.price=price
        self.durability=durability
        self.effect=effect
        self.effect_duration=effect_duration
        self.is_active=False

    def activate_effect(self):
        if self.durability>=0:
            self.durability -=1
            return f"Durability is now {self.durability}"
        else:
            return f"{self.name} is now destroyed"

    def apply_effect(self):
        if self.duration > 0:
            self.is_active=True
            print(f"The effect of {self.name} is active for {self.duration}")
        else:
            print(f"{self.name} ability is N/A")

    def update_duration(self):
        if self.is_active:
            self.duration -=1
            print(f"{self.name}'s effect is now over")
            if self.duration <= 0:
                self.expire_effect()  

    def expire_effect(self):
        self.is_active=False
        print(f"the effect of {self.name} is now over")

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

        def apply_effect(self):
            if self.duration > 0:
                self.is_active=True
                print(f"The effect of {self.name} is active for {self.duration}")
            else:
                print(f"{self.name} ability is N/A")

        def update_duration(self):
        if self.is_active:
            self.duration -=1
            print(f"{self.name}'s effect is now over")
            if self.duration <= 0:
                self.expire_effect()  

        def expire_effect(self):
            self.is_active=False
            print(f"the effect of {self.name} is now over")
    
        def repair(self, amount):
            self.durability += amount
            return f"{self.name} has been fixed. durability has become {self.durability}"


lamp = Items("Lamp", 5, 100, "light", 10)
Map = Items("Map", 3, 50, "N/A", "N/A")
Gold_coin = Items("Gold Coin", 1, 1, "N/A", "N/A")
healing_potion = Items("Healing Potion", 10, 1, "heal", 5)
exploding_potion = Items("Exploding Potion", 10, 1, "explosion", 5)
invisibility_potion = Items("Invisibility Potions", 10, 1, "invisibility", 5)
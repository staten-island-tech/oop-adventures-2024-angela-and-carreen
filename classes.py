class Character:
    def __init__(self, name, mana, defense, inventory):
        self.name = name
        self.mana = mana
        self.defense = defense
        self.health = 100
        self.currency = 25
        self.inventory = inventory

class Archer(Character):
    def __init__(self, name, mana, arrows, defense, inventory):
        super().__init__(name, mana, defense, inventory)
        self.arrows = arrows
        self.arrow_types = {
            1: {"name": "Standard", "damage": 10, "mana_cost": 0},
            2: {"name": "Fire", "damage": 15, "mana_cost": 7, "effect": "burn"},
            3: {"name": "Poison", "damage": 12, "mana_cost": 5, "effect": "poison"},}
    def attack(self, monster, arrow_choice):
        if arrow_choice not in self.arrow_types:
            print(f"{arrow_choice} is not a valid arrow choice")
            return
        arrow = self.arrow_types[arrow_choice]
        if self.arrows > 0:
            self.arrows -= 1
            print(f"{self.name} shoots a {arrow['name']} arrow at {monster.name}.")
            damage = arrow["damage"]
            monster.take_damage(damage)
            if "effect" in arrow:
                if arrow["effect"] == "burn":
                    print(f"{monster.name} is burned!")
                    monster.take_damage(5)
                elif arrow["effect"] == "poison":
                    print(f"{monster.name} is poisoned!")
                    monster.take_damage(5)
            if arrow["mana_cost"] > 0:
                if self.mana >= arrow["mana_cost"]:
                    self.mana -= arrow["mana_cost"]
                    print(f"{self.name} used {arrow['name']} arrow consuming {arrow['mana_cost']} mana.")
                else:
                    print(f"{self.name} doesn't have enough mana for {arrow['name']}!")
                    self.arrows += 1
        else:
            print(f"{self.name} is out of arrows!")
    def reload(self, number_of_arrows):
        self.arrows += number_of_arrows
        print(f"{self.name} reloads {number_of_arrows} arrows.")
    def __str__(self):
        return f"Archer {self.name}: Mana = {self.mana}, Arrows = {self.arrows}, Defense = {self.defense}, Inventory = {self.inventory}"
class Knight(Character):
    def __init__(self, name, mana, defense, inventory):
        super().__init__(name, mana, defense, inventory)
        self.attack_type = {
            1: {"name": "Slash", "damage": 10, "mana_cost": 0},
            2: {"name": "Charge Attack", "damage": 15, "mana_cost": 10},
            3: {"name": "Power Slash", "damage": 30, "mana_cost": 15},}
    def attack(self, monster, attack_choice):
        if attack_choice not in self.attack_type:
            print(f"{attack_choice} is not a valid attack choice.")
            return
        attack = self.attack_type[attack_choice]
        if self.health <= 0:
            print(f"{self.name} can't attack anymore!")
            return
        if attack["mana_cost"] > 0:
            if self.mana >= attack["mana_cost"]:
                self.mana -= attack["mana_cost"]
                print(f"{self.name} uses {attack['name']} consuming {attack['mana_cost']} mana.")
            else:
                print(f"{self.name} doesn't have enough mana for {attack['name']}!")
                return
        print(f"{self.name} attacks {monster.name} with {attack['name']}!")
        damage = attack["damage"]
        monster.take_damage(damage)
        monster.health -= damage
    def __str__(self):
        return f"Knight {self.name}: Mana = {self.mana}, Defense = {self.defense}, Inventory = {self.inventory}"
class Mage(Character):
    def __init__(self, name, mana, defense, inventory):
        super().__init__(name, mana, defense, inventory)
        self.attack_type = {
            1: {"name": "Fireball", "damage": 10, "mana_cost": 10, "effect": "burn"},
            2: {"name": "Frostbolt", "damage": 10, "mana_cost": 10, "effect": "frost"},
        }

    def attack(self, monster, attack_choice):
        if attack_choice not in self.attack_type:
            print(f"{attack_choice} is not a valid attack choice")
            return
        attack = self.attack_type[attack_choice]
        if self.health > 0:
            print(f"{self.name} attacks {monster.name} with {attack['name']}")
            damage = attack["damage"]
            monster.take_damage(damage)
            if "effect" in attack:
                if attack["effect"] == "burn":
                    print(f"{monster.name} is burned!")
                    monster.take_damage(5)
                elif attack["effect"] == "frost":
                    print(f"{monster.name} is frozen!")
                    monster.take_damage(5)
            if attack["mana_cost"] > 0:
                if self.mana >= attack["mana_cost"]:
                    self.mana -= attack["mana_cost"]
                    print(f"{self.name} used {attack['name']} consuming {attack['mana_cost']} mana.")
                else:
                    print(f"{self.name} doesn't have enough mana for {attack['name']}!")
        else:
            print(f"{self.name} can't attack anymore")
    def __str__(self):
        return f"Mage {self.name}: Mana = {self.mana}, Defense = {self.defense}, Inventory = {self.inventory}"
class Healer(Character):
    def __init__(self, name, mana, defense, inventory):
        super().__init__(name, mana, defense, inventory)
        self.healing_type = {
            1: {"name": "Standard", "heals_for": 10, "mana_cost": 10},
            2: {"name": "Better Healing", "heals_for": 20, "mana_cost": 20}}
    def attack(self, monster):
        dagger_damage = 5
        print(f"{self.name} stabs {monster.name} with a dagger for {dagger_damage} damage!")
        monster.take_damage(dagger_damage)
    def heal(self, target, healing_choice):
        if healing_choice not in self.healing_type:
            print(f"{healing_choice} is not a valid healing choice.")
            return
        healing = self.healing_type[healing_choice]
        if self.mana >= healing["mana_cost"]:
            self.mana -= healing["mana_cost"]
            target.health += healing["heals_for"]
            print(f"{self.name} used {healing['name']} to heal {target.name} for {healing['heals_for']} health, consuming {healing['mana_cost']} mana.")
        else:
            print(f"{self.name} doesn't have enough mana to use {healing['name']}!")
    def __str__(self):
        return f"Healer {self.name}: Mana = {self.mana}, Defense = {self.defense}, Inventory = {self.inventory}"
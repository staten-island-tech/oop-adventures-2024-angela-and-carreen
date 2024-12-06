class Archer:
    def __init__(self, name, health, mana, arrows, defense):
        self.name = name
        self.health = health
        self.defense = defense
        self.mana = mana
        self.arrows = arrows
        self.arrow_types = {
            1: {"name": "Standard", "damage": 10, "mana cost": 0},
            2: {"name": "Fire", "damage": 15, "mana cost": 7, "effect": "burn"},
            3: {"name": "Poison", "damage": 12, "mana cost": 5,"effect": "poison"},}

    def shoot_arrow(self, target, arrow_choice):
        if arrow_choice not in self.arrow_types:
            print(f"{arrow_choice} is not a valid arrow choice")
            return
        
        arrow = self.arrow_types[arrow_choice]
        
        if self.arrows > 0:
            self.arrows -= 1
            print(f"{self.name} shoots a {arrow['name']} arrow at {target.name}.")
            damage = arrow["damage"]
            target.take_damage(damage)
            if "effect" in arrow:
                if arrow["effect"] == "burn":
                    print(f"{target.name} is burned!")
                    target.take_damage(5)
                elif arrow["effect"] == "poison":
                    print(f"{target.name} is poisoned!")
                    target.take_damage(5)
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

    def take_damage(self, damage):
        reduced_damage = max(damage - self.defense, 0)
        self.health -= reduced_damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} takes {reduced_damage} damage, {self.health} health remaining.")

    def __str__(self):
        return f"Archer {self.name}: Health = {self.health}, Mana = {self.mana}, Arrows = {self.arrows}, Defense = {self.defense}"

class healer:
    def __init__(self, name, health, mana, healing, defense):
        self.name = name
        self.health = health
        self.defense = defense
        self.mana = mana
        self.healing = healing
        self.healing_type = {
            1: {"name": "Standard", "heals for": 10, "mana cost": 0},
            2: {"name": "Better healing", "heals for": 20, "mana cost": 10}}

    def healing(self, target, healing_choice):
        if healing_choice not in self.healing_type:
        print(f"{healing_choice} is not a valid arrow choice")
        return

        if self.healing:
            if arrow["mana_cost"] > 0:
                if self.mana >= arrow["mana_cost"]:
                    self.mana -= arrow["mana_cost"]
                    print(f"{self.name} used {healing['name']} arrow consuming {arrow['mana_cost']} mana.")
                else:
                    print(f"{self.name} doesn't have enough mana for {arrow['name']}!")

    def take_damage(self, damage):
        reduced_damage = max(damage - self.defense, 0)
        self.health -= reduced_damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} takes {reduced_damage} damage, {self.health} health remaining.")

    def __str__(self):
        return f"Healer {self.name}: Health = {self.health}, Mana = {self.mana}, Defense = {self.defense}"
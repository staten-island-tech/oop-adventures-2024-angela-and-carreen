class Healer:
    def __init__(self, name, health, mana, defense):
        self.name = name
        self.health = health
        self.defense = defense
        self.mana = mana
        self.healing_type = {
            1: {"name": "Standard", "heals_for": 10, "mana_cost": 10},
            2: {"name": "Better Healing", "heals_for": 20, "mana_cost": 20}}

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

    def take_damage(self, damage):
        reduced_damage = max(damage - self.defense, 0)
        self.health -= reduced_damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} takes {reduced_damage} damage, {self.health} health remaining.")

    def __str__(self):
        return f"Healer {self.name}: Health = {self.health}, Mana = {self.mana}, Defense = {self.defense}"
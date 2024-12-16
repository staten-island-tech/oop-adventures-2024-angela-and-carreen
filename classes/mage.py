class mage:
    def __init__(self, name, health, mana, defense, attacks):
        self.name = name
        self.health = health
        self.defense = defense
        self.mana = mana
        self.attacks = attacks
        self.attack_type = {
            1: {"name": "fireball", "damage": 10, "mana cost": 10, "effect": "burn"},
            2: {"name": "frostbolt", "damage": 10, "mana cost": 10, "effect": "forst"}}
    def attacking(self, target, attack_choice):
        if attack_choice not in self.attack_type:
            print(f"{attack_choice} is not a valid attack choice")
            return

        attack = self.attack_types[attack_choice]

        if self.attacks > 0:
            print(f"{self.name} attacks {target.name} with {attack['name']}")
            damage = attack["damage"]
            target.take_damage(damage)
            if "effect" in attack:
                if attack["effect"] == "burn":
                    print(f"{target.name} is burned!")
                    target.take_damage(5)
                elif attack["effect"] == "frost":
                    print(f"{target.name} is forzen!")
                    target.take_damage(5)
                if attack["mana_cost"] > 0:
                    if self.mana >= attack["mana_cost"]:
                        self.mana -= attack["mana_cost"]
                        print(f"{self.name} used {attack['name']} consuming {attack['mana_cost']} mana.")
                    else:
                        print(f"{self.name} doesn't have enough mana for {attack['name']}!")
        else:
            print(f"{self.name} can't attack any more")

    def take_damage(self, damage):
        reduced_damage = max(damage - self.defense, 0)
        self.health -= reduced_damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} takes {reduced_damage} damage, {self.health} health remaining.")

    def __str__(self):
        return f"mage {self.name}: Health = {self.health}, Mana = {self.mana}, Defense = {self.defense}, Attacks = {self.attacks}"
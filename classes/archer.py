class Archer:
    def __init__(self, name, health, arrows):
        self.name = name
        self.health = health
        self.arrows = arrows
        self.arrow_types = {
            1: {"name": "Standard", "damage": 10},
            2: {"name": "Fire", "damage": 15,"effect": "burn"},
            3: {"name": "Poison", "damage": 12, "effect": "poison"},}

    def shoot_arrow(self, target, arrow_choice):
        """Shoots a selected type of arrow at a target based on user choice."""
        if arrow_choice not in self.arrow_types:
            print(f"{arrow_choice} is not a valid arrow choice!")
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
        else:
            print(f"{self.name} is out of arrows!")

    def reload(self, number_of_arrows):
        """Reload the bow with arrows."""
        self.arrows += number_of_arrows
        print(f"{self.name} reloads {number_of_arrows} arrows.")

    def take_damage(self, damage):
        """Method to take damage when attacked."""
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} takes {damage} damage, {self.health} health remaining.")

    def __str__(self):
        return f"Archer {self.name}: Health = {self.health}, Arrows = {self.arrows}"

class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage, {self.health} health remaining.")

    def __str__(self):
        return f"{self.name}: Health = {self.health}"

# Example usage:
archer = Archer("Elandra", 100, 10)
enemy = Enemy("Goblin", 60)
while enemy.health > 0 and archer.health > 0:
    print("\nChoose an arrow type:")
    print("1. Standard Arrow - 10 damage")
    print("2. Fire Arrow - 15 damage")
    print("3. Poison Arrow - 12 damage")

    try:
        arrow_choice = int(input("\nEnter the number of your choice (1-3) or 0 to quit: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if arrow_choice == 0:
        print("Exiting the game.")
        break

    archer.shoot_arrow(enemy, arrow_choice)

    print("\nEnemy Status:")
    print(enemy)
    print("\nArcher Status:")
    print(archer)

if archer.health <= 0:
    print(f"{archer.name} has been defeated!")
elif enemy.health <= 0:
    print(f"\n{enemy.name} has been defeated!")


class NPC:
    def __init__(self, name, description, currency=0):
        self.name = name
        self.description = description
        self.currency = currency
        self.inventory = []
    def interact(self):
        print(f"{self.name}: Hello, traveler! How can I help you today?")
    def talk(self):
        print(f"{self.name}: {self.description}")


class StoreClerk(NPC):
    def __init__(self, name, description, currency, inventory):
        super().__init__(name, description, currency)
        self.inventory = inventory
    def show_inventory(self):
        print(f"\n{self.name}:Welcome to my shop! Here are the items available for sale:")
        for idx, (item, price) in enumerate(self.inventory, 1):
            print(f"{idx}.{item}- {price} gold")
    def buy_item(self, player, item_index):
        if 0 < item_index <= len(self.inventory):
            item, price = self.inventory[item_index - 1]
            if player.currency >= price:
                player.currency -= price
                self.currency += price
                self.inventory.remove(self.inventory[item_index - 1])
                print(f"{self.name}: Thank you for purchasing {item}! You have {player.currency} gold left.")
            else:
                print(f"{self.name}:Sorry, you don't have enough gold for {item}.")
        else:
            print("Invalid selection.")
    def interact(self, player):
        while True:
            self.show_inventory()
            try:
                choice = int(input(f"\nEnter the number of the item you want to buy (0 to leave): "))
                if choice == 0:
                    print(f"\n{self.name}: Goodbye! Come again soon!")
                    break
                else:
                    self.buy_item(player, choice)
            except ValueError:
                print("Please enter a valid number.")

class Player:
    def __init__(self, name, currency):
        self.name = name
        self.currency = currency

player = Player("Arthur", 200)
store_clerk = StoreClerk("Mia", "I sell weapons and potions.", 0, [("Sword", 100), ("Potion", 50), ("Shield", 150)])
store_clerk.interact(player)

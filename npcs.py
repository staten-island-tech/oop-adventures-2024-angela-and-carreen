import items
class NPC:
    def __init__(self, name, currency=50):
        self.name = name
        self.currency = currency
        self.inventory = []
    def interact(self):
        print(f"{self.name}: Hello, traveler! How can I help you today?")

class StoreClerk(NPC):
    def __init__(self, name, currency, inventory):
        super().__init__(name, currency)
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
                print(f"{self.name}:Sorry, you too broke for {item}.")
        else:
            print("Invalid selection.")
    def interact(self, player):
        while True:
            self.show_inventory()
            try:
                choice = int(input(f"\nEnter the number of the item you want to buy (0 to leave): "))
                if choice == 0:
                    print(f"\n{self.name}: bye!")
                    break
                else:
                    self.buy_item(player, choice)
            except ValueError:
                print("Please enter a valid number.")

class Trader(NPC):
    def __init__(self, name, currency, inventory):
        super().__init__(name, currency)
        self.inventory = inventory
    def show_inventory(self):
        print(f"\n{self.name}: Here are the items I can trade:")
        for idx, (item, price) in enumerate(self.inventory, 1):
            print(f"{idx}. {item} - {price} gold")
    def trade_item(self, player, item_index):
        if 0 < item_index <= len(self.inventory):
            item, price = self.inventory[item_index - 1]
            if player.currency >= price:
                player.currency -= price
                self.currency += price
                self.inventory.remove(self.inventory[item_index - 1])
                print(f"{self.name}: You've traded for {item}. You now have {player.currency} gold.")
            else:
                print(f"{self.name}: Sorry, you don't have enough gold for {item}.")
        else:
            print("\nInvalid selection.")
    def interact(self, player):
        while True:
            self.show_inventory()
            try:
                choice = int(input(f"\nEnter the number of the item you want to trade (0 to leave): "))
                if choice == 0:
                    print(f"\n{self.name}: Farewell, traveler!")
                    break
                else:
                    self.trade_item(player, choice)
            except ValueError:
                print("\nPlease enter a valid number.")

class Innkeeper(NPC):
    def __init__(self, name, currency, room_cost):
        super().__init__(name, currency)
        self.room_cost = room_cost
    def offer_room(self, player):
        print(f"\n{self.name}: I have rooms available for {self.room_cost} gold.")
        if player.currency >= self.room_cost:
            player.currency -= self.room_cost
            print(f"\n{self.name}: Here's your room. You now have {player.currency} gold left.")
        else:
            print(f"\n{self.name}: Sorry, you don't have enough gold for a room.")
    def interact(self, player):
        print(f"\n{self.name}: Welcome to my inn!")
        while True:
            choice = input(f"Would you like to rent a room for {self.room_cost} gold? (yes/no): ").lower()
            if choice == "yes":
                self.offer_room(player)
                break
            elif choice == "no":
                print(f"\n{self.name}: Safe travels!")
                break
            else:
                print("Please respond with 'yes' or 'no'.")

""" class Player:
    def __init__(self, name, currency):
        self.name = name
        self.currency = currency
player = Player("Arthur", 50) """
store_clerk = StoreClerk("Mia", 50, [('lamp', 5), ('Map', 3), ('sword', 15), ('shield', 10), ('bow', 15), ('arrows', 1)])

trader= Trader("John", 50, [('lamp', 5), ('Map', 3), ('healing_potion', 10), ('exploding_potion', 10), ('invisibility_potion', 10), ('invincibility_potion', 10), ('laxitive', 15)])
innkeeper = Innkeeper("Alya", 0, 15)


class main_charater:
    def __init__ (self, name, health, currency):
        self.name = name
        self.health = health
        self.currency = currency
        self.inventory = []
    if __name__ == "__main__":
        user_name = input("Enter your character's name: ")





with open("./saves.json", "r") as f:
    data = json.load(f)
    data.append(user_name.__dict__)
new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data)
    f.write(json_string)
os.remove("saves.json")
os.rename(new_file, "saves.json")
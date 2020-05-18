class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Gold(Item):
    def __init__(self, value):
        super().__init__(name="GOLD", description="a round coin with " + str(value) + " stamped on it")

class Weapon(Item):
    def __init__(self, name, description, damage):
        self.damage = damage
        super().__init__(name, description)

class Armor(Item):
    def __init__(self, name, description, soak):
        self.soak = soak
        super().__init__(name, description)

class Sword(Weapon):
    def __init__(self):
        super().__init__(name="SWORD",
                         description="a basic sword",
                         damage=10)

class Rock(Weapon):
    def __init__(self):
        super().__init__(name="ROCK",
                         description="a small rock",
                         damage=5)

class BronzePlate(Armor):
    def __init__(self):
        super().__init__(name="BRONZE PLATE",
                         description="a breast plate made of solid bronze",
                         soak=5)

class SteelPlate(Armor):
    def __init__(self):
        super().__init__(name="BRONZE PLATE",
                         description="a breast plate made of solid steel",
                         soak=10)
    

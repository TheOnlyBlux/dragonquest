class Monster:
    soak = 1
    def __init__(self, name, hp, strength, speed):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.speed = speed

    def is_alive(self):
        return self.hp > 0

class Goblin(Monster):
    def __init__(self):
        super().__init__(name="GOBLIN",
                         hp=20,
                         strength=5,
                         speed=6)
                         
class Troll(Monster):
    def __init__(self):
        super().__init__(name="TROLL",
                         hp=50,
                         strength=10,
                         speed=3)

class Dragon(Monster):
    def __init__(self):
        super().__init__(name="DRAGON",
                         hp=75,
                         strength=15,
                         speed=12)

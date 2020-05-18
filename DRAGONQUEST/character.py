class Character:
    def __init__(self, name, hp, strength, speed, soak):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.speed = speed
        self.soak = soak

    def is_alive(self):
        return self.hp > 0

class Warrior(Character):
    def __init__(self):
        super().__init__(name=input("what's your name?"), hp=50, strength=5, speed=10, soak=3)

class Rogue(Character):
    def __init__(self):
        super().__init__(name=input("what's your name?"), hp=40, strength=3, speed=20, soak=2)

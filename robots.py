from weapons import Weapons

class Robots: 
    def __init__(self, name, weapons):
        self.name = name 
        self.hp = 100
        self.weapons = Weapons('Laser beam', 35)
        self.attk_pwr = weapons

    def attack(self, dino):
        dino.hp -= self.weapons.attk_pwr

        
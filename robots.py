from weapons import weapons

class robots: 
    def __init__(self, name, weapons):
        self.name = name 
        self.health = 100
        self.weapons = weapons('Laser beam', 35, 0)
        self.attk_pwr = weapons

    def attack(self, dino):
        dino.health -= self.weapons.attk_pwr

        
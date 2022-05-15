class Dino: 
   
   
    def __init__(self, name, attk_pwr):
        self.name = name 
        self.hp = 100
        self.attk_pwr = attk_pwr

    def attack(self, robots):
        robots.hp -= self.attk_pwr

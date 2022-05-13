class dino: 
   
   
    def __init__(self, name, attk_pwr):
        self.name = name 
        self.health = 100
        self.attk_pwr = attk_pwr

    def attack(self, robots):
        robots.health -= self.attk_pwr

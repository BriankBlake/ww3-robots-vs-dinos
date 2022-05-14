from dino import Dino

class Herd:
    def __init__(self):
        self.dino = []
        self.create_herd()
        
    def create_herd(self):
            dino_1 = Dino('Rex', 100)
            dino_2 = Dino('Dino', 50)
            dino_3 = Dino('Godzilla', 100)

            self.dino.append(dino_1)
            self.dino.append(dino_2)
            self.dino.append(dino_3)

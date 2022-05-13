from dino import dino

class herd:
    def __init__(self):
        self.dino = []
        self.create_herd()
        
    def create_herd(self):
            dino_1 = dino('Rex', 100)
            dino_2 = dino('Dino', 50)
            dino_3 = dino('Godzilla', 100)

            self.dino.append(dino_1)
            self.dino.append(dino_2)
            self.dino.append(dino_3)

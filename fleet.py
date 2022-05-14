from robots import Robots


class Fleet:

    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        robots_1 = Robots('Optimus prime', 100)
        robots_2 = Robots('Megatron', 100)
        robots_3 = Robots('Starscream', 50)

        self.robots.append(robots_1)
        self.robots.append(robots_2)
        self.robots.append(robots_3)
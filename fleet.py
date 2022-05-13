from robots import robots


class Fleet:

    def __init__(self):
        self.robots = []
        # self.create_fleet()

    def create_fleet(self):
        robots_1 = robots('Optimus prime', 100)
        robots_2 = robots('Megatron', 100)
        robots_3 = robots('Starscream', 50)

        self.robots.append(robots_1)
        self.robots.append(robots_2)
        self.robots.append(robots_3)
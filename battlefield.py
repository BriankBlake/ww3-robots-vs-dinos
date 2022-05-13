from fleet import Fleet
from herd import herd

fleet = Fleet()
herd = herd()



class Battlefield:
    def __init__(self):
        self.fleet = fleet
        self.herd = herd
    def run_game(self):
        self.display_welcome()

    def display_welcome(self):
        print("Welcome to ww3 where robots and dinos fight to the death! Players are you ready? Let's get it on!")
        self.battle()

    def battle(self):
        round_number = 1
        print(f"Round {round_number} go! Dino's goes first.")
        self.dino_turn(self.herd.dino[0])
        print("Dino's turn end, robots go. ")
        self.robots_turn(self.fleet.robots[0])
        round_number += 1

    def dinos_turn(self, attking_dinos):
        print(f"{attking_dinos} dino turn go")
        # self.herd.dinos.attack(self.fleet.robots[0])
        self.show_dinos_opponent_options()


    def robots_turn(self, robots):
        print(f"{robots} robots go now")
        self.show_robots_opponent_options()


    def show_dino_opponent_options(self):
        print("Robots pick a Gladiator")

    def show_robot_opponent_options(self):
        print("Dinos pick a Gladiator")

    # def display_winners(self):
    #     if herd.health == 0:
    #         print("Robots defeated the dinos so the winner is Robots!")
    #     if  fleet.health == 0:
    #         print("Dinos defeatd the robots so the winner is Dinos!")
    #     else:
    #         Battlefield()  







# self.dino_turn(self.herd.dinosaurs[0])
# self.fleet.robot_list[0].attack(self.herd.dino_list[0])

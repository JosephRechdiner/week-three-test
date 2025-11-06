from .monster import Monster
import random

class Goblin(Monster):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 20
        self.speed = random.randint(5, 10)
        self.power = random.randint(5, 10)
        self.armor_rating = 1


    def speak(self):
        print(f"GOBLIN {self.name} IS ANGRY!!!")

    def attack(self, damage, deafender):
        deafender.hp -= damage * self.weapon_multy_value


    def run_away(self):
        pass


from .monster import Monster
from .player import Player
import random

class Orc(Monster):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 50
        self.speed = random.randint(0, 5)
        self.power = random.randint(10, 15)
        self.armor_rating = random.randint(2, 8)

    def speak(self):
        print(f"ORC {self.name} IS ANGRY!!!")

    def attack(self, damage, deafender: Player):
        deafender.hp -= damage *self.weapon_multy_value

import random


class Monster:
    monster_types = ["Orc", "Goblin"]
    weapon_values = {"Knife": 0.5, "Sword": 1, "Ax": 1.5} 

    def __init__(self, name: str):
        self.name = name
        self.weapon = random.choice(["Knife", "Sword", "Ax"])
        self.monster_type = random.choice(Monster.monster_types)
        self.weapon_multy_value = Monster.weapon_values[self.weapon]


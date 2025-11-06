import random


class Player:
    Player_types = ["Healer", "Fighter"]

    def __init__(self, name: str):
        self.name = name
        self.hp = random.randint(5, 10)
        self.speed = random.randint(5, 10)
        self.power = random.randint(5, 10)
        self.armor_rating = random.randint(5, 15)
        self.profession = random.choice(Player.Player_types)

    def selecting_player_type(self):
        if self.profession == "Fighter":
            player = Fighter(self.name)
            return player
        else:
            player = Healer(self.name)
            return player


class Fighter(Player):
    def __init__(self, name):
        super().__init__(name)
        self.power += 2
    
    def speak(self):
        print(f"HELLO {self.name}! YOU ARE A FIGHTER! 🥷| Power + 2")

    def attack(self, damage, deafender):
        deafender.hp -= damage



class Healer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.hp += 10

    def speak(self):
        print(f"HELLO {self.name}! YOU ARE A HEALER! 😇 | HP + 10")

    def attack(self, damage, deafender):
        deafender.hp -= damage



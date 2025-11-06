from core.goblin import Goblin
from core.orc import Orc
from core.player import Player
import random
import time


class Game:
    def __init__(self):
        pass

    def start(self):
        return self.show_menu()

    def show_menu(self):
        user_input = input("DO YOU WANT TO FIGHT(F) OR EXIT(E)? ")
        return user_input
    
    def create_player(self):
        user_name = input("ENTER YOUR NAME PLEASE: ")
        return Player(user_name)
    
    def choose_random_monster(self):
        optional_monster_name = ["GARGAMEL", "EVIL", "MADDNESS"]
        monster_name = random.choice(optional_monster_name)

        optional_monster_type = ["Orc", "Goblin"]
        monster_type = random.choice(optional_monster_type)

        if monster_type == "Orc":
            return Orc(monster_name)
        return Goblin(monster_name)
    
    def roll_dice(self, sides):
        roll_result = random.randint(1, sides)
        return roll_result
    
    def starting_attacker(self, player: Player, monster: Goblin | Orc):
        player_roll = self.roll_dice(6)
        monster_roll = self.roll_dice(6)
        return player if player_roll + player.speed >= monster_roll + monster.speed else monster
        
    
    def battle(self, player: Player, monster: Goblin | Orc):
        attacker = self.starting_attacker(player, monster)
        deafender = player if attacker is not player else monster
        
        while True:
            print("==============================")
            print(f"ATTACKER IS: {attacker.name}\nDEAFNDER IS {deafender.name}")
            print()
            print(f"ATTAKER HP: {attacker.hp}\nDEAFENDER HP: {deafender.hp}")
            print("ROLLING DICE...")
            time.sleep(1)
            dice_rolling = self.roll_dice(20)
            dice_rolling_and_speed = dice_rolling + attacker.speed

            if dice_rolling_and_speed < deafender.armor_rating:
                print("YOU MISSED! ")
                attacker, deafender = deafender, attacker
                continue
            else:
                print("GOOD SHOT! ") 
                cur_damage = self.roll_dice(6) + attacker.power

                if attacker is monster:
                    monster.attack(cur_damage, deafender)
                else:
                    player.attack(cur_damage, deafender)
        

            if deafender.hp <= 0:
                if deafender is player:
                    print(f"==============================\nBOOO YOU LOST!")
                else:
                    print(f"==============================\nWWW YOU WON!")
                return 

            attacker, deafender = deafender, attacker






from game import *
import time

if __name__ == "__main__":
    new_game = Game()
    print("\nWELCOM TO THE SHOOTING GAME!\n")
    
    while True:
        user_choice = new_game.start()
        if user_choice != "f" or user_choice != "f":
            print("==============================")
            print("YOU CHOSE TO LEAVE THE GAME!\n")
            print("==============================")
            break

        player = new_game.create_player().selecting_player_type()
        monster = new_game.choose_random_monster()
        print()
        player.speak()

        print("SELECTING ENEMY...\n")
        time.sleep(2)
        monster.speak()

        new_game.battle(player, monster)

    


import game_manager
import player
import inventory
import steps

blank_player = player.Player("Empty", 0, [])

game = game_manager.Game_manager([blank_player, blank_player, blank_player], None)

def start_game():

    x = input("\n play as "+game.current_player.name+"? \n 1-yes \n 2-no \n")
    if x == "1":
        print("starting")
    if x == "2":
        print("return to main menu")
        main_menu()

def select_game_file(slots):
    
    print("\nselect a save slot")
    for i in range(len(slots)):
        num = i+1
        print(str(num) + "-" + slots[i].name)
    x = input()

    if 0 < int(x) < 4:

        index = int(x)-1
        if game.save_slots[index].name == "Empty":
            name = input("\nEnter a name\n")
            new_player = player.Player(name, 1, [])
            game.set_save_data(index, new_player)

        game.set_current_player(index)
        start_game()
        

def main_menu():
    print("Enter a number to select")
    print("1-Play game")
    print("2-Clear save data")
    print("3-Exit")
    x = input()
    if x == "1":
        select_game_file(game.save_slots)

    if x == "2":
        print("Clearing data")

    if x == "3":
        print("exiting program")

main_menu()
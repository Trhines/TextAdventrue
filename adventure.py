import game_manager
import player
import inventory
import item
import ui_handler
import ui_element

main_menu = ui_element.UI_element(
    ["\nEnter a number to select","1-Play game", "2-Clear save data", "3-Exit"],
    True,
    3
)

select_save_slot_menu = ui_element.UI_element(
    "\nselect a save slot",
    False
)

save_slots = ui_element.UI_element(
    "placeholder",
    True
)

create_player = ui_element.UI_element(
    "\nEnter a name\n",
    True
)

confirm_slot = ui_element.UI_element(
    "this is a placeholder and should be set inside game manager",
    True,
    2
)

clear_data = ui_element.UI_element(
    ["\nClear all saved Data?", "1-yes", "2-no"],
    True,
    2
)


ui_elements= {
    "main_menu" : main_menu,
    "select_save_slot_menu": select_save_slot_menu,
    "save_slots": save_slots,
    "create_player": create_player,
    "confirm_slot": confirm_slot,
    "clear_data": clear_data
}

blank_player = player.Player("Empty")
default_save_data = [blank_player, blank_player, blank_player]

mirror = item.Mirror("Mirror")
saw = item.Saw("a saw")
halves = item.Table_halves("two table halves")
hole = item.Hole("a hole")

ui = ui_handler.UI_handler()
game = game_manager.Game_manager(ui, ui_elements, default_save_data)

game.main_menu()

# def step_one():
#     answer = input("You are in a room with no windows and doors. The only thing in the room is a table with a mirror on it. Your goal is to escape.\nWhat do you do?\n")
#     if answer == "look into the mirror":
#         mirror.use_item()
#         game.current_player.inventory.add_item(saw)
#         return True
    
# def step_two():
#     answer = input("this is step two")
#     print(answer)
#     print(game.save_slots[0].inventory.view_inventory())

# steps = [step_one, step_two]
        
# def init_step():
#     step_completed = steps[game.current_player.get_state()-1]()
#     if step_completed:
#         game.current_player.next_step()
#         print(game.current_player.get_state())
#         init_step()
    

# def clear_save_data():
#     x = input("\nClear all saved Data? \n 1-yes \n 2-no \n")
#     if x == "1":
#         game.save_slots = default_save_data
#         print("data cleard\n")
#         main_menu()
#     if x == "2":
#         print("return to main menu\n")
#         main_menu()


# def start_game():

#     x = input("\n play as "+game.current_player.name+"? \n 1-yes \n 2-no \n")
#     if x == "1":
#         print("starting \n \n")
#         init_step()
#     if x == "2":
#         print("return to main menu")
#         main_menu()

# def select_game_file(slots):
#     print("\nselect a save slot")
#     for i in range(len(slots)):
#         num = i+1
#         print(str(num) + "-" + slots[i].name)
#     x = input()

#     if 0 < int(x) < 4:

#         index = int(x)-1
#         if game.save_slots[index].name == "Empty":
#             name = input("\nEnter a name\n")
#             new_inventory = inventory.Inventory([])
#             new_player = player.Player(name, 1, new_inventory)
#             game.set_save_data(index, new_player)

#         game.set_current_player(index)
#         start_game()
        

# def main_menu():
#     print("Enter a number to select")
#     print("1-Play game")
#     print("2-Clear save data")
#     print("3-Exit")
#     x = input()
#     if x == "1":
#         select_game_file(game.save_slots)

#     if x == "2":
#         clear_save_data()

#     if x == "3":
#         print("exiting program")

#main_menu()
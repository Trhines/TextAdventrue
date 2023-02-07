import inventory
import player

class Game_manager:
    def __init__(self, ui_handler, ui_elements, save_data, current_player=None):
        self.ui = ui_handler
        self.ui_elements = ui_elements
        self.save_slots = save_data
        self.current_player = current_player
    
    def set_current_player(self, slot_num):
        self.current_player = self.save_slots[slot_num]

    def set_save_data(self, index, new_player):
        self.save_slots[index] = new_player

    def game_commands(self, input):
        print("entered commands")
        if input == "main menu":
            self.main_menu()
        return

    def start_game(self):
        print("add look around the room")
        # on initial start, present player with enviroment and inventory
        # then start action loop

    def confirm_player(self):
        res = self.ui.render(self.ui_elements["confirm_slot"], self.game_commands)
        if res == 1:
            self.start_game()
        else:
            self.main_menu()

    def create_player(self, index):
        res = self.ui.render(self.ui_elements["create_player"], self.game_commands)
        name = res
        new_inventory = inventory.Inventory()
        new_player = player.Player(name, new_inventory)
        self.set_save_data(index, new_player)
        self.confirm_player()
#             name = input("\nEnter a name\n")
#             new_inventory = inventory.Inventory([])
#             new_player = player.Player(name, 1, new_inventory)
#             game.set_save_data(index, new_player)
#         game.set_current_player(index)
#         start_game()


    def select_save_slot(self):
        slots = self.ui_elements.get("save_slots")
        def slot_names(slots):
            return slots.name
        raw_names = map(slot_names, self.save_slots)
        user_names = list(raw_names)
        slots.set_prompt(user_names)
        slots.set_validator(len(user_names))

        self.ui.render(self.ui_elements["select_save_slot_menu"], self.game_commands)
        res = self.ui.render(slots, self.game_commands)
        index = int(res)-1
        if self.save_slots[index].name == "Empty":
            self.create_player(index)
        else:
            self.confirm_player()

    def main_menu(self):
        res = self.ui.render(self.ui_elements["main_menu"], self.game_commands)
        if res == "1":
            self.select_save_slot()

        if res == "2":
            print("clear save data")

        if res == "3":
            print("exiting program")
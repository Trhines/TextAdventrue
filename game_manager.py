import player
import collection

class Game_manager:
    def __init__(self, ui_handler, ui_elements, save_data, default_environment, player_elements, current_player=None):
        self.ui = ui_handler
        self.ui_elements = ui_elements
        self.save_slots = save_data
        self.current_player = current_player
        self.default_environment = default_environment
        self.player_elements = player_elements
    
    def set_current_player(self, slot_num):
        self.current_player = self.save_slots[slot_num]
    
    def get_current_player(self):
        return self.current_player

    def set_save_data(self, index, new_player):
        self.save_slots[index] = new_player

    def retrieve_save_data(self, index):
        return self.save_slots[index]

    def menu_commands(self, input):
        if input == "current":
            print(self.current_player.name)
        if input == "main menu":
            self.main_menu()
        return
    
    def action_loop(self, player):
        while True:
            action = self.ui.render(self.ui_elements["action_loop"])
            escaped = player.take_action(action)
            if escaped is None:
                self.ui.render(self.ui_elements["nothing_happens"])
            if escaped:
                break
        self.ui.render(self.ui_elements["end"])
        self.main_menu()

    def start_game(self):
        player = self.get_current_player()
        player.take_action("look around")
        player.take_action("i")
        self.action_loop(player)

    def confirm_player(self, index):
        name = self.retrieve_save_data(index).name
        self.ui_elements["confirm_slot"].set_prompt("Play as "+ name + "?")
        res = self.ui.render(self.ui_elements["confirm_slot"], self.menu_commands)
        if res == "y":
            self.set_current_player(index)
            self.start_game()
        if res == "n":
            self.main_menu()

    def create_player(self, index):
        res = self.ui.render(self.ui_elements["create_player"], self.menu_commands)
        name = res
        new_inventory = collection.Collection()
        new_environment = collection.Collection(self.default_environment)
        new_player = player.Player(name, new_inventory, new_environment, self.ui, self.player_elements)
        self.set_save_data(index, new_player)
        self.confirm_player(index)
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

        self.ui.render(self.ui_elements["select_save_slot_menu"], self.menu_commands)
        res = self.ui.render(slots, self.menu_commands)
        index = int(res)-1
        if self.save_slots[index].name == "Empty":
            self.create_player(index)
        else:
            self.confirm_player(index)

    def main_menu(self):
        res = self.ui.render(self.ui_elements["main_menu"], self.menu_commands)
        if res == "1":
            self.select_save_slot()

        if res == "2":
            print("clear save data")

        if res == "3":
            print("exiting program")
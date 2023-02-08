import player
import ui_element

class Game_manager:
    def __init__(self, ui_handler, current_player=None):

        self.blank = player.Player("Empty")

        self.main_menu_ui_title = ui_element.UI_element(
            "\nEnter a number to select",
            False,
            None,
            "main_menu_title"
        )

        self.main_menu_ui_options = ui_element.UI_element(
            ["Play game", "Clear save data", "Exit"],
            True,
            3,
            "main_menu_options"
        )

        self.select_save_slot_menu = ui_element.UI_element(
            "\nselect a save slot",
            False,
            None,
            "select_save_slot_menu"
        )

        self.save_slots_ui = ui_element.UI_element(
            "placeholder",
            True,
            None,
            "save_slots"
        )

        self.create_player_ui = ui_element.UI_element(
            "\nEnter a name\n",
            True,
            None,
            "create_player"
        )

        self.confirm_slot = ui_element.UI_element(
            "this is a placeholder and should be set inside game manager",
            True,
            "y/n",
            "confirm_slot"
        )

        self.clear_data = ui_element.UI_element(
            "\nClear all saved Data?",
            True,
            "y/n",
            "clear_data"
        )

        self.game_intro = ui_element.UI_element(
            [
             "\nYou are in a house with no windows and doors.",
             "All you see is a table with a mirror on it.",
             "Your goal is to escape",
             "What do you do?"
             ]
        )

        self.action_loop_ui = ui_element.UI_element(
            "",
            True,
            None,
            "action_loop"
        )

        self.nothing_happens = ui_element.UI_element(
            "Nothing happens",
            False,
            None,
            "nothing_happens"
        )

        self.end = ui_element.UI_element(
            "Returning to main menu",
            False,
            None,
            "end"
        )

        self.ui = ui_handler
        self.save_slots = [self.blank, self.blank, self.blank]
        self.current_player = current_player

    def no_current_player(self):
        self.current_player = None
    
    def set_current_player(self, slot_num):
        self.current_player = self.save_slots[slot_num]
    
    def get_current_player(self):
        return self.current_player

    def set_save_data(self, index, new_player):
        self.save_slots[index] = new_player

    def retrieve_save_data(self, index):
        return self.save_slots[index]

    def menu_commands(self, input):
        match input:
            case "default":
                print(self.default_environment)

            case "slots":
                for slot in self.save_slots:
                    print(slot.name)

            case "environment":
                for slot in self.save_slots:
                    print(slot.environment.name)
                    print(slot.environment.items)

            case "inventories":
                for slot in self.save_slots:
                    print(slot.inventory.name)
                    print(slot.inventory.items)

            case "current":
                print(self.current_player.name)

            case"main menu":
                self.main_menu()
        return
    
    def action_loop(self, player):
        while True:
            action = self.ui.render(self.action_loop_ui)
            escaped = player.take_action(action)
            if escaped is None:
                self.ui.render(self.nothing_happens)
            if escaped:
                break
        self.ui.render(self.end)
        self.main_menu()

    def start_game(self):
        player = self.get_current_player()
        if player.new_game:
            self.ui.render(self.game_intro)
        else:
            player.take_action("look around")
            player.take_action("i")
        self.action_loop(player)

    def confirm_player(self, index):
        name = self.retrieve_save_data(index).name
        self.confirm_slot.set_prompt("Play as "+ name + "?")
        res = self.ui.render(self.confirm_slot, self.menu_commands)
        if res == "y":
            self.set_current_player(index)
            self.start_game()
        if res == "n":
            self.main_menu()

    def create_player(self, index):
        res = self.ui.render(self.create_player_ui, self.menu_commands)
        name = res
        new_player = player.Player(name, self.ui)
        self.set_save_data(index, new_player)
        self.confirm_player(index)


    def select_save_slot(self):
        slots = self.save_slots_ui
        user_names = [slot.name for slot in self.save_slots]
        slots.set_prompt(user_names)
        slots.set_validator(len(user_names))
        self.ui.render(self.select_save_slot_menu, self.menu_commands)
        res = self.ui.render(slots, self.menu_commands)
        index = int(res)-1
        if self.save_slots[index].name == "Empty":
            self.create_player(index)
        else:
            self.confirm_player(index)
    
    def clear_save_data(self):
        res = self.ui.render(self.clear_data)
        if res == "y":
            self.save_slots = [self.blank, self.blank, self.blank]
        self.main_menu()

    def main_menu(self):
        self.no_current_player()
        self.ui.render(self.main_menu_ui_title)
        res = self.ui.render(self.main_menu_ui_options)
        if res == "1":
            self.select_save_slot()

        if res == "2":
            self.clear_save_data()

        if res == "3":
            print("Goodbye")
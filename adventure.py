import game_manager
import ui_handler


ui = ui_handler.UI_handler()
game = game_manager.Game_manager(ui)
game.main_menu()
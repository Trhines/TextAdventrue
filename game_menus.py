from consolemenu import *
from consolemenu.items import *

menu = ConsoleMenu("Text Adventure", "Main Menu")

menu_item = MenuItem("this is the menu item")
function_item = FunctionItem("call a func", input, ["Enter an input"])
#selection_menu = SelectionMenu(["item1", "item2", "item3"])
#submenu_item = SubmenuItem("Submenu", selection_menu, menu)

menu.append_item(menu_item)
menu.append_item(function_item)
# menu.append_item(selection_menu)
# menu.append_item(submenu_item)

menu.show()

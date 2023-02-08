import game_manager
import player
import item
import ui_handler
import ui_element

main_menu = ui_element.UI_element(
    ["\nEnter a number to select","1-Play game", "2-Clear save data", "3-Exit"],
    True,
    3,
    "main_menu"
)

select_save_slot_menu = ui_element.UI_element(
    "\nselect a save slot",
    False,
    None,
    "select_save_slot_menu"
)

save_slots = ui_element.UI_element(
    "placeholder",
    True,
    None,
    "save_slots"
)

create_player = ui_element.UI_element(
    "\nEnter a name\n",
    True,
    None,
    "create_player"
)

confirm_slot = ui_element.UI_element(
    "this is a placeholder and should be set inside game manager",
    True,
    "y/n",
    "confirm_slot"
)

clear_data = ui_element.UI_element(
    "\nClear all saved Data?",
    True,
    "y/n",
    "clear_data"
)

action_loop = ui_element.UI_element(
    "",
    True,
    None,
    "action_loop"
)

nothing_happens = ui_element.UI_element(
    "Nothing happens",
    False,
    None,
    "nothing_happens"
)

end = ui_element.UI_element(
    "Returning to main menu",
    False,
    None,
    "end"
)

leave_game = ui_element.UI_element(
    "Return to main menu?",
    True,
    "y/n",
    "leave_game"
)

ui_elements = {
    main_menu.key : main_menu,
    select_save_slot_menu.key: select_save_slot_menu,
    save_slots.key: save_slots,
    create_player.key: create_player,
    confirm_slot.key: confirm_slot,
    clear_data.key: clear_data,
    action_loop.key: action_loop,
    nothing_happens.key: nothing_happens,
    end.key: end,
}

player_elements = {
    leave_game.key: leave_game
}

table_with_mirror = item.Item(
            "table_with_mirror",
            "a table with a mirror on it",
            [
            "you look into the mirror and see what you saw.",
            "The saw is sharp and breaks the mirror"
             ])
default_environment = {table_with_mirror.key: table_with_mirror}
blank_player = player.Player("Empty")
default_save_data = [blank_player, blank_player, blank_player]


ui = ui_handler.UI_handler()
game = game_manager.Game_manager(ui, ui_elements, default_save_data, default_environment, player_elements)

game.main_menu()
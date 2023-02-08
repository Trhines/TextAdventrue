import ui_element
import item

class Player:
    def __new__(cls, *args):
        return super(Player, cls).__new__(cls)

    def __init__(self, name, inventory=None, environment=None, ui_handler=None, ui_elements=None):
        self.name = name
        self.inventory = inventory
        self.environment = environment
        self.ui = ui_handler
        self.ui_elements = ui_elements

    def view_collection(self, collection, intro):
        all_descriptions = collection.get_all_descriptions()
        all_descriptions.insert(0, intro)
        descriptions = ui_element.UI_element(all_descriptions)
        self.ui.render(descriptions)

    def view_environment(self):
        self.view_collection(self.environment, "You see")

    def view_inventory(self):
        self.view_collection(self.inventory, "You have")

    def use_item(self, collection, key, fail_msg):
        try:
            item = collection.get_item(key)
            action_el = ui_element.UI_element(item.interaction)
            self.ui.render(action_el)
            return True
        except:
            msg = ui_element.UI_element(fail_msg)
            self.ui.render(msg)
            return False
              
    def take_action(self, input):
        match input:
            case "i":
                self.view_inventory()

            case "look around":
                self.view_environment()
            
            case "look into the mirror":
                if self.use_item(self.environment, "table_with_mirror","there is no mirror"):
                    saw = item.Item("saw", 
                                    "a saw", 
                                    "a saw has been added to your inventory")
                    
                    table = item.Item("table",
                                      "a normal table",
                                      "you cut the table into two halves")
                    self.environment.add_item(saw)
                    self.environment.remove_item("table_with_mirror")
                    self.environment.add_item(table)
                    return False
            
            case "take the saw":
                if self.use_item(self.environment, "saw", "there is no saw"):
                    saw = self.environment.remove_item("saw")
                    self.inventory.add_item(saw)
                    return False
            
            case "cut the table":
                if "saw" in self.inventory.get_all():
                    if self.use_item(self.environment, "table", "You can't do that"):
                        self.environment.remove_item("table")
                        table_halves = item.Item("table_halves",
                                                 "a table cut into two halves",
                                                 ["You put the two halves together and create a hole.",
                                                  "The hole is quite large."
                                                  ])
                        self.environment.add_item(table_halves)
                        return False
                    
            case "put the halves together":
                if self.use_item(self.environment, "table_halves", "You can't do that"):
                    self.environment.remove_item("table_halves")
                    hole = item.Item("hole",
                                     "a rather large hole",
                                     ["You climb into the the hole, under the house, and out.",
                                      "Congradulations! You escaped!"])
                    self.environment.add_item(hole)
                    return False
                
            case "climb into the hole":
                if self.use_item(self.environment, "hole", "what hole?"):
                    return True
                
            case "exit":
                res = self.ui.render(self.ui_elements["leave_game"])
                if res == "y":
                    return True
            


                    
                    
            
                    

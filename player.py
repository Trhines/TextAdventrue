import ui_element
import item

class Player:
    def __new__(cls, *args):
        return super(Player, cls).__new__(cls)

    def __init__(self, name, ui_handler=None, new_game=True, ui_elements=None):
        
        self.leave_game = ui_element.UI_element(
            "Return to main menu?",
            True,
            "y/n",
            "leave_game"
            )
        
        self.table_with_mirror = item.Item(
            "table_with_mirror",
            "a table with a mirror on it",
            [
            "you look into the mirror and see what you saw.",
            "The saw is sharp and breaks the mirror"
             ])
        
        self.saw = item.Item(
            "saw", 
            "a saw", 
            "a saw has been added to your inventory"
            )
                  
        self.table = item.Item(
            "table",
            "a normal table",
            "you cut the table into two halves"
            )
        
        self.table_halves = item.Item(
            "table_halves",
            "a table cut into two halves",
            [
            "You put the two halves together and create a hole.",
            "The hole is quite large."
              ])
        
        self.hole = item.Item(
            "hole",
            "a rather large hole",
            [
            "You climb into the the hole, under the house, and out.",
            "Congradulations! You escaped!"
            ])
        
        
        self.new_game = new_game
        self.name = name
        self.inventory = self.Collection(self.name, "inventory", {})
        self.environment = self.Collection(self.name, "environment",{self.table_with_mirror.key: self.table_with_mirror})
        self.ui = ui_handler
        self.ui_elements = ui_elements
    
    class Collection:
        def __new__(cls, *args, **kwargs):
            obj = object.__new__(cls)
            return obj

        def __init__(self, name, coll_type, items):
            self.name = name +"'s "+ coll_type
            self.coll_type = coll_type
            self.items = items

        def get_all(self):
            return self.items
            
        def get_all_descriptions(self):
            all_items = self.items.values()
            descriptions = [item.description for item in all_items]
            return list(descriptions)
        
        def get_item(self, key):
            return self.items.get(key)

        def add_item(self, item):
            self.items.update({item.key: item})
        
        def remove_item(self, item):
            return self.items.pop(item.key)
        
    def has_progressed(self):
        self.new_game = False

    def view_collection(self, collection, intro):
        all_descriptions = collection.get_all_descriptions()
        if len(all_descriptions) == 0:
            all_descriptions.append("nothing")
        all_descriptions.insert(0, intro)
        descriptions = ui_element.UI_element(all_descriptions)
        self.ui.render(descriptions)

    def view_environment(self):
        self.view_collection(self.environment, "\nYou see")
        return False

    def view_inventory(self):
        self.view_collection(self.inventory, "\nYou have")
        return False

    def use_item(self, collection, ref, fail_msg):
        try:
            item = collection.get_item(ref.key)
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
                return False

            case "look around":
                self.view_environment()
                return False
            
            case "look into the mirror":
                if self.use_item(self.environment, self.table_with_mirror,"there is no mirror"):
                    self.environment.add_item(self.saw)
                    self.environment.remove_item(self.table_with_mirror)
                    self.environment.add_item(self.table)
                    self.has_progressed()
                    return False
            
            case "take the saw":
                if self.use_item(self.environment, self.saw, "there is no saw"):
                    saw = self.environment.remove_item(self.saw)
                    self.inventory.add_item(saw)
                    return False
            
            case "cut the table":
                if "saw" in self.inventory.get_all():
                    if self.use_item(self.environment, self.table, "You can't do that"):
                        self.environment.remove_item(self.table)
                        self.environment.add_item(self.table_halves)
                        return False
                    
            case "put the halves together":
                if self.use_item(self.environment, self.table_halves, "You can't do that"):
                    self.environment.remove_item(self.table_halves)
                    self.environment.add_item(self.hole)
                    return False
                
            case "climb into the hole":
                if self.use_item(self.environment, self.hole, "what hole?"):
                    return True
                
            case "exit":
                res = self.ui.render(self.leave_game)
                if res == "y":
                    return True
            


                    
                    
            
                    

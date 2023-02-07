class Inventory:
    def __init__(self, items=[]):
      self.items = items
    
    def view_inventory(self):
      print("You have")
      for item in self.items:
        print(item.name)    

    def add_item(self, item):
      self.items.append(item)
      print("You add "+item.name+" to your inventory")
    
    def remove_item(self):
      print("placeholder")

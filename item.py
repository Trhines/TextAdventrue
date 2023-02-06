class Item():
    def __init__(self, name):
      self.name = name
    
    def use_item():
      print("this is a place holder func and should be replaced in child classes")

class Saw(Item):
    def use_item():
      print("You use the saw to cut the table in half")

class Table_halves(Item):
    def use_item():
      print("you put the two halves together and create a hole")

class Hole(Item):
    def use_item():
      print("you climb in the hole, under the house, and out")

class Mirror(Item):
    def use_item(self):
      print("you look into the mirror and see what you saw")
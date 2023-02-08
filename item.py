class Item():
    def __new__(cls, *args):
        return super(Item, cls).__new__(cls)
    
    def __init__(self, key, description, interaction):
      self.key = key
      self.description = description
      self.interaction = interaction

# class Table_with_mirror(Item):
#     def __init__(self):
#       self.key = "table_with_mirror"
#       self.description = "a table with a mirror on it"
      
# class Saw(Item):
#     def __init__(self):
#       self.key = "saw"
#       self.description = "a saw"

# class Table_halves(Item):
#     def __init__(self):
#       self.key = "table_halves"
#       self.description = "a table cut into two halves"

# class Hole(Item):
#     def __init__(self):
#       self.key = "hole"
#       self.description = "a very dark hole"

# class Mirror(Item):
#     def __init__(self):
#       self.key = "Mirror"
#       self.description = "a mirror"
    
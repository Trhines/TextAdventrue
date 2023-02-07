class Player:
    def __init__(self, name, inventory=None):
      self.name = name
      self.inventory= inventory
       

    def get_state(self):
      return self.state
    
    def next_step(self):
      self.state += 1
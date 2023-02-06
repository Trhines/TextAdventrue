class Player:
    def __init__(self, name, step, inventory):
      self.name = name
      self.state = step
      self.inventory= inventory
       

    def get_state(self):
      return self.state
    
    def next_step(self):
      self.state += 1
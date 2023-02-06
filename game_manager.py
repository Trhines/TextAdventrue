class Game_manager:
    def __init__(self, slots, save):
        self.save_slots = slots
        self.current_player = save
    
    def set_current_player(self, slot_num):
        self.current_player = self.save_slots[slot_num]

    def set_save_data(self, index, new_player):
        self.save_slots[index] = new_player

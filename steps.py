class Step:
    def __init__(self, question, answer, hint):
      self.question = question
      self.answer = answer
      self.hint = hint

    def get_question(self):
      print(self.question)

    def get_answer(self):
      print(self.answer)
      
    def get_hint(self):
      print(self.hint)
# step1
question1 = "You are in a room with no windows and doors. The only thing in the room is a table with a mirror on it. Your goal is to escape.\nWhat do you do?"
answer1 = "look in the mirror"
hint1 = "look in the mirror"
response1 = "You look in the mirror and see what you saw.\nYou pick up the saw."
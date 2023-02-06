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
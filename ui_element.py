class UI_element:
    def __init__(self, prompt="", response=False, validator=None):
        self.prompt = prompt
        self.response = response
        self.validator = validator
    
    def set_prompt(self, x):
        self.prompt = x

    def set_response(self, x):
        self.response = x
   
    def set_validator(self, x):
        self.validator = x

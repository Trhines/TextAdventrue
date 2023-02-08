# this class should not contain actual UI elements but be responsible for rendering
class UI_handler:
    def __init__(self):
        self
        
    def verify_input(self, input, arg):
        if arg is None:
            return True
        
        elif isinstance(arg, int):
            if input.isdigit():
                return 1 <= int(input) <= arg
            
        elif arg.lower() == "y/n":
            if input.lower() == "y" or input.lower() == "n":
                return True
            else:
                return False
            
        else:
            #placeholder
            return False
        
    def render(self, element, check_commands = lambda res: True):
        if isinstance(element.prompt, list):
            for i in element.prompt:
                print(i)
        else:
            print(element.prompt)
        
        if element.validator == "y/n":
            print("y/n")

        if(element.response):
            res = input()
            check_commands(res)
            if self.verify_input(res, element.validator):
                return res
            else:
                print('\nInvalid input')
                return self.render(element, check_commands)
        else:
            return
# this class should not contain actual UI elements but be responsible for rendering
class UI_handler:
    def __init__(self):
        self
        
    def verify_input(self, input, arg):
        if arg is None:
            return True
        elif input.isdigit():
            if isinstance(arg, int):
                return 1 <= int(input) <= arg
        else:
            #placeholder
            return False
        
    def render(self, element, check_commands):
        if isinstance(element.prompt, list):
            for i in element.prompt:
                print(i)
        else:
            print(element.prompt)

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
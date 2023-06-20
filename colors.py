from colorama import Fore

class colors:
    def __init__(self):
        self.color = Fore

    def green(self):
        return self.color.GREEN
    
    def yellow(self):
        return self.color.YELLOW
    
    def red(self):
        return self.color.RED
    
    def black(self):
        return self.color.BLACK
    
    def none(self):
        return self.color.RESET
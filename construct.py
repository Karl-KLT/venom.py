import os
from time import sleep
from colors import colors
from pyfiglet import Figlet
class construct():
    def __init__(self):
        sleep(1)
        if os.name == "nt":
            os.system("clear")
        else:
            os.system("cls")
        print(colors().yellow(), Figlet("crawford").renderText("venom.py") +colors().none())
        try:
            if(os.getuid() != 0):
                print(colors.red+'u need to have root privileges to run this script')
                quit();
        except:
            pass
# [open-source-script:version-1.0.0]

# imports
from time import sleep
from menu import menu
import os
from colors import colors
from construct import construct
construct()
try:
    section_input = input(f'''
1 - download tools (Beta)
    
>> ''')
    menu(section_input)
except KeyboardInterrupt:
    print(f"\n\n {colors().green()}(thx for using venom.py){colors().none()} \n")         
    

        
        
        




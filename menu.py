import os
from time import sleep
import sys,subprocess,shutil
from colors import colors  
from construct import construct
class menu:
    def __init__(self,number = None):
        construct()
        if number != None:
            self.path = os.path.dirname(__file__)
            if os.path.exists(f"{self.path}/units") and os.path.exists(f"{self.path}/units.py"):
                print(f"\n{colors().green()}(folder units exists){colors().none()}\n")    
                self.number = number
                self.menu()
            else:
                print(f"\n{colors().red()}(not found 'units' or 'units.py'){colors().none()}\n")    
    # #################################### 
    # types
    # inits
    def path(self):
        return self.path
    # end inits
    def Types(self):
        return [
            'kali',
            'garuda'
        ]
         
    
    def getAllTypes(self, index=False):
        types = {}
        for type in self.Types():
            if index:    
                types[type] = self.Types().index(type)
            else:
                types[self.Types().index(type)] = type
        return types
    
    def getOneType(self,index,withIndex=False):
        return self.getAllTypes(withIndex)[index]
    # end of types
    # #################################### 
    def menu(self):
        if(self.number == "1"): # download tools
            self.units()
        else:
            print(f"{colors().red()}option's not found{colors().none()}")
            quit()
    
    
    def units(self):
        try:
            for type in self.Types():
                print(self.getOneType(type,True)+1,"-",type)
                
            index = input('\n>> ')

            if index:
                # index = self.getOneType(int(index) - 1)
                index = int(index)-1
                path = self.path
                from units import units
                units(path,index)




                # if index == 'kali':
                
                #     if os.path.exists('/usr/local/bin/apktool') and os.path.exists('/usr/local/bin/apktool.jar'):
                #         print('(apktool) already installed on ur device')
                #     else:
                #         shutil.copy(f"{path}/units/ApkTool/apktool","/usr/local/bin/")
                #         shutil.copy(f"{path}/units/ApkTool/apktool.jar","/usr/local/bin/")
                #         print(f"tools has been installed in ur device ({index})")
                
                # elif index == "garuda":
                #     if os.path.exists('/bin/apktool') and os.path.exists('/bin/apktool.jar'):
                #         print('(apktool) already installed on ur device')
                #     else:
                #         shutil.copy(f"{path}/units/ApkTool/apktool","/bin/")
                #         shutil.copy(f"{path}/units/ApkTool/apktool.jar","/bin/")
                #         print(f"tools has been installed in ur device ({index})")
                                            

                    
                
            
        except:
            print('smth went wrong .. error:')
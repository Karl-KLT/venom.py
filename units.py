from colors import colors
import os,shutil
from construct import construct
from downloader import downloader
from menu import menu
class units:
    def __init__(self,path,index):
        construct()
        self.path = path
        self.index = index # type of device
        print(f"{colors().green()}({menu().getOneType(self.index)}){colors().none()}\n")
        self.showUnits()


    def showUnits(self):
        units = os.listdir(self.path+"/units")

        for unit in units:
            print(units.index(unit)+1 ,"-", unit)

        unit = input("\n>> ")
        unit = int(unit)-1
        self.downloadUnits(unit)


    def getTool(self,index):
        units = os.listdir(self.path+"/units")
        return units[index]
    
    def downloadUnits(self,unit):
        unitName = self.getTool(unit)
        deviceName = menu().getOneType(self.index)
        downloader(unitName,deviceName,self.path)
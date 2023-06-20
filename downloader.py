import shutil,os
from colors import colors
class downloader:
    def __init__(self,unitName,deviceName,path):
        self.unitName = unitName
        self.deviceName = deviceName
        self.path = path+"/units"
        self.downloader()

    def downloader(self):
        # ///////////////////////////////////////////////////////////
        if self.deviceName == "kali" :
            # ////////////////////////////
            if self.unitName == "ApkTool":
                    if os.path.exists('/usr/local/bin/apktool') and os.path.exists('/usr/local/bin/apktool.jar'):
                        print(f'({self.unitName}) already installed on ur device')
                    else:
                        shutil.copy(f"{self.path}/ApkTool/apktool","/usr/local/bin/")
                        shutil.copy(f"{self.path}/ApkTool/apktool.jar","/usr/local/bin/")
                        print(f"{colors().green()}tools has been installed in ur device {colors().yellow()}({self.deviceName}){colors().none()}")
        # ///////////////////////////////////////////////////////////
        elif self.deviceName == "garuda":
            # ////////////////////////////
            if self.unitName == "ApkTool":
                if os.path.exists('/bin/apktool') and os.path.exists('/bin/apktool.jar'):
                    print(f'({self.unitName}) already installed on ur device')
                else:
                    shutil.copy(f"{self.path}/ApkTool/apktool","/bin/")
                    shutil.copy(f"{self.path}/ApkTool/apktool.jar","/bin/")
                    print(f"{colors().green()}tools has been installed in ur device {colors().yellow()}({self.deviceName}){colors().none()}")
       
        
        
        
        # /////////////////////////////////////////////////////////////////
        else:
            print(f"\n {colors().red()}option's not found{colors().none()} \n")



        # if 1==1:

        
        # elif index == "garuda":
        #     if os.path.exists('/bin/apktool') and os.path.exists('/bin/apktool.jar'):
        #         print('(apktool) already installed on ur device')
        #     else:
        #         shutil.copy(f"{path}/units/ApkTool/apktool","/bin/")
        #         shutil.copy(f"{path}/units/ApkTool/apktool.jar","/bin/")
        #         print(f"tools has been installed in ur device ({index})")
            

import os
import urllib.request
import zipfile
import shutil
import time
from subprocess import Popen


supercpg_master_directory = os.getcwd()
supercpg_directory = supercpg_master_directory+"\supercpg-updates"
supercpg_file = supercpg_directory+"\\main.exe"
supercpg_rev = supercpg_directory+"\\Rev.txt"


def installation():
    print("*** Downloading new version ***")
    urllib.request.urlretrieve("https://gitlab.devtools.intel.com/ianimash/supercpg/-/archive/updates/supercpg-updates.zip", supercpg_master_directory+"\\supercpg_new.zip")
    print("*** Extracting new version ***")
    zip_ref = zipfile.ZipFile(supercpg_master_directory+"\supercpg_new.zip", 'r')
    zip_ref.extractall(supercpg_master_directory)
    zip_ref.close()
    os.remove(supercpg_master_directory+"\supercpg_new.zip")
    time.sleep(5)
    
def upgrade():    
    print("*** Removing old files ***")
    shutil.rmtree(supercpg_directory)
    time.sleep(10)
    installation()


### Is supercpg already installed? If yes get file size to compare for upgrade
if os.path.isfile(supercpg_file):
    local_file_size = int(os.path.getsize(supercpg_rev))
    # print(local_file_size)
    ### Check if update needed:
    f = urllib.request.urlopen("https://gitlab.devtools.intel.com/ianimash/supercpg/-/raw/updates/Rev.txt") # points to the exe file for size
    i = f.info()
    web_file_size = int(i["Content-Length"])
    # print(web_file_size)


    if local_file_size != web_file_size:# upgrade available
        updt = input("*** New upgrade available! enter <y> to upgrade now, other key to skip upgrade *** ")
        if updt == "y" or updt == "Y": # proceed to upgrade
            upgrade()

### supercpg wasn't installed, so we download and install it here                
else:
    install = input("Welcome to Need4Seed! If you enter <y> Need4Seed will be downloaded in the same folder where this file is.\nAfter the installation, this same file you are running now (\"Need4Seed.exe\") will the one to use to open Need4Seed :)\nEnter any other key to skip the download\n -->")
    if install == "y" or install == "Y":
        installation()

print('Ready')


### We open the real application:
try:
    Popen(supercpg_file)
    print("*** Opening Need4Seed ***")
    time.sleep(20)
except:
    print('Failed to open application, Please open manually in subfolder')
    pass
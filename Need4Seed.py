import os
import urllib.request
import zipfile
import shutil
import time
from subprocess import Popen


need4seed_master_directory = os.getcwd()
need4seed_directory = need4seed_master_directory+"\\need4seed-updates"
need4seed_file = need4seed_directory+"\\main.exe"
need4seed_rev = need4seed_directory+"\\Rev.txt"

proxy_handler = urllib.request.ProxyHandler({'https': 'http://proxy-dmz.intel.com:912'})
opener = urllib.request.build_opener(proxy_handler)
urllib.request.install_opener(opener)

def installation():
    print("*** Downloading new version ***")
    urllib.request.urlretrieve("https://github.com/idriss-animashaun-intel/need4seed/archive/refs/heads/updates.zip", need4seed_master_directory+"\\need4seed_new.zip")
    print("*** Extracting new version ***")
    zip_ref = zipfile.ZipFile(need4seed_master_directory+"\\need4seed_new.zip", 'r')
    zip_ref.extractall(need4seed_master_directory)
    zip_ref.close()
    os.remove(need4seed_master_directory+"\\need4seed_new.zip")
    time.sleep(5)
    
def upgrade():    
    print("*** Removing old files ***")
    shutil.rmtree(need4seed_directory)
    time.sleep(10)
    installation()


### Is need4seed already installed? If yes get file size to compare for upgrade
if os.path.isfile(need4seed_file):
    local_file_size = int(os.path.getsize(need4seed_rev))
    # print(local_file_size)
    ### Check if update needed:
    f = urllib.request.urlopen("https://github.com/idriss-animashaun-intel/need4seed/raw/updates/Rev.txt") # points to the exe file for size
    i = f.info()
    web_file_size = int(i["Content-Length"])
    # print(web_file_size)


    if local_file_size != web_file_size:# upgrade available
        updt = input("*** New upgrade available! enter <y> to upgrade now, other key to skip upgrade *** ")
        if updt == "y" or updt == "Y": # proceed to upgrade
            upgrade()

### need4seed wasn't installed, so we download and install it here                
else:
    install = input("Welcome to Need4Seed! If you enter <y> Need4Seed will be downloaded in the same folder where this file is.\nAfter the installation, this same file you are running now (\"Need4Seed.exe\") will the one to use to open Need4Seed :)\nEnter any other key to skip the download\n -->")
    if install == "y" or install == "Y":
        installation()

print('Ready')


### We open the real application:
try:
    Popen(need4seed_file)
    print("*** Opening Need4Seed ***")
    time.sleep(20)
except:
    print('Failed to open application, Please open manually in subfolder')
    pass
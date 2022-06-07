import os
import urllib.request
import zipfile
import shutil
import time


need4seed_master_directory = os.getcwd()
need4seed_file = need4seed_master_directory+"\\Need4Seed.exe"
Old_need4seed_directory = need4seed_master_directory+"\\need4seed_exe-master"

proxy_handler = urllib.request.ProxyHandler({'https': 'http://proxy-dmz.intel.com:912'})
opener = urllib.request.build_opener(proxy_handler)
urllib.request.install_opener(opener)


def installation():
    urllib.request.urlretrieve("https://github.com/idriss-animashaun-intel/need4seed/archive/refs/heads/master.zip", need4seed_master_directory+"\\need4seed_luancher_new.zip")
    print("*** Updating Launcher Please Wait ***")
    zip_ref = zipfile.ZipFile(need4seed_master_directory+"\\need4seed_luancher_new.zip", 'r')
    zip_ref.extractall(need4seed_master_directory)
    zip_ref.close()
    os.remove(need4seed_master_directory+"\\need4seed_luancher_new.zip")

    src_dir = need4seed_master_directory + "\\need4seed-master"
    dest_dir = need4seed_master_directory
    fn = os.path.join(src_dir, "Need4Seed.exe")
    shutil.copy(fn, dest_dir)

    shutil.rmtree(need4seed_master_directory+"\\need4seed-master")

    time.sleep(5)
    
def upgrade():
    print("*** Updating Launcher Please Wait ***")    
    print("*** Removing old files ***")
    time.sleep(20)
    os.remove(need4seed_file)
    time.sleep(10)
    installation()


### Is need4seed already installed? If yes get file size to compare for upgrade
if os.path.isfile(need4seed_file):
    local_file_size = int(os.path.getsize(need4seed_file))
    # print(local_file_size)

    url = 'https://github.com/idriss-animashaun-intel/need4seed/raw/master/Need4Seed.exe'
    f = urllib.request.urlopen(url)

    i = f.info()
    web_file_size = int(i["Content-Length"])
    # print(web_file_size)

    if local_file_size != web_file_size:# upgrade available
        upgrade()

### need4seed wasn't installed, so we download and install it here                
else:
    installation()

if os.path.isdir(Old_need4seed_directory):
        print('removing need4seed_exe-master')
        time.sleep(5)
        shutil.rmtree(Old_need4seed_directory)

print('Launcher up to date')
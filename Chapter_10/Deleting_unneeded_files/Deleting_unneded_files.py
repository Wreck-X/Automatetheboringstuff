import os,shutil
from pathlib import Path
path_ = input('enter absolute path- ')
os.chdir(path_)
for folder,subfolder,file in os.walk(path_):
    for i in file:
        if os.path.getsize(i) >= 104857600:
            # os.unlink(path_+'/'+i) #(deletes files)
            print(i)

import os,shutil
from pathlib import Path
for folder,subfolders,files in os.walk(Path.home()/'Desktop/Automatetheboringstuff/chapter_10/Selective_Copy'):
    for subfolder in subfolders:
        if subfolder == 'Source_':
            os.chdir(Path.home()/'Desktop/Automatetheboringstuff/chapter_10/Selective_Copy'/'Source_')
            for i in os.listdir():
                shutil.copy(Path.home()/'Desktop/Automatetheboringstuff/chapter_10/Selective_Copy'/'Source_'/i,Path.home()/'Desktop/Automatetheboringstuff/chapter_10/Selective_Copy'/'Destination'/i)
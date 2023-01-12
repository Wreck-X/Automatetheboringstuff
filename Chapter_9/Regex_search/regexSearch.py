import os
import re
from pathlib import Path
os.chdir(Path.home()/'Desktop/Automatetheboringstuff/chapter_9/Regex_search')

def regexSearch(regex):
    directory = os.listdir()
    search = re.compile(regex)
    listofregex = []
    for i in directory:
        if i.endswith('.txt'):
            file = open(i,'r')
            string = file.read()
            if search.findall != []:
                listofregex = listofregex + search.findall(string)
            file.close()
    return listofregex
        
print(regexSearch(r'[0-9]{2}/[0-9]{2}/[1-9][0-9]{3}'))
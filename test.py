import re,os,shutil
from pathlib import Path
dirlist = os.listdir('/home/wreck/Desktop/Automatetheboringstuff/Chapter_10/Filling_in_the_gaps/Stuff')
numbers = re.compile('[0-9]+')
chars = re.compile('[^0-9]*')
numlist = []
charlist = []
final = []
for i in dirlist:
    num = int(numbers.search(i).group())
    char = chars.search(i).group()
    charlist.append(char)
    numlist.append(num)
for index,element in enumerate(numlist):
    try:
        if numlist[index + 1] - element!= 1:
            numlist[index + 1] = element + 1
            print(numlist)
    except IndexError:
        pass
for number,character in zip(numlist,charlist):
    final.append(character+str(number)+'.txt')
for old,new in zip(dirlist,final):
    shutil.move(fr'/home/wreck/Desktop/Automatetheboringstuff/Chapter_10/Filling_in_the_gaps/Stuff/{old}',fr'/home/wreck/Desktop/Automatetheboringstuff/Chapter_10/Filling_in_the_gaps/Stuff/{new}')
print(final)

import re
def regexstrip(string):
    lcheck = re.compile(r'^(\s)*')
    rcheck = re.compile(r'(\s)*$')
    templout = lcheck.search(string)
    temprout = rcheck.search(string)
    lout = len(templout.group())
    rout = len(temprout.group())
    liststring = list(string)
    for i in range(lout):
        liststring.pop(0)
    for j in range(rout):
        liststring.pop()
    string = ''.join(liststring)
    print(string)

string = '        bananana apple          '
regexstrip(string)
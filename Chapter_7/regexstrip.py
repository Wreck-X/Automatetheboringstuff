import re
def regexstrip(string, strp):
    lcheck = re.compile(fr'^({strp})*')
    rcheck = re.compile(fr'({strp})*$')
    templout = lcheck.findall(string)
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

string = 'aaaaaabananana apple aaaa'
regexstrip(string,'a')
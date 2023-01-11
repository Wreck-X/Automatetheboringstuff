import re


def strongornot(password):
    stronk = re.compile(r'\w{8,}')
    upperstronk = re.compile(r'[A-Z]')
    lowerstronk = re.compile(r'[a-z]')
    num = re.compile(r'\d+')
    check1 = stronk.search(password)
    check2 = upperstronk.search(password)
    check3 = lowerstronk.search(password)
    check4 = num.search(password)
    if check1 != None and check2 != None and check3 != None and check4 != None:
        print('Strong')
    else:
        print('Not Strong')
        
strongornot('AAaa12aaa')
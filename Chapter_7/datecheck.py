import re

datecheck = re.compile(r'([0-9]{2})/([0-9]{2})/([1-9][0-9]{3})')
something = datecheck.search("asdasdsada ssddafg 29/02/2024 weasdadd wqeqweqe qwqweqewqweqw eq")
try:
    day = something.group(1)
    month = something.group(2)
    year = something.group(3)
except AttributeError:
    print('Not found')
    exit()
intday = int(day)
intmonth = int(month)
intyear = int(year)
print(intday,intmonth,intyear)
validdate = False
thirtymonth = ['04','06','09','11']
thirtyonemonth = ['01','03','05','07','08','10','12']
if month in thirtymonth:
    if intday <= 30 and intyear > 1000 and intyear <= 2999:
        validdate = True
if month in thirtyonemonth:
    if intday <= 31 and intyear > 1000 and intyear <= 2999:
        validdate = True
if month == '02':
    leapyear = None
    if intyear % 400 and intyear % 100 == 0:
        leapyear = True
    elif intyear % 4 == 0 and intyear % 100 != 0:
        leapyear = True
    else:
        leapyear = False
    
    if leapyear == True:
        if intday <= 29 and intyear > 1000 and intyear <=2999:
            validdate = True
    elif leapyear == False:
        if intday <= 28 and intyear > 1000 and intyear <= 2999:
            validdate = True
print(validdate)
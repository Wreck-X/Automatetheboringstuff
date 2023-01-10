import pyinputplus as pyinp
breadtype = pyinp.inputMenu(['wheat','white','sourdough'])
proteintype = pyinp.inputMenu(['chicken','turkey','ham','tofu'])
yesnocheese = pyinp.inputYesNo('Do you want cheese??? ')
if yesnocheese == 'yes':
    cheesetype = pyinp.inputMenu(['cheddar','swiss','mozzerella'])
howmany = pyinp.inputInt('how many? ',min= 1)

menu = {'wheat':1,'white':1,'sourdough':2,'chicken':5,'turkey':3,'ham':10,'tofu':2,'cheddar':1,'swiss':1,'mozerella':1}

cost = (menu[breadtype] + menu[proteintype] + menu[cheesetype])* howmany
print('cost = ',cost,'$')
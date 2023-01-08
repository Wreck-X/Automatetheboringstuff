import random

final = 0
for experimentNumber in range(10000):
    list_ = []
    for i in range(100):
        if random.randint(0,1) == 0:
            list_.append('H')
        else:
            list_.append('T')
    for index,element in enumerate(list_):
        sublist = []
        sublist.append(element)
        try:
            for i in range(1,6):
                sublist.append(list_[index + i])
        except IndexError:
            break
        if len(set(sublist)) == 1:
            print(sublist)
            final +=1
            break
print(f'Chance of streak: {(final/100)}')
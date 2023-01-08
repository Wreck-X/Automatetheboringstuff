spam = ['apples', 'bananas', 'tofu', 'cats']
for index,element in enumerate(spam):
    if index + 1 == len(spam):
        print('and',element)
    else:
        if index + 1== len(spam) - 1:
            print(element,end = ' ')
        else:
            print(element,end = ',')
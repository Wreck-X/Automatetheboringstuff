spam = ['apples', 'bananas', 'tofu', 'cats']
for index,element in enumerate(spam):
    if index + 1 == len(spam):
        print('and',element)
    else:
        print(element,end = ' ')
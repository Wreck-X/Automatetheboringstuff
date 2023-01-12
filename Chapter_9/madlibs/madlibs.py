import re
file = open('./madlibs.txt','r')
filestring  = file.readlines()
final = ''
for i in range(len(filestring)):
    line = filestring[i].split()
    for index,word in enumerate(line):
        upper = re.compile('[A-Z]*')
        search_ = upper.search(word)
        word = search_.group()
        match word:
            case 'ADJECTIVE':
                adjecive = input('Enter an adjecive: ')
                line[index] = adjecive
            case 'VERB':
                verb = input('Enter a verb: ')
                line[index] = verb
            case 'NOUN':
                noun = input('Enter a noun: ')
                line[index] = noun
    final = final + ' '.join(line) + '\n'
filew = open('./madlibs.txt','w')
filew.write(final)    
file.close()
filew.close()
import sys,pyperclip,shelve

TEXT = {'agree': """Yes, I agee. That sounds fine to me.""",'busy': """Sorry, can we do this later this week or next week?""",'upsell':"""Would you consider making this a monthly donation?"""}
shelfFile = shelve.open('Shelf')
shelfFile['agree'] = TEXT['agree']    
shelfFile['busy'] = TEXT['busy']
shelfFile['upsell'] = TEXT['upsell']

if len(sys.argv) <2 :
    print('Usage: python mclipimproved.py [keyphrase]')
    sys.exit()
keyphrase = sys.argv[1]
if keyphrase == 'save':
    if len(sys.argv) < 4:
        print('Usage: python mclipimproved.py save [keyphrase] [value]')
        sys.exit()
    if sys.argv[1] not in shelfFile:
        shelfFile[sys.argv[2]] = sys.argv[3]
        print('Saved')
if keyphrase == 'delete':
    if len(sys.argv )< 3:
        print('Usage: python mclipimproved.py delete [keyphrase]')
        sys.exit()
    if sys.argv[2] in shelfFile:
        del shelfFile[sys.argv[2]]
        print(f'Deleted values for {sys.argv[2]}')
        sys.exit()
if keyphrase == 'list':
    for i in shelfFile:
        print(i)
if keyphrase == 'copy' :
    if sys.argv[2] in shelfFile:
        pyperclip.copy(shelfFile[sys.argv[2]])
        print('Text for',sys.argv[2],'copied to clip board.')
    else:
        print('There is no text for',sys.argv[2])
shelfFile.close()
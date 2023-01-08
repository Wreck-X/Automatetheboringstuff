def isValidChessBoard(dict):
    validnums = ['1','2','3','4','5','6','7','8']
    validletters = ['a','b','c','d','e','f','g','h']

    numcheck = True
    lettercheck = True

    for i in dict:
        if i[0] not in validnums:
            numcheck = False
        if i[1] not in validletters:
            lettercheck = False

    blackcounter = 0
    blackpawncounter =0
    whitecounter = 0
    whitepawncounter = 0

    for i in dict.values():
        if i[0] == 'b':
            blackcounter += 1
            if i[1:] == 'pawn':
                blackpawncounter += 1
        if i[0] == 'w':
            whitecounter += 1
            if i[1:] == 'pawn':
                whitepawncounter += 1

    final = False
    if numcheck == True and lettercheck == True and blackcounter <= 16 and blackpawncounter <= 8 and whitecounter <= 16 and whitepawncounter <= 8:
        final = True

    return final

print(isValidChessBoard({'1h': 'bking', '6c': 'wqueen', '8g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}))
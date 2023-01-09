tableData = [['apples', 'oranges', 'cherries', 'banana'],['Alice', 'Bob', 'Carol', 'David'],['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colHight= len(table)
    colWidthlen = len(table[0])
    colWidth = [0] * len(table)
    for i in range(len(table)):
        colWidth[i] = max(tableData[i],key=len)
    for i in range(colWidthlen):
        for j in range(colHight):
            print(table[j][i].rjust(len(colWidth[j])),end = ' ')
        print()
printTable(tableData)
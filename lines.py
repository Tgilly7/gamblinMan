LINE1 = [5, 6, 7, 8, 9]
LINE2 = [0, 1, 2, 3, 4]
LINE3 = [10, 11, 12, 13, 14]
LINE4 = [0, 6, 12, 8, 4]
LINE5 = [10, 6, 2, 8, 14]
LINE6 = [10, 11, 7, 3, 4]
LINE7 = [0, 1, 7, 13, 14]
LINE8 = [5, 11, 7, 3, 9]
LINE9 = [5, 1, 7, 13, 9]
LINE10 = [10, 6, 7, 8, 4]
LINE11 = [10, 6, 7, 8, 14]
LINE12 = [5, 11, 12, 8, 4]
LINE13 = [5, 1, 2, 8, 14]
LINE14 = [5, 6, 12, 8, 4]
LINE15 = [5, 6, 2, 8, 14]

 

def easyout(result):
    print('__________________________________')
    for i in range(0,5):
        print(result[i], end=" ")
    print('\n')
    for i in range(5, 10):
        print(result[i], end=" ")
    print('\n')
    for i in range(10, 15):
        print(result[i], end=" ")
    print('\n___________________________________')


def checkLines(result, linesList):
    goodLines = []
    line = 1
    for i in range(len(linesList)):
        isLine = True
        start = result[i][0]
        for val in linesList[i]:
            if result[val] != start:
                isLine = False
                break
        line += 1
        if isLine == True:
            goodLines.append(line)
 
    return goodLines

 
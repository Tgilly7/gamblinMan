import random
from lines import *
import timeit

 

 

#symbols = ['10', 'J', 'Q', 'K', 'A', 'Dragon', 'Wizard', 'Princess']
symbols = ['10', 'J', 'Q', 'K', 'A', 'D', 'W', 'P']
weights = [15, 13, 9, 7, 5, 5, 2, 1]
linesList = [LINE1, LINE2, LINE3, LINE4, LINE5, LINE6, LINE7, LINE8, LINE9, LINE10, LINE11, LINE12, LINE13, LINE14, LINE15]

 

 

 

for i in range(10000):
    result = random.choices(symbols, weights, k = 15)  
    goodLines = checkLines(result, linesList)
    if goodLines:
        easyout(result)
        print(goodLines)
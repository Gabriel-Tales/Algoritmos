def printList(newList):
    for i, n in enumerate(newList):
        print(f"{i}: {n}")
        
from random import randint

newList = [5, 2, 4, 6, 1, 3]
#newList = [randint(0,50) for i in range(6)]


j = 1

while j < len(newList):
    currentNumber = newList[j]
    i = j - 1
    
    while i >= 0 and newList[i] > currentNumber:
        newList[i + 1] = newList[i]
        i -= 1
    
    newList[i + 1] = currentNumber
    
    j += 1

printList(newList)
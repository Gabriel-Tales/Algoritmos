from random import randint

newList = [randint(0,50) for i in range(20)]

value = randint(0,50)

#newList[randint(0, len(newList))] = value

for i, n in enumerate(newList):
    print(f"{i}: {n}")

print(f"buscando o valor {value}")

valueIndex = ""
i = 0
while i < len(newList):
    if(newList[i] == value):
        valueIndex = i
        break
    i += 1

if valueIndex != "":
    print(f"o valor {value} foi encontrado na posição {i}")
else:
    print(f"valor {value} nao encontrado na lista")
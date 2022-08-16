from random import randint
a = [randint(0,1) for i in range(16)]#[0, 1, 0, 1]
b = [randint(0,1) for i in range(16)]#[1, 1, 0, 0]

print(f"lista A: {a}")
print(f"lista B: {b}")

sum = [0 for i in range(len(a) + 1)]

i = 0
addSum = 0
while(i < len(a)):
    currentSum = a[i] + b[i] + addSum
    addSum = 0
    if(currentSum == 0):
        sum[i] = 0
    elif (currentSum == 1):
        sum[i] = 1
    elif (currentSum == 2):
        addSum = 1
        sum[i] = 0
    elif (currentSum == 3):
        addSum = 1
        sum[i] = 1
    i += 1

sum[len(sum) - 1] = addSum

print(f"lista C: {sum}")
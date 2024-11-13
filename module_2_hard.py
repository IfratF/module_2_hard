enterValue = int(input())
denominators = [enterValue]
outValues = []

for i in range(2, enterValue // 2):
    if enterValue % i == 0:
        denominators.append(i)

for i in denominators:
    for x in range(1, (i // 2) + 1):
        outValues.append(x)
        outValues.append(i - x)

print(''.join(map(str, outValues)))

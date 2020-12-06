inputFile = open("Day 1\input.txt", "r")
expenseList = []
a = 0

for line in inputFile:
    expenseList.append(int(line.strip("\n")))
inputFile.close()

for expenseA in expenseList:
    expenseB = expenseA
    for expenseB in expenseList:
        expenseC = expenseB
        for expenseC in expenseList:
            if expenseC + expenseB + expenseA == 2020:
                print(expenseA*expenseB*expenseC)
                a = 1
                break
        if a !=0:
            break
    if a !=0:
        break
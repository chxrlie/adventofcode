inputFile = open("2020\Day 1\input.txt")
expenseList = []
a = 0
b = 0
for line in inputFile:
    expenseList.append(int(line.strip("\n")))
inputFile.close()

for expense in expenseList:
    check = expense
    for expense in expenseList:
        if check + expense == 2020:
            a = check
            b = expense
            break
    if a != 0:
        break
print(a*b)

import re

def policyCheck(posA, posB, policyLet, splitPass):
    if splitPass[posA] == policyLet and splitPass[posB] == policyLet:
        print("Both")
        return False
    elif splitPass[posA] != policyLet and splitPass[posB] != policyLet:
        print("Neither")
        return False
    elif splitPass[posA] == policyLet and splitPass[posB] != policyLet:
        print("PosA Match")
        return True
    else:
        print("PosB Match")
        return True

inputFile = open("2020\Day 2\input.txt", "r")
passwordList = []
validPasswords = []

for line in inputFile:
    passwordList.append(line.strip("\n"))
inputFile.close()

for password in passwordList:
    passwordLine = re.findall("\w+", password)
    passW = passwordLine[3]
    splitPass = re.findall("\w", passW)
    posA = int(passwordLine[0])-1
    posB = int(passwordLine[1])-1
    policyLet = passwordLine[2]

    if policyCheck(posA, posB, policyLet, splitPass):
        validPasswords.append(passW)
        print("{} is valid.".format(passW))
    else:
        print("{} is not valid.".format(passW))

print("Valid Passwords: {}".format(len(validPasswords)))
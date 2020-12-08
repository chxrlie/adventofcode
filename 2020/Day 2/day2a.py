import re

inputFile = open("2020\Day 2\input.txt", "r")
passwordList = []
validPasswords = []

for line in inputFile:
    passwordList.append(line.strip("\n"))
inputFile.close()

for password in passwordList:
    passwordLine = re.findall("\w+", password)
    passW = passwordLine[3]
    policyMin = int(passwordLine[0])
    policyMax = int(passwordLine[1])
    policyLet = passwordLine[2]
    if len(re.findall(policyLet, passW)) >= policyMin and len(re.findall(policyLet, passW)) <= policyMax:
        validPasswords.append(passW)
        print("{} is valid.".format(passW))
    else:
        print("{} is not valid.".format(passW))

print("Valid Passwords: {}".format(len(validPasswords)))
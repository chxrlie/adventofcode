import re

inputFile = open("Day 2\input.txt", "r")
passwordList = []
alphabet = "abcdefghijklmnopqrstuvwxyz"

validPasswords = []

for line in inputFile:
    passwordList.append(line.strip("\n"))
inputFile.close()

for password in passwordList:
    passW = password[password.rindex(":"):].strip(": ")
    policyMin = password[:password.rindex("-")]
    policyMax = password[password.rindex("-"):password.rindex(":")].strip("-:abcdefghijklmnopqrstuvwxyz")
    policyLet = password[:password.rindex(":")].strip("-1234567890")
    strippedPass = re.sub("[^" + policyLet + "]", "", passW)
    print("Password: {}\nMin: {}\nMax: {}\nLetter: {}\nStripped: {}\n".format(passW, policyMin, policyMax, policyLet, strippedPass))
    if len(strippedPass) >= int(policyMin) and len(strippedPass) <= int(policyMax):
        validPasswords.append(passW)
        print("Valid Password")

print("Valid Passwords: {}".format(len(validPasswords)))
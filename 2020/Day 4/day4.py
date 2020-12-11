import re

passportFile = open("2020\Day 4\input.txt").read().splitlines()
requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
validPassports = 0
passportSet = []

for line in passportFile:
    if line != "":
        passportSet.append(line)
    elif all(words in ' '.join(map(str, passportSet)) for words in requiredFields):
        print("Valid Passport")
        validPassports += 1
        passportSet = []
    else:
        print("Invalid Passport")
        passportSet = []
        
print(validPassports)
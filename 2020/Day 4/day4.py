import re

passportFile = open("2020\Day 4\input.txt").read().splitlines()
requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def part1():
    validPassports = 0
    passportSet = []
    for line in passportFile:
        if line != "":
            passportSet.append(line)
        elif all(words in ' '.join(map(str, passportSet)) for words in requiredFields):
            validPassports += 1
            passportSet = []
        else:
            passportSet = []
    return validPassports

print("Part 1, Valid Passports: {}".format(part1()))
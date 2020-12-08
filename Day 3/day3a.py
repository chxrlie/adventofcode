import re

mapFile = open("Day 3\input.txt", "r").read().splitlines()
#print(mapFile)

treeTile = "#"
moveRight = 3
moveDown = 1
currentRight = 0
currentDown = 0
trees = 0

while currentDown < len(mapFile):
    if mapFile[currentDown][currentRight % len(mapFile[0])] == treeTile:
        trees += 1
        print("Tree Found")
    currentRight += moveRight
    currentDown += moveDown
print(trees)
mapFile.close()
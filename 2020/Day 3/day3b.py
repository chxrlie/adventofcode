import math

mapFile = open("2020\Day 3\input.txt", "r").read().splitlines()
treeTile = "#"
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
treeList = []

def findTrees(a, b):
    moveRight = a
    moveDown = b
    currentRight = 0
    currentDown = 0
    trees = 0
    while currentDown < len(mapFile):
        if mapFile[currentDown][currentRight % len(mapFile[0])] == treeTile:
            trees += 1
        currentRight += moveRight
        currentDown += moveDown
    return(trees)

mapFile.close()
for slope in slopes:
    treeList.append(findTrees(slope[0], slope[1]))

print(math.prod(treeList))
from collections import defaultdict
from copy import deepcopy

f = open("day5.txt")

rules, updates = f.read().split("\n\n")

adjList = defaultdict(list)

for rule in rules.split():
    a, b = rule.split("|")
    adjList[b].append(a)

def part1():
    middleSum = 0
    for update in updates.split():
        correct = True
        update = update.split(",")
        for i in range(len(update)):
            for j in range(i):
                if update[i] in adjList[update[j]]:
                    correct = False
        if correct:
            middleSum += int(update[len(update) // 2])
    print(middleSum)

def part2():
    middleSum = 0
    for update in updates.split():
        correct = True
        update = update.split(",")
        for i in range(len(update)):
            for j in range(i):
                if update[i] in adjList[update[j]]:
                    correct = False
        if not correct:
            adjL = deepcopy(adjList)
            for n in list(adjL):
                if n not in update:
                    del adjL[n]
                else:
                    for x in list(adjL[n]):
                        if x not in update:
                            adjL[n].remove(x)
    
            middleSum += int(sorted(adjL, key= lambda x: len(adjL[x]))[len(update) // 2])
    print(middleSum)

part1()
part2()
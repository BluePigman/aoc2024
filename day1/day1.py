from collections import Counter

f = open("input.txt")

list1, list2 = [], []

for line in f:
    a, b = line.split()
    list1.append(int(a))
    list2.append(int(b))

list1.sort()
list2.sort()

def part1():
    totalDist = 0
    for i in range(len(list1)):
        totalDist += abs(list1[i] - list2[i])
    print(totalDist)

def part2():
    freq = Counter(list2)
    ss = 0
    for num in list1:
        ss += (num * freq[num])
    print(ss)

part1()
part2()
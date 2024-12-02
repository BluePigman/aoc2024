f = open("day2.txt")

reports = [list(map(int, line.split())) for line in f]

def isSafe(r:list[int]):
    if r[0] > r[1]:
        r.reverse()
    for i in range(1,len(r)):
        if r[i] <= r[i - 1] or r[i] > r[i - 1] + 3:
            return False
    return True

def part1():
    safeReports = 0
    for report in reports:
        if isSafe(report):
            safeReports += 1
    print(safeReports)

def canDampen(r:list[int]):
    for i in range(len(r)):
        x = list(r)
        x.pop(i)
        if isSafe(x):
            return True
    return False
     
def part2():
    safeReports = 0
    for report in reports:
        if isSafe(report):
            safeReports += 1
        elif canDampen(report):
            safeReports += 1
    print(safeReports)

part1()
part2()
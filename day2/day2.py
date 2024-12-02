f = open("day2.txt")

def isSafe(r:list[int]):
    if r[0] > r[1]:
        r.reverse()
    for i in range(1,len(r)):
        if r[i] <= r[i - 1] or r[i] > r[i - 1] + 3:
            return False
    return True

def part1():
    safeReports = 0
    for line in f:
        report = list(map(int, line.split()))
        if isSafe(report):
            safeReports += 1
    print(safeReports)

def canDampen(r:list[int]):
    for i in range(len(r)):
        x = list(r)
        isPossible = True
        x.pop(i)
        if x[0] > x[1]:
            x.reverse()
        for j in range(1,len(x)):
            if x[j] <= x[j - 1] or x[j] > x[j - 1] + 3:
                isPossible = False
        if isPossible:
            return True
    return False
     
def part2():
    safeReports = 0
    for line in f:
        report = list(map(int, line.split()))
        if isSafe(report):
            safeReports += 1
        elif canDampen(report):
            safeReports += 1
    print(safeReports)

part1()
f.seek(0) # start from beginning of file
part2()
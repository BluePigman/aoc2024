from collections import defaultdict

f = open("day4.txt")
wordSearch = [line.rstrip() for line in f.readlines()]

grid = defaultdict(lambda: ".")

M = len(wordSearch)
N = len(wordSearch[0])

for i in range(M):
    for j in range(N):
        grid[(i,j)] = wordSearch[i][j]

def part1():
    def search(r, c):
        count = 0

        delta = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
        for d in delta:
            word = ""
            for i in range(4):
                word += grid[(r + d[0] * i, c + d[1] * i)]
            if word == "XMAS":
                count += 1

        return count

    total = 0
    for r in range(M):
        for c in range(N):
            total += search(r, c)

    print(total)

def part2():
    def search(r, c):
        l1 = grid[(r - 1, c - 1)] + grid[(r, c)] + grid[(r + 1, c + 1)]
        l2 = grid[(r + 1, c - 1)] + grid[(r, c)] + grid[(r - 1, c + 1)]

        mas = ["MAS", "SAM"]
        if l1 in mas and l2 in mas:
            return 1
        return 0

    total = 0
    for r in range(M):
        for c in range(N):
            total += search(r, c)
    print(total)

part1()
part2()
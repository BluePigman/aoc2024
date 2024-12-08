import re
f = open("day7.txt")

equations = [line.rstrip() for line in f.readlines()]
def part1():
    # brute force: try all combinations of adding/multipling  
    def canCreate(target, curr, nums, i):
        if i == len(nums) - 1:
            return curr == target
        return canCreate(target, curr + nums[i + 1], nums, i + 1) or canCreate(target, curr * nums[i + 1], nums, i + 1)

    total = 0
    for eq in equations:
        nums = re.findall(r"\d+", eq) # regex to find all numbers
        testVal = int(nums[0])
        nums = [int(x) for x in nums[1:]]

        if canCreate(testVal, nums[0], nums, 0):
            total += testVal

    print(total)

part1()

def part2():
    def canCreate(target, curr, nums, i):
        if i == len(nums) - 1:
            return curr == target
        return canCreate(target, curr + nums[i + 1], nums, i + 1) or canCreate(target, curr * nums[i + 1], nums, i + 1) \
        or canCreate(target, int(str(curr) + str(nums[i + 1])), nums, i + 1) # new operator (concatenate numbers together)

    total = 0
    for eq in equations:
        nums = re.findall(r"\d+", eq)
        testVal = int(nums[0])
        nums = [int(x) for x in nums[1:]]

        if canCreate(testVal, nums[0], nums, 0):
            total += testVal

    print(total)
part2()
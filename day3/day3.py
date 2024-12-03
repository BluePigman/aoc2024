import re

f = open("day3.txt")
memory = f.read()

r = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
ops = r.findall(memory)

def multiply(x:str):
    x = x.replace("mul", "")
    x = x.replace("(", "")
    x = x.replace(")", "")
    a, b = map(int, x.split(","))
    return a * b

def part1():
    total = 0 
    for o in ops:
        total += multiply(o)
    print(total)

part1()

def part2():
    disabled = False
    total = 0
    for o in ops:
        if o == "don't()":
            disabled = True
            continue
        elif o == "do()":
            disabled = False
            continue
        if not disabled:
            total += multiply(o)
    print(total)

r = re.compile(r"mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)")
ops = r.findall(memory)

part2()
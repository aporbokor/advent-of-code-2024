import re

inp = open(0).read()


def p1():
    total = 0
    for x in re.findall(r"mul\(\d{1,3},\d{1,3}\)", inp):
        a, b = x.split(",")
        total += int(a[4:]) * int(b[:-1])
    print(total)


total = 0
ok = True
for x in re.findall(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))", inp):
    if ok and x[0] == "m":
        a, b = map(int, x[4:-1].split(","))
        total += a * b
    if x == "don't()":
        ok = False
    if x == "do()":
        ok = True
print(total)

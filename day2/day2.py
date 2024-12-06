def safe(levels):
    diffs = list(abs(int(a) - int(b)) for a, b in zip(levels[1:], levels))
    return (
        (levels == sorted(levels) or levels == sorted(levels, reverse=True))
        and max(diffs) <= 3
        and min(diffs) >= 1
    )


def damp(levels):
    if safe(levels):
        return 1
    for i in range(len(levels)):
        if safe(levels[:i] + levels[i + 1 :]):
            return 1
    return 0


def p2():
    total = 0
    for line in open(0).read().splitlines():
        total += damp(list(map(int, line.split())))
    print(total)


def p1():
    total = 0
    for line in open(0).read().splitlines():
        total += safe(list(map(int, line.split())))
    print(total)

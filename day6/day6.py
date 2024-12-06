import sys
import copy

sys.setrecursionlimit(10000000)  # lol


def p1():
    grid = [list(line) for line in open(0).read().splitlines()]
    seen = []
    pr, pc = 0, 0
    for r in range(len(grid)):
        found = False
        for c in range(len(grid[r])):
            if grid[r][c] == "^":
                pr, pc = r, c
                found = True
                break
        if found:
            break

    def sim(pr, pc, dr, dc):
        # check if going out of bounds
        seen.append((pr, pc))
        if (
            (pr == 0 and dr == -1)
            or (pr == len(grid) - 1 and dr == 1)
            or (pc == 0 and dc == -1)
            or (pc == len(grid[0]) - 1 and dc == 1)
        ):
            return
        if grid[pr + dr][pc + dc] == "#":
            # try all rotations
            dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            i = dirs.index((dr, dc))
            if i == len(dirs) - 1:
                i = 0
            else:
                i += 1
            dr, dc = dirs[i]
            return sim(pr, pc, dr, dc)
        else:
            return sim(pr + dr, pc + dc, dr, dc)

    sim(pr, pc, -1, 0)
    print(len(set(seen)))


grid = [list(line) for line in open(0).read().splitlines()]
seen = set()
pr, pc = 0, 0
for r in range(len(grid)):
    found = False
    for c in range(len(grid[r])):
        if grid[r][c] == "^":
            pr, pc = r, c
            found = True
            break
    if found:
        break


def sim(pr, pc, dr, dc):
    # check if going out of bounds
    seen.add((pr, pc))
    if (
        (pr == 0 and dr == -1)
        or (pr == len(grid) - 1 and dr == 1)
        or (pc == 0 and dc == -1)
        or (pc == len(grid[0]) - 1 and dc == 1)
    ):
        return
    if grid[pr + dr][pc + dc] == "#":
        # try all rotations
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        i = dirs.index((dr, dc))
        if i == len(dirs) - 1:
            i = 0
        else:
            i += 1
        dr, dc = dirs[i]
        return sim(pr, pc, dr, dc)
    else:
        return sim(pr + dr, pc + dc, dr, dc)


def loop(pr, pc, dr, dc, cache, grid):
    if dr == 0:
        grid[pr][pc] = "-"
    if dr == 1:
        grid[pr][pc] = "|"
    # check if going out of bounds
    if (
        (pr == 0 and dr == -1)
        or (pr == len(grid) - 1 and dr == 1)
        or (pc == 0 and dc == -1)
        or (pc == len(grid[0]) - 1 and dc == 1)
    ):
        return 0
    if grid[pr + dr][pc + dc] == "#":
        if (pr, pc, dr, dc) in cache:
            return 1
        cache.add((pr, pc, dr, dc))
        # print(cache)
        # try all rotations
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        i = dirs.index((dr, dc))
        if i == len(dirs) - 1:
            i = 0
        else:
            i += 1
        dr, dc = dirs[i]
        return loop(pr, pc, dr, dc, cache, grid)
    else:
        return loop(pr + dr, pc + dc, dr, dc, cache, grid)


total = 0
sim(pr, pc, -1, 0)
for rs, cs in seen:
    mgrid = copy.deepcopy(grid)
    mgrid[rs][cs] = "#"
    total += loop(pr, pc, -1, 0, set(), mgrid)
print(total)

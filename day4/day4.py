grid = [line for line in open(0).read().splitlines()]


def p1():
    total = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "X":
                # check straight
                if r >= 3:
                    total += grid[r - 1][c] + grid[r - 2][c] + grid[r - 3][c] == "MAS"
                if r <= len(grid) - 4:
                    total += grid[r + 1][c] + grid[r + 2][c] + grid[r + 3][c] == "MAS"
                if c >= 3:
                    total += grid[r][c - 1] + grid[r][c - 2] + grid[r][c - 3] == "MAS"
                if c <= len(grid[r]) - 4:
                    total += grid[r][c + 1] + grid[r][c + 2] + grid[r][c + 3] == "MAS"
                # check diagonal
                if r >= 3 and c >= 3:
                    total += (
                        grid[r - 1][c - 1] + grid[r - 2][c - 2] + grid[r - 3][c - 3]
                        == "MAS"
                    )
                if r >= 3 and c <= len(grid[r]) - 4:
                    total += (
                        grid[r - 1][c + 1] + grid[r - 2][c + 2] + grid[r - 3][c + 3]
                        == "MAS"
                    )
                if r <= len(grid) - 4 and c >= 3:
                    total += (
                        grid[r + 1][c - 1] + grid[r + 2][c - 2] + grid[r + 3][c - 3]
                        == "MAS"
                    )
                if r <= len(grid) - 4 and c <= len(grid[r]) - 4:
                    total += (
                        grid[r + 1][c + 1] + grid[r + 2][c + 2] + grid[r + 3][c + 3]
                        == "MAS"
                    )
    print(total)


total = 0

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == "A":
            if 1 <= r <= len(grid) - 2 and 1 <= c <= len(grid[r]) - 2:
                s1 = grid[r - 1][c - 1] + grid[r + 1][c + 1]
                s2 = grid[r + 1][c - 1] + grid[r - 1][c + 1]
                if "M" in s1 and "M" in s2 and "S" in s1 and "S" in s2:
                    total += 1
print(total)

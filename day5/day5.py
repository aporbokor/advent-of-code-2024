import functools

rules, updates = open(0).read().split("\n\n")


def p1():
    # create a dict
    order = {}
    for rule in rules.split():
        l, r = rule.split("|")
        if l not in order:
            order[l] = [r]
        else:
            order[l].append(r)

    def check(update: list[str]):
        seen = []
        for page in update:
            if page in seen:
                return 0
            for x in seen:
                if page not in order:
                    continue
                if x in order[page]:
                    return 0
            seen.append(page)
        return 1

    total = 0
    for update in updates.strip().split("\n"):
        update = update.split(",")
        if check(update):
            total += int(update[len(update) // 2])
    print(total)


# create a dict
order = {}
for rule in rules.split():
    l, r = rule.split("|")
    if l not in order:
        order[l] = [r]
    else:
        order[l].append(r)


def check(update: list[str]):
    seen = []
    for page in update:
        if page in seen:
            return 0
        for x in seen:
            if page not in order:
                continue
            if x in order[page]:
                return 0
        seen.append(page)
    return 1


@functools.lru_cache(maxsize=None)
def fix(update):
    seen = []
    update = update.split(",")
    for i, page in enumerate(update):
        for j, x in enumerate(seen):
            if page not in order:
                continue
            if x in order[page]:
                update[i], update[j] = update[j], update[i]
                return fix(",".join(update))
        seen.append(page)
    return update


total = 0
for update in updates.strip().split("\n"):
    # update = update.split(",")
    if not check(update.split(",")):
        res = fix(update)
        total += int(res[len(res) // 2])
print(total)

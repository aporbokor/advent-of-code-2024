l1 = []
l2 = []
for line in open(0):
    l1.append(int(line.split()[0]))
    l2.append(int(line.split()[1]))
print(l1, l2)
l1.sort()
l2.sort()
print(sum(x * l2.count(x) for x in l1))

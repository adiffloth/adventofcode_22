cals = 0
elves = []

for line in open('day01/1.in').read().splitlines():
    if line:
        cals += int(line)
    else:
        elves.append(cals)
        cals = 0

elves.append(cals)  # Don't forget the last one

elves.sort(reverse=True)
print(sum(elves[:3]))

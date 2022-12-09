cals = 0
elves = []

for line in open('day01/1.in').read().splitlines():
    if line:
        cals += int(line)
    else:
        elves.append(cals)
        cals = 0

elves.append(cals)  # Don't forget the last one

print(f'{max(elves)}')

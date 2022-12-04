cals = 0
elves = []

for n in open('day01/1.in').read().splitlines():
    if n:
        cals += int(n)
    else:
        elves.append(cals)
        cals = 0
elves.append(cals)  # Don't forget the last one
elves.sort(reverse=True)

p1 = elves[0]
p2 = sum(elves[:3])

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

assert p1 == 69626
assert p1 == max(elves)
assert p2 == 206780
print('Tests passed.')

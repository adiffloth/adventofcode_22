lines = open('day04/1.in').read().splitlines()

part_1 = part_2 = 0
for line in lines:
    a, b = [list(map(int, x.split('-'))) for x in line.split(',')]
    part_1 += ((a[0] <= b[0]) and (a[1] >= b[1])) or ((a[0] >= b[0]) and (a[1] <= b[1]))
    part_2 += ((a[0] <= b[0]) and (a[1] >= b[0])) or ((a[0] >= b[0]) and (a[0] <= b[1]))

print(f'{part_1 = }')
assert part_1 == 424
print(f'{part_2 = }')
assert part_2 == 804
print('Tests passed.')

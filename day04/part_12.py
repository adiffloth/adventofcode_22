lines = [x for x in open('day04/1.in').read().splitlines()]

part_1 = 0
part_2 = 0
for line in lines:
    a, b = [x.split('-') for x in line.split(',')]
    a_set = set(range(int(a[0]), int(a[1]) + 1))
    b_set = set(range(int(b[0]), int(b[1]) + 1))
    part_1 += a_set.issubset(b_set) or b_set.issubset(a_set)
    part_2 += len(a_set.intersection(b_set)) > 0

print(f'{part_1 = }')
assert part_1 == 424
print(f'{part_2 = }')
assert part_2 == 804
print('Tests passed.')

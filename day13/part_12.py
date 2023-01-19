from functools import cmp_to_key


def compare_ints(left, right):
    return (left < right) - (left > right)  # -1, 0, 1


def compare_lists(left, right):
    for pair in zip(left, right):
        if (res := compare(*pair)) != 0:
            return res
    return compare_ints(len(left), len(right))


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return compare_ints(left, right)
    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]
    return compare_lists(left, right)


pairs = [p.splitlines() for p in open('day13/1.in').read().split('\n\n')]
pairs = [list(map(eval, p)) for p in pairs]

part_1 = 0
for i, pair in enumerate(pairs):
    if compare(*pair) == 1:  # correct order
        part_1 += i + 1  # 1 indexed
print(f'{part_1 = }')

items = [item for pair in pairs for item in pair]
items.extend([[[2]], [[6]]])  # divider packets
items.sort(key=cmp_to_key(compare), reverse=True)

part_2 = (items.index([[2]]) + 1) * (items.index([[6]]) + 1)  # 1 indexed
print(f'{part_2 = }')

assert part_1 == 5843
assert part_2 == 26289
print('Tests passed.')

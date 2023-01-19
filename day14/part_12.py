from collections import namedtuple
Rock = namedtuple('Rock', ['x', 'y'])


def get_rocks(lines):
    rocks = set()
    for line in lines[:]:
        rock_path = [Rock(*map(int, p.split(','))) for p in line.split(' -> ')]
        for start, end in zip(rock_path, rock_path[1:]):
            for x in range(min(start.x, end.x), max(start.x, end.x) + 1):
                rocks.add(Rock(x, start.y))
            for y in range(min(start.y, end.y), max(start.y, end.y) + 1):
                rocks.add(Rock(start.x, y))
    return rocks


def check_part_1(rocks, cur_pos, max_y):
    return cur_pos.y > max_y


def check_part_2(rocks, cur_pos, max_y):
    return Rock(500, 0) in rocks


def run(rocks, check_fn):
    max_y = max(r.y for r in rocks)
    sand_units = 0
    while True:
        cur_pos = Rock(500, 0)  # Given starting position
        while True:
            if check_fn(rocks, cur_pos, max_y):
                return sand_units
            if Rock(cur_pos.x, cur_pos.y + 1) not in rocks:
                cur_pos = Rock(cur_pos.x, cur_pos.y + 1)
            elif Rock(cur_pos.x - 1, cur_pos.y + 1) not in rocks:
                cur_pos = Rock(cur_pos.x - 1, cur_pos.y + 1)
            elif Rock(cur_pos.x + 1, cur_pos.y + 1) not in rocks:
                cur_pos = Rock(cur_pos.x + 1, cur_pos.y + 1)
            else:
                rocks.add(Rock(*cur_pos))
                break  # On the the next unit of sand

        sand_units += 1


lines = open('day14/1.in').read().splitlines()

part_1 = run(get_rocks(lines), check_part_1)
print(f'Part 1: {part_1}')
assert part_1 == 793

part_2_rocks = get_rocks(lines)
max_y = max(r.y for r in part_2_rocks)
for x in range(500 - max_y - 10, 500 + max_y + 10):
    part_2_rocks.add(Rock(x, max_y + 2))  # Set the floor a little wider than right triangle
part_2 = run(part_2_rocks, check_part_2)
print(f'Part 2: {part_2}')
assert part_2 == 24166

print('Tests passed')

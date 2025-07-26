from itertools import cycle
from math import inf
from collections import defaultdict
from sys import exit

jets = cycle([i for i in open('day17/00.in').read()])
# rocks = cycle(enumerate([[120], [32, 112, 32], [112, 16, 16], [64, 64, 64, 64], [96, 96]]))
rock_list = [
    [(0, 2), (0, 3), (0, 4), (0, 5)],  # -
    [(0, 3), (1, 2), (1, 3), (1, 4), (2, 3)],  # +
    [(0, 2), (0, 3), (0, 4), (1, 4), (2, 4)],  # L
    [(0, 2), (1, 2), (2, 2), (3, 2)],  # |
    [(0, 2), (0, 3), (1, 2), (1, 3)]  # square
]
rocks = cycle(rock_list)


def collision_floor(floor, rock):
    lowest_el = inf
    for el in rock:
        if (el in floor) or (el[0] < 0):
            return True
    return False
    # return any(el in floor for el in rock)


def collision_wall(floor, rock):
    for el in rock:
        if not (0 <= el[1] <= 6):
            return True
        if el in floor:
            return True
    return False


def rock_jet(floor, rock, jet):
    new_rock = []
    direction = 1 if jet == '>' else -1
    for el in rock:
        new_rock.append((el[0], el[1] + direction))
    return rock if collision_wall(floor, new_rock) else new_rock


def rock_fall(floor, rock):
    new_rock = []
    for el in rock:
        new_rock.append((el[0] - 1, el[1]))
    return (rock, True) if collision_floor(floor, new_rock) else (new_rock, False)


def print_vis(floor):
    floor_dict = defaultdict(list)
    for el in floor:
        floor_dict[el[0]].append(el[1])

    prev_row = max(floor_dict)
    for row in sorted(floor_dict.items(), reverse=True):
        for i in range(prev_row -1, row[0], -1):
            print(f'{i:4} - .......')
        print(f'{row[0]:4} - ', end='')
        
        for col in range(7):
            if col in row[1]:
                print('#', end='')
            else:
                print('.', end='')
        prev_row = row[0]
        print()


def update_floor(floor, rock):
    new_floor = []
    max_floor_height = 0
    for col in range(7):
        rock_height = 0
        for el in rock:
            if el[1] == col:
                rock_height = max(rock_height, el[0])
        max_col_height = max(floor[col][0], rock_height)
        new_floor.append((max_col_height, col))
        max_floor_height = max(max_floor_height, max_col_height)
    return new_floor, max_floor_height


def init_rock(max_floor_height, rock):
    new_rock = []
    for el in rock:
        new_rock.append((el[0] + max_floor_height + 4, el[1]))
    return new_rock


def drop_piece(floor, rock):
    blocked = False
    while not blocked:
        # step += 1
        # print_vis(rock)
        jet = next(jets)
        rock = rock_jet(floor, rock, jet)  # Jet movement
        rock, blocked = rock_fall(floor, rock)  # Gravity movement
        if blocked:
            # print('blocked')
            pass
        # print(step, jet, rock)
        # floor = update_floor(floor, rock)
    return floor, rock

if False:
    step = 0
    floor = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]
    max_floor_height = 0
    # rock = [(6, 0), (6, 1), (6, 2), (6, 3)]
    # rock = [(6, 0), (6, 1), (7, 0), (7, 1)]
    rock = [(6, 0), (6, 1), (6, 2), (6, 3)]
    # print(f'0   {rock}')

    print(f'{step=}')
    floor, rock = drop_piece(floor, rock)

    print()
    print_vis(rock)
    print_vis(floor)
    print()
    floor, max_floor_height = update_floor(floor, rock)
    print_vis(floor)
    print(f'{max_floor_height=}')

    step += 1
    print(f'{step=}')
    rock = [(8, 1), (7, 0), (7, 1), (7, 2), (6, 1)]
    floor, rock = drop_piece(floor, rock)

    print_vis(rock)
    print_vis(floor)
    print()
    floor, max_floor_height = update_floor(floor, rock)
    print_vis(floor)
    print(f'{max_floor_height=}')

    print(floor)
    print('end')


# exit()
floor = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]
max_floor_height = 0
for step in range(3):
    if step%50 == 0:
        print(step, max_floor_height)
    # print(f'{step=}')
    rock = init_rock(max_floor_height, next(rocks))
    # print_vis(rock)
    # print()
    floor, rock = drop_piece(floor, rock)
    # print_vis(rock)
    # print_vis(floor)
    # print()
    floor, max_floor_height = update_floor(floor, rock)
    # print_vis(floor)
    # print()
print_vis(floor)
print(max_floor_height)

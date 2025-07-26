from itertools import cycle
jets = cycle([i for i in open('day17/00.in').read()])
# rocks = cycle(enumerate([[120], [32, 112, 32], [112, 16, 16], [64, 64, 64, 64], [96, 96]]))
rock_list = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
    [(0, 2), (1, 2), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (1, 0), (1, 1)]
]
rocks = cycle(rock_list)


def collision(floor, rock):
    return any(el in floor for el in rock)


def rock_jet(rock, jet):
    new_rock = []
    direction = 1 if jet == '>' else -1
    for el in rock:
        new_rock.append((el[0], el[1] + direction))
    return new_rock


def rock_fall(rock):
    new_rock = []
    for el in rock:
        new_rock.append((el[0] - 1, el[1]))
    return new_rock


step = 0
floor = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]
rock = [(6, 0), (6, 1), (6, 2), (6, 3)]
print(f'0   {rock}')
while True:
    step += 1
    jet = next(jets)
    rock = rock_jet(rock, jet)
    if collision(floor, rock):
        print(step, jet, rock)
        print('break: jet')
        break
    rock = rock_fall(rock)
    if collision(floor, rock):
        print(step, jet, rock)
        print('break: fall')
        break
    print(step, jet, rock)

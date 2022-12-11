from math import dist, sqrt


def move(knot, direction):
    return tuple([sum(x) for x in zip(knot, d[direction])])


def move_tail(head, tail):  # Diagonal movement is allowed
    if dist(head, tail) > sqrt(2):  # The two knots are not touching
        if head[0] > tail[0]:
            tail = move(tail, 'R')
        elif head[0] < tail[0]:
            tail = move(tail, 'L')
        if head[1] > tail[1]:
            tail = move(tail, 'U')
        elif head[1] < tail[1]:
            tail = move(tail, 'D')
    return tail


def step(knots, direction):
    if len(knots) == 1:  # Base case: we're at the head knot
        head = knots.pop()
        return [move(head, direction)]

    # Recursive case: we're on a body or tail knot
    curr_knot = knots.pop()
    knots = step(knots, direction)
    curr_knot = move_tail(knots[-1], curr_knot)
    knots.append(curr_knot)
    return(knots)


def solve(lines, knots):
    tail_locs = set()
    for line in lines:
        direction, num_steps = line.split()
        for _ in range(int(num_steps)):
            knots = step(knots, direction)
            tail_locs.add(knots[-1])
    return len(tail_locs)


lines = open('day09/1.in').read().splitlines()
d = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

part_1 = solve(lines, [(0, 0)] * 2)
print(part_1)
assert part_1 == 6081

part_2 = solve(lines, [(0, 0)] * 10)
print(part_2)
assert part_2 == 2487

print('Tests passed.')

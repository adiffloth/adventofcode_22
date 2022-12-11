from math import dist, sqrt


def move(knot, direction):
    return tuple([sum(x) for x in zip(knot, d[direction])])


def move_tail(head, tail):
    if dist(head, tail) > sqrt(2):  # The two knots are not touching.
        if head[0] > tail[0]:
            tail = move(tail, 'R')
        elif head[0] < tail[0]:
            tail = move(tail, 'L')
        if head[1] > tail[1]:
            tail = move(tail, 'U')
        elif head[1] < tail[1]:
            tail = move(tail, 'D')
    return tail


lines = [x for x in open('day09/1.in').read().splitlines()]
d = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
head = (0, 0)
tail = (0, 0)
tail_locs = set()

for line in lines:
    direction, steps = line.split()
    for _ in range(int(steps)):
        head = move(head, direction)
        tail = move_tail(head, tail)
        tail_locs.add(tail)

print(len(tail_locs))
assert len(tail_locs) == 6081
print('Tests passed.')

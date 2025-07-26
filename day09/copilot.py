lines = open('day09/1.in').read().splitlines()

def move(knot, direction):
    return tuple([sum(x) for x in zip(knot, d[direction])])

def move_tail(head, tail):
    
def draw_pixel(cycle, register):
    if abs(cycle - register) <= 1:
        print('\u2588', end='')
    else:
        print(' ', end='')


def tick(cycle):
    cycle += 1
    if cycle % 40 == 0:
        print('\n', end='')
        cycle = 0
    return cycle


lines = open('day10/1.in').read().splitlines()
cycle = 0
register = 1

for line in lines:
    draw_pixel(cycle, register)

    if line == 'noop':
        cycle = tick(cycle)

    else:
        cycle = tick(cycle)
        draw_pixel(cycle, register)
        cycle = tick(cycle)
        register += int(line.split()[1])

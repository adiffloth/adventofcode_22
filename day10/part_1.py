def check():
    if (cycle == 20) or (((cycle - 20) % 40) == 0):
        signal_strengths.append(cycle * reg)


lines = open('day10/1.in').read().splitlines()
cycle = 1
reg = 1
signal_strengths = []

for line in lines:
    check()
    if line == 'noop':
        cycle += 1
    else:
        cycle += 1
        check()
        cycle += 1
        reg += int(line.split()[1])

part_1 = sum(signal_strengths)
print(f'{part_1 = }')
assert part_1 == 14220
print('Tests passed.')

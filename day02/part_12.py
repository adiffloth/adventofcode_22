lines = [x for x in open('day02/1.in').read().splitlines()]

op_plays = 'ABC'
my_plays = 'XYZ'
p1_score = 0
for line in lines:
    op_idx = op_plays.index(line[0])
    my_idx = my_plays.index(line[-1])
    p1_score += ((my_idx - op_idx + 1) % 3) * 3 + my_idx + 1

# X: lose,  +2 positions
# Y: draw,  +0 positions
# Z: wins,  +1 positions
outcomes = 'YZX'
p2_score = 0
for line in lines:
    op_idx = op_plays.index(line[0])
    my_idx = (op_idx + outcomes.index(line[-1])) % 3  # Shift my play according to outcome
    p2_score += ((my_idx - op_idx + 1) % 3) * 3 + my_idx + 1

print(f'Part 1: {p1_score}')
assert p1_score == 15632
print(f'Part 2: {p2_score}')
assert p2_score == 14416
print('Tests passed')

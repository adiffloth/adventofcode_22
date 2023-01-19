lines = open('day02/1.in').read().splitlines()

op_plays = 'ABC'
my_plays = 'XYZ'
total_score = 0
for line in lines:
    op_idx = op_plays.index(line[0])
    my_idx = my_plays.index(line[-1])
    total_score += ((my_idx - op_idx + 1) % 3) * 3 + (my_idx + 1)

print(f'{total_score = }')

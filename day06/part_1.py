line = open('day06/1.in').read()


def solve(line, substr_len):
    for i in range(substr_len, len(line)):
        if len(set(line[i-substr_len:i])) >= substr_len:
            return i


print(part_1_ans := solve(line, 4))
assert part_1_ans == 1343

print(part_2_ans := solve(line, 14))
assert part_2_ans == 2193
print('All tests passed')

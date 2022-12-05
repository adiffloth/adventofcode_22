def find_stack_shape(lines):
    max_init_height = int(lines.index('')) - 1
    num_stacks = max(map(int, lines[max_init_height].split()))
    return max_init_height, num_stacks


def get_init_stacks(lines, max_init_height, num_stacks):
    stacks = []
    for _ in range(num_stacks):
        stacks.append([])

    for line in lines[max_init_height - 1::-1]:
        for i in range(num_stacks):
            char = line[(i * 4) + 3]
            if char != ' ':
                stacks[i].append(char)
    return stacks


def parse_instructions(line):
    line_data = line.split()
    boxes_to_move = int(line_data[1])
    source_stack = int(line_data[3]) - 1
    dest_stack = int(line_data[5]) - 1
    return boxes_to_move, source_stack, dest_stack


def get_top_crates(stacks):
    top_crates = []
    for stack in stacks:
        top_crates.append(stack[-1])
    return f'{"".join(top_crates)}'


def part_1(lines, max_init_height, num_stacks):
    stacks = get_init_stacks(lines, max_init_height, num_stacks)
    for line in lines[max_init_height + 2:]:
        boxes_to_move, source_stack, dest_stack = parse_instructions(line)
        for i in range(boxes_to_move):
            stacks[dest_stack].append(stacks[source_stack].pop())
    return get_top_crates(stacks)


def part_2(lines, max_init_height, num_stacks):
    stacks = get_init_stacks(lines, max_init_height, num_stacks)
    for line in lines[max_init_height + 2:]:
        boxes_to_move, source_stack, dest_stack = parse_instructions(line)
        stacks[dest_stack].extend(stacks[source_stack][-boxes_to_move:])
        stacks[source_stack] = stacks[source_stack][:-boxes_to_move]
    return get_top_crates(stacks)


lines = [x for x in open('day05/1.in').read().splitlines()]
max_init_height, num_stacks = find_stack_shape(lines)

part_1_ans = part_1(lines, max_init_height, num_stacks)
print(f'{part_1_ans = }')
assert part_1_ans == 'SPFMVDTZT'

part_2_ans = part_2(lines, max_init_height, num_stacks)
print(f'{part_2_ans = }')
assert part_2_ans == 'ZFSJBPRFP'

print('Tests passed.')

from collections import defaultdict

lines = open('day07/00.in').read().splitlines()

pwd = ['/']
files = {}
for line in lines[1:]:
    if line == '$ cd ..':
        pwd.pop()
    elif line.startswith('$ cd'):
        pwd.append(line.split()[2] + '/')
    elif line[0].isnumeric():
        size, file_name = line.split()
        files[''.join(pwd + [file_name])] = int(size)

dirs = defaultdict(int)
for path, size in files.items():
    path_ls = path.split('/')[:-1]
    while path_ls:
        dirs['/'.join(path_ls)] += size
        path_ls.pop()

part_1 = sum([x for x in dirs.values() if x <= 100_000])
print(f'Part 1: {part_1}')
assert part_1 == 1490523

space_needed = 30000000 - (70000000 - dirs[''])
part_2 = min([x for x in dirs.values() if x >= space_needed])
print(f'Part 2: {part_2}')
assert part_2 == 12390492

print('Tests passed.')

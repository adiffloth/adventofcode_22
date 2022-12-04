lines = [x for x in open('day03/1.in').read().splitlines()]

priorities_1 = []
for line in lines:
    lt = line[:len(line)//2]
    rt = line[len(line)//2:]
    common = set(lt).intersection(set(rt)).pop()
    offset = 96 - common.isupper() * 58
    priorities_1.append(ord(common) - offset)

priorities_2 = []
for elf_1, elf_2, elf_3 in zip(*[iter(lines)] * 3):
    common = set(elf_1).intersection(set(elf_2), set(elf_3)).pop()
    offset = 96 - common.isupper() * 58
    priorities_2.append(ord(common) - offset)

part_1 = sum(priorities_1)
print(f'{part_1=}')
assert part_1 == 8053
part_2 = sum(priorities_2)
print(f'{part_2=}')
assert part_2 == 2425
print('Tests passed.')

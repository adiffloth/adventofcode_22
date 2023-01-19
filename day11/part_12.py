from collections import deque
import numpy as np


class Monkey:
    def __init__(self, raw_monkey):
        self.inspection_cnt = 0
        self.items = deque([int(x) for x in raw_monkey[1].split(': ')[1].split(',')])
        self.operation = raw_monkey[2].split('= ')[1]
        self.divisor = int(raw_monkey[3].split('by ')[1])
        self.if_true = int(raw_monkey[4].split()[-1])
        self.if_false = int(raw_monkey[5].split()[-1])

    def operate(self, old):
        return eval(self.operation)

    def test(self, item):
        return self.if_true if item % self.divisor == 0 else self.if_false

    def inspect_all(self, lcm, worry_reducer=3):
        while self.items:
            self.inspection_cnt += 1
            item = self.operate(self.items.popleft()) // worry_reducer
            item = item % lcm
            target = self.test(item)
            monkeys[target].items.append(item)


def solve(rounds, worry_reducer):
    for r in range(rounds):
        for monkey in monkeys:
            monkey.inspect_all(lcm, worry_reducer)
    return np.prod(sorted([m.inspection_cnt for m in monkeys])[-2:])


raw_monkeys = open('day11/1.in').read().split('\n\n')
monkeys = [Monkey(m.splitlines()) for m in raw_monkeys]
lcm = np.prod([m.divisor for m in monkeys])

part_1 = solve(rounds=20, worry_reducer=3)
print(f'{part_1 = }')
assert part_1 == 54036

monkeys = [Monkey(m.splitlines()) for m in raw_monkeys]
part_2 = solve(rounds=10_000, worry_reducer=1)
print(f'{part_2 = }')
assert part_2 == 13237873355

print('Tests passed.')

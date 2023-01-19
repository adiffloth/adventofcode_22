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

    def inspect_all(self):
        while self.items:
            self.inspection_cnt += 1
            item = self.operate(self.items.popleft())
            item = item % lcm
            target = self.test(item)
            monkeys[target].items.append(item)


raw_monkeys = open('day11/1.in').read().split('\n\n')
monkeys = [Monkey(m.splitlines()) for m in raw_monkeys]
lcm = np.prod([m.divisor for m in monkeys])

for r in range(10000):
    for monkey in monkeys:
        monkey.inspect_all()

part_2 = np.prod(sorted([m.inspection_cnt for m in monkeys])[-2:])
print(f'{part_2 = }')
assert part_2 == 13237873355
print('Tests passed.')

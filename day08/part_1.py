def is_visible(y, x):
    height = forest[y][x]
    lt = max(forest[y][:x]) < height
    rt = max(forest[y][x + 1:]) < height
    up = max([line[x] for line in forest[:y]]) < height
    dn = max([line[x] for line in forest[y + 1:]]) < height
    return lt or rt or up or dn


def scenic_score(y, x):
    sight_dist_product = 1
    up = [line[x] for line in forest[:y]][::-1]
    lt = forest[y][:x][::-1]
    rt = forest[y][x + 1:]
    dn = [line[x] for line in forest[y + 1:]]
    for sight_line in [up, lt, rt, dn]:
        sight_dist = 0
        for tree in sight_line:
            sight_dist += 1
            if tree >= forest[y][x]:
                break
        sight_dist_product *= sight_dist
    return sight_dist_product


forest = [list(map(int, [*x])) for x in open('day08/1.in', encoding='UTF8').read().splitlines()]

visible_cnt = len(forest) * 2 + (len(forest[0]) - 2) * 2  # Outer trees
max_scenic_score = 0
for j in range(1, len(forest) - 1):
    for i in range(1, len(forest[0]) - 1):
        visible_cnt += is_visible(j, i)
        max_scenic_score = max(max_scenic_score, scenic_score(j, i))
print(f'Part 1: {visible_cnt}')
assert visible_cnt == 1736

print(f'Part 2: {max_scenic_score}')
assert max_scenic_score == 268800

print('Tests passed.')

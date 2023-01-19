from collections import deque


def find_start(lines):
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == 'E':
                return (y, x)


def get_height(y, x):
    chr_height = lines[y][x]
    if lines[y][x] == 'S':
        chr_height = 'a'
    elif lines[y][x] == 'E':
        chr_height = 'z'
    return ord(chr_height)


def get_neighbors(y, x, y_dim, x_dim):
    deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    neighbs = []
    for d in deltas:
        if 0 <= y + d[0] <= y_dim and 0 <= x + d[1] <= x_dim:
            curr_height = get_height(y, x)
            neighb_height = get_height(y + d[0], x + d[1])
            if neighb_height >= curr_height - 1:  # Changed from part 1
                neighbs.append((y + d[0], x + d[1]))
    return neighbs


def bfs(start, goal_height):
    queue = deque([[start]])
    visited = set()
    while queue:
        path = queue.popleft()  # Next path to examine
        node = path[-1]  # Last node is the one to examine
        if get_height(node[0], node[1]) == goal_height:  # Changed from part 1
            return path
        if node not in visited:
            neighbors = get_neighbors(node[0], node[1], y_max, x_max)
            for neighbor in neighbors:
                queue.append(path + [neighbor])
            visited.add(node)
    return []  # No path found


lines = open('day12/1.in').read().splitlines()
start = find_start(lines)  # Start at the end now
goal_height = ord('a')  # Goal is to get to height a

y_max = len(lines) - 1
x_max = len(lines[0]) - 1

part_2 = len(bfs(start, goal_height)) - 1
print(f'{part_2 = }')
assert part_2 == 488
print('Tests passed.')

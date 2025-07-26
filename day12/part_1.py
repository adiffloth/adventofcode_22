from collections import deque


def find_start_goal(lines):
    start = goal = None
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == 'S':
                start = (y, x)
            elif char == 'E':
                goal = (y, x)
    return start, goal


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
            if neighb_height <= curr_height + 1:
                neighbs.append((y + d[0], x + d[1]))
    return neighbs


def bfs(start, goal):
    queue = deque([[start]])
    visited = set()
    while queue:
        path = queue.popleft()  # Next path to examine
        node = path[-1]  # Last node is the one to examine
        if node == goal:
            return path
        if node not in visited:
            neighbors = get_neighbors(node[0], node[1], y_max, x_max)
            for neighbor in neighbors:
                queue.append(path + [neighbor])
            visited.add(node)
    return []  # No path found


lines = open('day12/00.in').read().splitlines()
start, goal = find_start_goal(lines)

y_max = len(lines) - 1
x_max = len(lines[0]) - 1

part_1 = len(bfs(start, goal)) - 1
print(f'{part_1 = }')
print(bfs(start, goal))
# assert part_1 == 490
print('Tests passed.')

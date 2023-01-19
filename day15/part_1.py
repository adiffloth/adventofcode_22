from collections import namedtuple, defaultdict


def m_dist(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)


Point = namedtuple('Point', ['x', 'y'])
lines = open('day15/1.in').read().splitlines()

beacons = defaultdict(set)
isnts = set()
for line in lines:
    sensor = Point(int(line.split('x=')[1].split(',')[0]), int(line.split('y=')[1].split(':')[0]))
    beacon = Point(int(line.split('x=')[2].split(',')[0]), int(line.split('y=')[2]))

    beacons[beacon.y].add(beacon.x)
    d = m_dist(sensor, beacon)
    y = 2000000
    for x in range(sensor.x - d, sensor.x + d + 1):
        current = Point(x, y)
        if (m_dist(current, sensor) <= d) and (x not in beacons[y]):
            isnts.add(x)


part_1 = len(isnts)
print(f'{part_1 = }')
assert part_1 == 4502208
print('Tests passed.')

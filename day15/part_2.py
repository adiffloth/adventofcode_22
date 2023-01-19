from collections import namedtuple
import shapely.geometry as geom
import shapely.ops as ops


def m_dist(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)


def get_sensor_coverage(line):
    sensor = Point(int(line.split('x=')[1].split(',')[0]), int(line.split('y=')[1].split(':')[0]))
    beacon = Point(int(line.split('x=')[2].split(',')[0]), int(line.split('y=')[2]))
    d = m_dist(sensor, beacon)

    return geom.Polygon([(sensor.x, sensor.y + d),  # It's a diamond
                         (sensor.x - d, sensor.y),
                         (sensor.x, sensor.y - d),
                         (sensor.x + d, sensor.y)])


Point = namedtuple('Point', ['x', 'y'])
lines = open('day15/1.in').read().splitlines()
sensor_polys = []

for line in lines:
    sensor_polys.append(get_sensor_coverage(line))

total_coverage = ops.unary_union(sensor_polys)

interiors = ops.clip_by_rect(total_coverage,
                             0, 0, 4_000_000, 4_000_000
                             ).interiors

x, y = interiors[0].centroid.coords[0]
part_2 = int(x * 4_000_000 + y)

print(f'{part_2 = }')
assert part_2 == 13784551204480
print('Tests passed.')

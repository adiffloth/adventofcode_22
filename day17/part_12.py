import sys

jet_directions = list(open('day17/1.in').read().strip())
jet_directions = list(map(lambda _: -1 if _ == '<' else 1, jet_directions))

solid_squares = set([(x,0) for x in range(7)])

X_START_OFFSET = 2
Y_START_OFFSET = 4

def spawn_rock(tower_height, pattern):
  # bottom left coordinate
  x, y = (X_START_OFFSET, tower_height + Y_START_OFFSET)

  if pattern == 0:
    return set([
      (x, y),
      (x + 1, y),
      (x + 2, y),
      (x + 3, y)
    ])
  elif pattern == 1:
    return set([
      (x + 1, y),
      (x, y + 1),
      (x + 1, y + 1),
      (x + 2, y + 1),
      (x + 1, y + 2)
    ])
  elif pattern == 2:
    return set([
      (x, y),
      (x + 1, y),
      (x + 2, y),
      (x + 2, y + 1),
      (x + 2, y + 2)
    ])
  elif pattern == 3:
    return set([
      (x, y),
      (x, y + 1),
      (x, y + 2),
      (x, y + 3)
    ])
  elif pattern == 4:
    return set([
      (x, y),
      (x + 1, y),
      (x, y + 1),
      (x + 1, y + 1)
    ])

def should_fall(rock):
  for square in rock:
    x,y = square

    if (x, y - 1) in solid_squares:
      return False

  return True

def fall(rock):
  return set([(x, y - 1) for x,y in rock])

def should_push(rock, direction):
  for square in rock:
    x,y = square

    if direction == -1 and x - 1 < 0:
      return False
    
    if direction == 1 and x + 1 > 6:
      return False
    
    if (x + direction, y) in solid_squares:
      return False

  return True

def push(rock, direction):
  return set([(x + direction, y) for x,y in rock])

def come_to_rest(rock):
  max_y = 0

  for square in rock:
    _,y = square
    solid_squares.add(square)
    max_y = max(max_y, y)
  
  return (max_y, rock)

def visualization(max_y = 10, min_y = 0, rock = set()):
  s = ''

  for y in range(max_y, min_y, -1):
    s += f'{y:4} - '
    for x in range(0,7):
      s += '@' if (x,y) in rock else '#' if (x,y) in solid_squares else '.'
    s += '\n'

  return s

next_jet = 0
next_rock = 0
tower_height = 0
ROCKS_TO_FALL = 10

r = 0

while r < ROCKS_TO_FALL:
  rock = spawn_rock(tower_height, next_rock)

  while True:
    direction = jet_directions[next_jet]
    next_jet = (next_jet + 1) % len(jet_directions)

    if should_push(rock, direction):
      rock = push(rock, direction)

    if should_fall(rock):
      rock = fall(rock)
    else:
      break
  
  max_y, rock = come_to_rest(rock)
  tower_height = max(tower_height, max_y)
  next_rock = (next_rock + 1) % 5
  r += 1

print(visualization(20, 0, rock))
print(tower_height)
print(sum([(('XYZ'.index(line[-1]) - 'ABC'.index(line[0]) + 1) % 3) * 3 + ('XYZ'.index(line[-1]) + 1) for line in open('day02/1.in').read().splitlines()]))

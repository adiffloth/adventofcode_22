def is_straight(y):
    y = set(y)
    if y == set([1, 2, 3, 4, 5]) or y == set([2, 3, 4, 5, 6]):
        return True

    if y.intersection(set([1, 2, 3, 4])) == set([1, 2, 3, 4]):
        return True
    if y.intersection(set([2, 3, 4, 5])) == set([2, 3, 4, 5]):
        return True
    if y.intersection(set([3, 4, 5, 6])) == set([3, 4, 5, 6]):
        return True
    return False


y = [2, 3, 4]

count = 0
for i in range(1, 7):
    for j in range(1, 7):
        if is_straight(y + [i, j]):
            count += 1
            print(count, i, j, sorted(y + [i, j]))

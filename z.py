from itertools import combinations


def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

    # write your code here
    for a1 in dice1:
        for a2 in dice2:
            if a1 > a2:
                dice1_wins += 1
            elif a2 > a1:
                dice2_wins += 1

    return (dice1_wins, dice2_wins)


def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)

    # write your code here
    # use your implementation of count_wins method if necessary
    losers = set()
    pairs = combinations(range(0, len(dices)), 2)
    for d in pairs:
        compare = count_wins(dices[d[0]], dices[d[1]])
        if compare[0] > compare[1]:
            losers.add(d[1])
        elif compare[1] > compare[0]:
            losers.add(d[0])

    if len(losers) == len(dices):
        return -1
    else:
        for i in range(len(dices)):
            if i not in losers:
                return i


def return_winner(opp, dices):
    for idx, d2 in enumerate(dices):
        compare = count_wins(opp, d2)
        if compare[1] > compare[0]:
            return idx
    return -1


def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    strategy["choose_first"] = True
    strategy["first_dice"] = 0
    for i in range(len(dices)):
        strategy[i] = (i + 1) % len(dices)

    # write your code here
    best_dice = find_the_best_dice(dices)
    if best_dice != -1:
        strategy['first_dice'] = best_dice
    else:
        strategy['choose_first'] = False
        for i in range(len(dices)):
            strategy[i] = return_winner(dices[i], dices)

    return strategy


# print(count_wins([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]))
# print(count_wins([1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9]))

# print(find_the_best_dice([[1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9], [3, 3, 5, 5, 7, 7]]), '\n***\n')
# print(find_the_best_dice([[1, 1, 2, 4, 5, 7], [1, 2, 2, 3, 4, 7], [1, 2, 3, 4, 5, 6]]), '\n***\n')
# print(find_the_best_dice([[3, 3, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [4, 4, 4, 4, 0, 0], [5, 5, 5, 1, 1, 1]]), '\n***\n')

print(compute_strategy([[1,1,4,6,7,8], [2,2,2,6,7,7], [3,3,3,5,5,8]]))
print(compute_strategy([[4,4,4,4,0,0,], [7,7,3,3,3,3,], [6,6,2,2,2,2], [5,5,5,1,1,1]]))

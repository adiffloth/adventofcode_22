def find_max_calories(input_list):
    max_calories = 0
    max_elf = 0
    elf = 0
    for i, calories in enumerate(input_list):
        if calories == "":
            if max_calories < sum([int(x) for x in input_list[elf:i]]):
                max_calories = sum([int(x) for x in input_list[elf:i]])
                max_elf = elf
            elf = i + 1
    return max_calories, max_elf


# input_list = [1000, 2000, 3000, "", 4000, "", 5000, 6000, "", 7000, 8000, 9000, "", 10000]
input_list = [(x) for x in open('day01/1.in').read().splitlines()]
result = find_max_calories(input_list)
print("Elf carrying the most calories: Elf ", result[1] + 1)
print("Calories carried by that Elf: ", result[0])


def find_top_3_calories(input_list):
    max_calories = [0, 0, 0]
    max_elf = [0, 0, 0]
    elf = 0
    for i, calories in enumerate(input_list):
        if calories == "":
            current_calories = sum(input_list[elf:i])
            if current_calories > max_calories[0]:
                max_calories[2] = max_calories[1]
                max_calories[1] = max_calories[0]
                max_calories[0] = current_calories
                max_elf[2] = max_elf[1]
                max_elf[1] = max_elf[0]
                max_elf[0] = elf
            elif current_calories > max_calories[1]:
                max_calories[2] = max_calories[1]
                max_calories[1] = current_calories
                max_elf[2] = max_elf[1]
                max_elf[1] = elf
            elif current_calories > max_calories[2]:
                max_calories[2] = current_calories
                max_elf[2] = elf
            elf = i + 1
    return sum(max_calories), max_elf


input_list = [1000, 2000, 3000, "", 4000, "", 5000, 6000, "", 7000, 8000, 9000, "", 10000]
result = find_top_3_calories(input_list)
print("Total calories carried by the top three Elves: ", result[0])
print("Elves carrying the most calories: Elf ", [x + 1 for x in result[1]])


def find_top_3_calories(input_list):
    max_calories = []
    elf = 0
    for i, calories in enumerate(input_list):
        if calories == "":
            sum_calories = sum(input_list[elf:i])
            max_calories.append((sum_calories, elf))
            max_calories.sort(reverse=True)
            max_calories = max_calories[:3]
            elf = i + 1
    max_calories.sort(reverse=True)
    return sum(x[0] for x in max_calories), [x[1] for x in max_calories]


input_list = [1000, 2000, 3000, "", 4000, "", 5000, 6000, "", 7000, 8000, 9000, "", 10000]
result = find_top_3_calories(input_list)
# print("Top three Elves carrying the most calories: Elf ", result[1] + 1)
print("Calories carried by those Elves: ", result[0])

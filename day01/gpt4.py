def find_elf_with_most_calories(input_str):
    elf_inventories = input_str.strip().split('\n\n')
    total_calories = []

    for inventory in elf_inventories:
        calories = list(map(int, inventory.split('\n')))
        total_calories.append(sum(calories))

    return max(total_calories)


input_str = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''

print(find_elf_with_most_calories(input_str))  # Output: 24000
print(find_elf_with_most_calories(open('day01/1.in').read()))

def find_most_calories(calories):
    """Finds the Elf carrying the most Calories.

    Args:
        calories: A list of integers representing the Calories carried by each Elf.

    Returns:
        The Elf carrying the most Calories.
    """
    max_calories = calories[0]
    max_elf = 0
    for i in range(1, len(calories)):
        if calories[i] > max_calories:
            max_calories = calories[i]
            max_elf = i

    return max_elf


if __name__ == "__main__":
    # Read the input.
    input = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
    calories = []
    for line in input.splitlines():
        if line:
            calories.append(int(line))

    # Find the Elf carrying the most Calories.
    max_elf = find_most_calories(calories)

    # Print the number of Calories carried by the Elf carrying the most Calories.
    print(calories[max_elf])

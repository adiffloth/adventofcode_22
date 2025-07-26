# Read the input data
input_data = open("day01/0.in", "r").readlines()

# Create a list to store the calories for each elf
calories = []

# Loop over the input data
for line in input_data:
    # Split the line into a list of numbers
    numbers = line.split()
    numbers = map(int, numbers)

    # Add the calories for the elf to the list
    calories.extend(numbers)

# Calculate the sum of all the calories
total_calories = sum(calories)

# Print the sum of all the calories
print(total_calories)
print(calories)

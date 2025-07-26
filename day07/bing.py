def get_size(folder):
    # Base case: if folder is empty, return 0
    if not folder:
        return 0
    # Recursive case: if folder has subfolders, add their sizes
    total = 0
    for subfolder in folder.values():
        total += get_size(subfolder)
    # Return the total size plus 1 for the current folder
    return total + 1


# Read input file and split into lines
with open("day07/00.in") as f:
    lines = f.read().splitlines()


# Create a nested dictionary to represent the file system
root = {}
for line in lines:
    # Split line by slashes and reverse it
    path = line.split("/")[::-1]
    # Start from root and create subfolders as needed
    current = root
    for folder in path:
        # If folder does not exist, create it as an empty dict
        if folder not in current:
            current[folder] = {}
        # Move to the next subfolder
        current = current[folder]

# Get a list of (size, name) tuples for each top-level folder
sizes = []
for name, subfolder in root.items():
    size = get_size(subfolder)
    sizes.append((size, name))

# Sort the list by size (descending) and name (ascending)
sizes.sort(key=lambda x: (-x[0], x[1]))

# Print the first three folders with their sizes
for i in range(3):
    print(sizes[i][1], sizes[i][0])

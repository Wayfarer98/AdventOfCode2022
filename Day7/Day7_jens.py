import numpy as np

with open('input.txt', 'r') as f:
    lines = f.readlines()
lines = [s.strip() for s in lines]

directories = {}
path = []

for command in lines:
    if "$ cd .." in command:
        path.pop()
        continue

    if "$ cd" in command:
        path.append(command.split(" ").pop())
        if "\\".join(path) not in directories:
            directories["\\".join(path)] = 0
            continue

    if "$ ls" in command or "dir" in command:
        continue

    size = int(command.split(' ')[0])
    for folder_index in range(len(path)):
        if folder_index == 0:
            directories[path[folder_index]] += size
            continue

        directories["\\".join(path[:folder_index+1])] += size

total = sum(directories[direct] for direct, value in directories.items() if value <= 100000)

total_space_used = directories['/']
free_space = 70000000 - total_space_used
needed_space = 30000000 - free_space

big_enough_directories = [v for _, v in directories.items() if v >= needed_space]
big_enough_directories.sort()
print(big_enough_directories[0])
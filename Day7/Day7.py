import numpy as np

with open('input.txt', 'r') as f:
    lines = f.readlines()
lines = [s.strip() for s in lines]

sizes = {}
def find_size_of_dir(dir: str, index: int) -> tuple:
    local_index = index
    size = 0
    while local_index < len(lines) and ("$ cd .." not in lines[local_index] and "cd /" not in lines[local_index]):
        command = lines[local_index]
        if "$ cd" in command:
            nested_size, new_index = find_size_of_dir(command.split(' ')[2], local_index + 1)
            size += nested_size
            local_index = new_index
        elif "dir " in command or "$ ls" in command:
            local_index += 1
        else:
            size += int(command.split(' ')[0])
            local_index += 1
    sizes[dir + str(local_index)] = size
    return size, local_index + 1

# i = 1
# while i < len(lines):
#     _, index = find_size_of_dir("/", i)
#     i = index

find_size_of_dir("/", 1)

vals = [v for _, v in sizes.items() if v <= 100000]
print(sum(vals))

# part 2

name_for_root = [k for k, _ in sizes.items() if "/" in k]
total_space_used = sizes[name_for_root[0]]
free_space = 70000000 - total_space_used
needed_space = 30000000 - free_space

big_enough_directories = [v for _, v in sizes.items() if v >= needed_space]
big_enough_directories.sort()
print(big_enough_directories[0])
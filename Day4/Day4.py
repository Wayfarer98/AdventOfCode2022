import numpy as np

data = np.loadtxt('input.txt', delimiter=',', dtype=str)
def is_contained(range1, range2):
    return int(range1[0]) <= int(range2[0]) and int(range1[1]) >= int(range2[1])

# sourcery skip: sum-comprehension
total_overlapping_pairs = 0
for i in data:
    first = i[0].split('-')
    second = i[1].split('-')
    if is_contained(first, second) or is_contained(second, first):
        total_overlapping_pairs += 1

print(total_overlapping_pairs)

# Part 2

def is_overlapping(range1, range2):
    return int(range1[0]) <= int(range2[0]) and int(range1[1]) >= int(range2[0])

total_overlapping_pairs = 0
for i in data:
    first = i[0].split('-')
    second = i[1].split('-')
    if is_overlapping(first, second) or is_overlapping(second, first):
        total_overlapping_pairs += 1

print(total_overlapping_pairs)
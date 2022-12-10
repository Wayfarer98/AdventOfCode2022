import numpy as np

data = np.loadtxt('input.txt', dtype=str)

total_priority = 0
ascii_a = ord('a')
ascii_A = ord('A')
for rucksack in data:
    compartment_length = len(rucksack)//2
    compartment1 = rucksack[:compartment_length]
    compartment2 = rucksack[compartment_length:]

    for char in compartment1:
        if char in compartment2:
            ascii_val = ord(char)
            priority = ascii_val - (ascii_a - 1) if ascii_val > ascii_a else ascii_val - (ascii_A - 1) + 26
            total_priority += priority
            break

print(total_priority)

total_priority = 0
for i in range(1, len(data)//3 + 1):
    start = (i - 1) * 3
    end = start + 3
    rucksacks = data[start:end]
    for char in rucksacks[0]:
        if char in rucksacks[1] and char in rucksacks[2]:
            ascii_val = ord(char)
            priority = ascii_val - (ascii_a - 1) if ascii_val > ascii_a else ascii_val - (ascii_A - 1) + 26
            total_priority += priority
            print(total_priority, priority, char, i)
            break
print(total_priority)
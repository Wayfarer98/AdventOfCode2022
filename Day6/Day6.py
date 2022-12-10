import numpy as np

data = str(np.loadtxt('input.txt', dtype=str))

def check_sequence(sequence):
    char_set = [False] * 128
    for i in range(len(sequence)):
        val = ord(sequence[i])
        if char_set[val]:
            return False
        char_set[val] = True

    return True

for i in range(len(data) - 3):
    sequence = data[i:i+4]
    if check_sequence(sequence):
        index = i + 4
        print(sequence)
        break

print(index)

for i in range(len(data) - 13):
    sequence = data[i:i+14]
    if check_sequence(sequence):
        index = i + 14
        print(sequence)
        break

print(index)
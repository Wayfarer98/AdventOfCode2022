import numpy as np

with open('input.txt', 'r') as f:
    lines = f.readlines()
lines = [x.replace('\n', '') for x in lines]
lines.append('')

def divide_list_next(lst):
    j = 0
    ret = []
    for i in range(len(lst)):
        if not lst[i]:
            ret.append(sum(int(x) for x in lst[j:i]))
            j = i + 1
    return ret

divided = divide_list_next(lines)

print(max(divided))

divided.sort(reverse=True)

print(sum(divided[:3]))
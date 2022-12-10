import numpy as np
import copy

with open('input.txt', 'r') as f:
    lines = f.readlines()

initial_stack = [[] for _ in range(9)]
for i in reversed(range(8)):
    lines[i] += ' '
    for j in range(9):
        start = 4 * j
        end = start + 4
        if item := lines[i][start:end].strip():
            initial_stack[j].append(item)

moves = lines[10:]

stack = copy.deepcopy(initial_stack)
print(stack)

def parse_move(move):
    move_arr = move.split(' ')
    amount = int(move_arr[1])
    from_column = int(move_arr[3])
    to_column = int(move_arr[5])
    return amount, from_column, to_column

def make_move(amount, from_column, to_column):
    for _ in range(amount):
        item = stack[from_column - 1].pop()
        stack[to_column - 1].append(item)

def find_tops(stack_inp):
    ret = ''
    for i in range(9):
        item = stack_inp[i][-1]
        ret += item[1]
    return ret

for move in moves:
    amount, from_column, to_column = parse_move(move)
    make_move(amount, from_column, to_column)

print(find_tops(stack))

# Part 2
stack2 = copy.deepcopy(initial_stack)

def make_new_move(amount, from_column, to_column):
    intermediate = [stack2[from_column - 1].pop() for _ in range(amount)]
    intermediate.reverse()
    stack2[to_column - 1].extend(intermediate)

for move in moves:
    amount, from_column, to_column = parse_move(move)
    make_new_move(amount, from_column, to_column)

print(find_tops(stack2))
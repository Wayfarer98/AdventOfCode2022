import numpy as np

A = {'A': "Rock", 'B': "Paper", 'C': "Scissor"}
X = {'X': "Rock", 'Y': "Paper", 'Z': "Scissor"}
values = {"Rock": 1, "Paper": 2, "Scissor": 3}
outcome = {"Win": 6, "Draw": 3, "Lose": 0}

data = np.loadtxt('input.txt', delimiter=' ', dtype=str)

def who_wins(mine, theirs):
    if mine == theirs:
        return 'Draw'
    if mine == 'Rock' and theirs == "Scissor" or mine == 'Scissor' and theirs == 'Paper' or mine == 'Paper' and theirs == 'Rock':
        return 'Win'
    else:
        return 'Lose'

total_score = 0
for i in data:
    opponent = A[i[0]]
    mine = X[i[1]]
    value = values[mine]
    win = who_wins(mine, opponent)
    total_score += value + outcome[win]

print(total_score)

# Part 2

X = {'X': "Lose", 'Y': "Draw", 'Z': "Win"}

def what_to_pick(theirs, result):
    if result == "Draw":
        return theirs
    if result == "Lose":
        if theirs == "Paper":
            return "Rock"
        elif theirs == "Rock":
            return "Scissor"
        else:
            return "Paper"
    elif result == "Win":
        if theirs == "Paper":
            return "Scissor"
        elif theirs == "Rock":
            return "Paper"
        else:
            return "Rock"

total_score = 0
for i in data:
    opponent = A[i[0]]
    result = X[i[1]]
    mine = what_to_pick(opponent, result)
    value = values[mine]
    total_score += value + outcome[result]

print(total_score)
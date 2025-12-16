

file = 'aoc1-input.txt' # Make sure this path is correct

with open(file, 'r') as f:

    moves = [line.strip() for line in f]

pos = 50 

for move in moves:
    if move[0] == 'L':
        pos -= move[1:]
    else:
        pos += move[1:]
    

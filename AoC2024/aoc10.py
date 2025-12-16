input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

matrix = [[int(num) for num in row] for row in input.split("\n")]
n = len(matrix)
m = len(matrix[0])



for i in range(len(matrix)):
    matrix[i].insert(0, '.')
    matrix[i].append('.')
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            break

matrix.insert(0, ['.'] * len(matrix[0]))
matrix.append(['.'] * len(matrix[0]))

def find_path(nextNum):

    

for row in matrix:
    print(row)


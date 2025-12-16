input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

rows = [[int(num) for num in row] for row in input.split("\n")] 

print(rows) 

for row in rows: 
    for num in row: 
        if num == 0:
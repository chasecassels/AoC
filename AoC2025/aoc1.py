def main():

    file = 'aoc1-input.txt'
    pos = 50 
    ans = 0

    with open(file, 'r') as f:
        moves = [line.strip() for line in f]

    for move in moves:
        if move[0] == 'L':
            pos = (pos - int(move[1:])) % 100
        else:
            pos = (pos + int(move[1:])) % 100
        if pos == 0:
            ans += 1

    print(ans)
    
if __name__ == "__main__":
    main()

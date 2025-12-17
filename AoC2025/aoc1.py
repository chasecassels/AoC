def main():

    file = 'testinput.txt'

    pos = 50 
    ans1 = 0
    ans2 = 0

    with open(file, 'r') as f:
        moves = [line.strip() for line in f]

    #compute part 1 answer
    for move in moves:
        if move[0] == 'L':
            pos = (pos - int(move[1:])) % 100
        else:
            pos = (pos + int(move[1:])) % 100
        if pos == 0:
            ans1 += 1
    
    pos = 50

    #compute part 2 answer
    for move in moves:
        if move[0] == 'L':
            if pos != 0 and pos - int(move[1:]) < 0:  
                #subtract because the integer division is negative 
                ans2 -= (pos - int(move[1:])) // 100
            pos = (pos - int(move[1:])) % 100
        else: # move[0] == 'R'
            if pos + int(move[1:]) > 100:
                ans2 += (pos + int(move[1:])) // 100
            pos = (pos + int(move[1:])) % 100
        if pos == 0:
            ans2 += 1

        print(pos)

    print(ans2)


    
if __name__ == "__main__":
    main()

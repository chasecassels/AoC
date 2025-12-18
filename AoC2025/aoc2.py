def main():

    file = 'aoc2-input.txt'
    ans1 = 0
    intervals = []
    
    with open(file, 'r') as f:
        line = f.readline()
        intervals = line.split(',')
    
    for interval in intervals:
        bounds = interval.split('-')
        lower = int(bounds[0])
        upper = int(bounds[1])
        for num in range(lower, upper + 1):
            strnum = str(num)
            length = len(strnum)
            if length % 2 == 0:
                half = int(length / 2)
                if strnum[:half] == strnum[half:]:
                    ans1 += num

    print(ans1)

if __name__ == "__main__":
    main()

def main():

    file = 'aoc2-input.txt'
    ans1 = 0
    ans2 = 0
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

            #check each possible length for repeating substrings
            for i in range(1, (length // 2) + 1):
                
                if length % i == 0:
                    for j in range(i, length, i):   
                        if strnum[j:j+i] != strnum[j-i:j]:
                            
                            #current substring length cant divide string to create an invalid id
                            break
                    else:
                        #loop completed, so ID is invalid. We want to stop immediately before determing
                        #it's invalid through a different substring length (ie, '111111' is invalid using
                        #substrings of length 1 or 2 or 3)
                        ans2 += num
                        break

    print(ans1)
    print(ans2)

if __name__ == "__main__":
    main()

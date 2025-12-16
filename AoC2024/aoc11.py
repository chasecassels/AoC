input = """28591 78 0 3159881 4254 524155 598 1"""

stones = [stone for stone in input.split(" ")]

def blink(stones):
    tempstones = []
    for stone in stones:
        if stone == '0':
            tempstones.append('1')
        elif len(stone) % 2 == 0:
            tempstones.append(str(int(stone[:int(len(stone)/2)])))
            tempstones.append(str(int(stone[int(len(stone)/2):])))
        else:
            tempstones.append(str(int(stone) * 2024))
    return tempstones


for _ in range(25):
    stones = blink(stones)

print(len(stones))
    
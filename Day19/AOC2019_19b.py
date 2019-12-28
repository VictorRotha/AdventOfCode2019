from collections import defaultdict
from Intcode import Computer
import time

def show(grid, size=50):
    print('SHOW')
    for y in range(size):
        print (y, end='  ')
        for x in range(size):
            if (x,y) in grid:
                print(grid[(x,y)], end=' ')
            else:
                print('.', end=' ')
        print()

base_program = defaultdict(int)
with open('input.txt', 'r') as f:
    for n, x in enumerate(f.readline().strip().split(',')):
        base_program[n] = int(x)

now = time.time()
computer = Computer(base_program)

def find_left(line, lastleft):
    for i in range(line):
        if i < lastleft:
            continue
        if grid[i, line] == 1:
            return i

def check_square(line, left, size):
    top = line - size + 1
    right = left + size - 1
    if top < 0:
        return False
    if grid[left, top] == 0:
        return False
    if grid[right, top] == 0:
        return False
    return True

size = 100
grid = defaultdict(int)

line = 0
left = 0

while True:
    first = False
    for i in range(line):
        if i < left:
            continue
        pos = (i, line)
        computer.reset()
        result = computer.run(pos)
        grid[pos] = result
        if result:
            first = True
        elif first and not result:
            break

    new_left = find_left(line, left)
    left = left if new_left is None else new_left

    if check_square(line, left, size):
        print(f'SQUARE {size} FOUND AT LINE {line}, TOPLEFT: {left}, {line - size + 1}' )
        print(f'PART 02: {left*10000 + (line - size + 1)}')
        break

    # if line % 500 == 0:
    #     print ('Counter ', line, time.time() - now)

    line += 1

# show(grid, size = 100)
print(time.time() - now)

# SQUARE 100 FOUND AT LINE 1381, TOPLEFT: 944, 1282
# PART 02: 9441282
# 336.53124594688416
from collections import defaultdict
from Intcode import Computer
import time

def show(grid):
    print('SHOW')
    for y in range(50):
        for x in range(50):
            if (x,y) in grid:
                print(grid[(x,y)], end='')
            else:
                print('.', end='')
        print()

base_program = defaultdict(int)
with open('input.txt', 'r') as f:
    for n, x in enumerate(f.readline().strip().split(',')):
        base_program[n] = int(x)

now = time.time()

computer = Computer(base_program)

grid = {}
counter = 0
for y in range(50):
    for x in range(50):
        computer.reset()
        result = computer.run([x, y])
        grid[(x, y)] = result
        if result == 1:
            counter += 1

show(grid)
print(counter)
print(time.time() - now)

# PART 01:
# 160
# 6.664640426635742

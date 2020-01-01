def show(grid):
    for y in range(5):
        for x in range(5):
            print (grid[(x,y)], end='')
        print()

def new_grid(grid):
    newgrid = {}
    for y in range(5):
        for x in range(5):
            nbs = [nb for nb in ((x-1, y), (x+1, y), (x, y+1), (x, y-1)) if nb in grid]
            bugs = 0
            for nb in nbs:
                if grid[nb] == '#':
                    bugs+=1
            if grid[(x,y)] == '#':
                newgrid[(x,y)] = '#' if bugs == 1 else '.'
            if grid[(x,y)] == '.':
                newgrid[(x,y)] = '#' if bugs in (1,2) else '.'
    return newgrid

def biodiversity(grid):
    result = 0
    for y in range(5):
        for x in range(5):
            if grid[(x,y)] == '#':
                pos = x + 5*y
                result += pow(2, pos)
    return result

base_grid = {}
with open('input.txt') as f:
    for y, line in enumerate(f):
        for x, char in enumerate(line.strip()):
            base_grid[x,y] = char

bios = []
grid = base_grid.copy()
while True:
    # print(i)
    # show(grid)
    bio = biodiversity(grid)
    if bio in bios:
        print('PART 01: ', bio)
        break
    bios.append(bio)
    grid = new_grid(grid)

# PART 01:  18350099

import time

def show(grid, n):
    for z in range(-n, n+1):
        print (z)
        for y in range(5):
            for x in range(5):
                if (x,y,z) in grid:
                    print (grid[x,y,z], end = '')
            print()

def new_grid(grid):
    newgrid = {}
    for position in grid:
        x,y,z = position
        nbs = [(a,b,c) for (a,b,c) in ((x - 1, y, z), (x + 1, y, z), (x, y + 1, z), (x, y - 1, z))
               if a in range(5) and b in range(5) and (a,b) != (2,2)]
        if x == 0:
            nbs.append((1,2,z-1))
        elif x == 4:
            nbs.append((3,2,z-1))
        if y == 0:
            nbs.append((2,1, z-1))
        elif y == 4:
            nbs.append((2, 3, z - 1))
        d = {(1,2): [(0, y1, z+1) for y1 in range(5)],
             (3,2): [(4, y1, z+1) for y1 in range(5)],
             (2,1): [(x1, 0, z+1) for x1 in range(5)],
             (2,3): [(x1, 4, z+1) for x1 in range(5)]}
        if (x,y) in d:
            nbs.extend(d[(x,y)])
        bugs = 0
        for nb in nbs:
            if nb in grid and grid[nb] == '#':
                bugs += 1
        if grid[position] == '#':
            newgrid[position] = '#' if bugs == 1 else '.'
        if grid[position] == '.':
            newgrid[position] = '#' if bugs in (1, 2) else '.'
    return newgrid

def new_level(n):
    result = {}
    for y in range(5):
        for x in range(5):
            if (x,y) != (2,2):
                result[(x,y,n)] = '.'
    return result

def have_bugs(n):
    for y in range(5):
         for x in range(5):
            if (x,y,n) in grid and grid[(x, y, n)] == '#':
                return True
    return False

def count_bugs(grid):
    bugs = 0
    for position in grid:
        if grid[position] == '#':
            bugs += 1
    return bugs

now = time.time()
base_grid = {}
with open('input.txt') as f:
    for y, line in enumerate(f):
        for x, char in enumerate(line.strip()):
            if (x,y) != (2,2):
                base_grid[(x,y,0)] = char

levels = [0,0]
mins = 200
grid = base_grid.copy()
for i in range(mins):
    if have_bugs(levels[0]):
        newlevel = new_level(levels[0]-1)
        grid.update(newlevel)
        levels[0] -= 1
    if have_bugs(levels[1]):
        newlevel = new_level(levels[1]+1)
        grid.update(newlevel)
        levels[1] += 1
    grid = new_grid(grid)

print (f'bugs after {mins} minutes: {count_bugs(grid)}')
print (time.time() - now)

# PART 02: bugs after 200 minutes: 2037
# 10.33168339729309

def get_manhatten(x, y):
    return abs(x)+abs(y)

def make_path(wire):
    pos = (0,0)
    path = []
    for node in wire:
        for step in range(int(node[1:])):
            if node[0] == 'R':
                pos = (pos[0] + 1, pos[1])
            elif node[0] == 'L':
                pos = (pos[0] - 1, pos[1])
            elif node[0] == 'U':
                pos = (pos[0], pos[1] - 1)
            elif node[0] == 'D':
                pos = (pos[0], pos[1] + 1)
            path.append(pos)
    return path

with open('input.txt', 'r') as f:
    wire01 = f.readline().split(',')
    wire02 = f.readline().split(',')

path01 = make_path(wire01)
path02 = make_path(wire02)
crossings = set(path01).intersection(set(path02))

distance = min([get_manhatten(pos[0], pos[1]) for pos in crossings])

print('path01', len(path01), 'path02', len(path02))
print('crossings', len(crossings))
print('shortest manhatten distance: ',  distance)

# part 2:

steps = []
for cross in crossings:
    steps01 = path01.index(cross) + 1
    steps02 = path02.index(cross) + 1
    steps.append(steps01+steps02)

print('fewest combined steps: ', min(steps))

# path01 146120 path02 149225
# crossings 38
# shortest manhatten distance:  557
# fewest combined steps:  56410










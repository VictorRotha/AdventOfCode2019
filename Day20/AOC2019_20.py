def load_maze():
    mz = {}
    w = 0
    with open('input.txt') as f:
        for y, line in enumerate(f):
            w = max(w, len(line.strip('\n')))
            for x, char in  enumerate(line.strip('\n')):
                if char in '.#' or char.isupper():
                    mz[(x, y)] = char
        h = y+1
    return mz, w, h

def show(mz, w, h):
    for y in range(h):
        for x in range(w):
            if (x,y) in mz:
                print(mz[(x,y)], end = ' ')
            else:
                print('_', end = ' ')
        print()

def find_portals(mz, w, h):
    start, end = None, None
    visited = []
    ports = {}
    portalpoints = {}
    for y in range(h):
        for x in range(w):
            pos = (x, y)
            if pos in visited:
                continue
            if (x, y) in mz and mz[(x, y)].isupper():
                nbs = [(v[0] + x, v[1] + y, v) for v in ((0, 1), (1, 0), (0, -1), (-1, 0))]
                for nb in nbs:
                    nbx, nby, v = nb
                    nbpos = (nbx, nby)
                    if nbpos not in mz:
                        continue
                    if mz[nbpos].isupper():
                        pos1 = (nbpos[0] + v[0], nbpos[1] + v[1])
                        pos2 = (pos[0] - v[0], pos[1] - v[1])
                        if pos1 in mz and mz[pos1] == '.':
                            mzpos = nbpos
                            entrance = pos1
                        elif pos2 in mz and mz[pos2] == '.':
                            mzpos = pos
                            entrance = pos2
                        else:
                            continue
                        visited.append(nbpos)
                        portal = mz[pos] + mz[nbpos]
                        if portal == 'AA':
                            start = entrance
                        elif portal == 'ZZ':
                            end = entrance
                        else:
                            ports[mzpos] = portal
                            if portal not in portalpoints:
                                portalpoints[portal] = {mzpos: entrance}
                            else:
                                portalpoints[portal][mzpos] = entrance
    return ports, portalpoints, start, end

def neighbours(pos, mz, portals, ppoints):
    x, y = pos
    nbs = [(v[0]+x, v[1]+y) for v in ((0,1), (0,-1), (1,0), (-1,0))]
    neighbours = []
    for nb in nbs:
        if nb not in mz or mz[nb] == '#':
            continue
        if mz[nb] == '.':
            neighbours.append(nb)
        elif nb in portals:
            for portal in ppoints[portals[nb]]:
                if portal != nb:
                    destination = ppoints[portals[nb]][portal]
                    neighbours.append(destination)
    return neighbours

def find_path(mz, start, end, portals, ppoints):
    nodes = [start]
    visited = {start: 0}
    while nodes:
        pos = nodes.pop(0)
        for nb in neighbours(pos, mz, portals, ppoints):
            if nb in visited:
                continue
            if nb == end:
                print ('EXIT', visited[pos]+1, nb)
            else:
                visited[nb] = visited[pos] + 1
                nodes.append(nb)

maze, width, height = load_maze()
portals, ppoints, start, end = find_portals(maze, width, height)
find_path(maze, start, end, portals, ppoints)
# show(maze, width, height)

# EXIT 654 (122, 71)




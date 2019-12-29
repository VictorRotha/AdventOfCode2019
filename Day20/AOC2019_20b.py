def load_maze():
    mz = {}
    w = 0
    with open('input.txt') as f:
        for y, line in enumerate(f):
            w = max(w, len(line.strip('\n')))
            for x, char in enumerate(line.strip('\n')):
                if char in '.#' or char.isupper():
                    mz[(x, y)] = char
        h = y + 1
    return mz, w, h

def show(mz, w, h):
    for y in range(h):
        for x in range(w):
            if (x, y) in mz:
                print(mz[(x, y)], end=' ')
            else:
                print('_', end=' ')
        print()

def is_inner(pos, w, h):
    x, y, l = pos
    if y < 2 or y > h - 3 or x < 2 or x > w - 3:
        return -1
    return 1

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
                        # print(pos, nbpos, v, pos1, pos2)
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
                            start = (entrance[0], entrance[1], 0)
                        elif portal == 'ZZ':
                            end = (entrance[0], entrance[1], 0)
                        else:
                            ports[mzpos] = portal
                            if portal not in portalpoints:
                                portalpoints[portal] = {mzpos: entrance}
                            else:
                                portalpoints[portal][mzpos] = entrance

    return ports, portalpoints, start, end


def neighbours(pos, mz, w, h, portals, ppoints):
    x, y, l = pos
    nbs = [(v[0] + x, v[1] + y, l) for v in ((0, 1), (0, -1), (1, 0), (-1, 0))]
    neighbours = []
    for nb in nbs:
        if nb[:2] not in mz or mz[nb[:2]] == '#':
            continue
        if mz[nb[:2]] == '.':
            neighbours.append(nb)
        elif nb[:2] in portals:
            dl = is_inner(nb, w, h)
            if l+dl >= 0:
                for portal in ppoints[portals[nb[:2]]]:
                    if portal != nb[:2]:
                        destination = ppoints[portals[nb[:2]]][portal]
                        neighbours.append((destination[0], destination[1], l+dl))
    return neighbours

def find_path(mz, start, end, w, h, portals, ppoints):
    nodes = [start]
    visited = {start: 0}
    found_exit = False
    while nodes and not found_exit:
        pos = nodes.pop(0)
        for nb in neighbours(pos, mz, w, h, portals, ppoints):
            if nb in visited:
                continue
            if nb == end:
                print('EXIT', visited[pos] + 1, nb)
                found_exit = True
            else:
                visited[nb] = visited[pos] + 1
                nodes.append(nb)


maze, width, height = load_maze()
portals, ppoints, start, end = find_portals(maze, width, height)
find_path(maze, start, end, width, height, portals, ppoints)

# show(maze, width, height)

# EXIT 7360 (122, 71, 0)




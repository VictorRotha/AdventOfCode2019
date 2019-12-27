import time

position = None
keys = {}
base_pos = {}
positions = []
with open('input2.txt', 'r') as f:
    for i, row in enumerate(f):
        for j, col in enumerate(row.strip()):
            if col == '#':
                continue
            base_pos[(j, i)] = col
            if col == '@':
                positions.append((j, i))
            elif col.islower():
                keys[col] = (j, i)

print('Positions: ', positions)
print('Keys  ', len(keys), keys)
print('Base Positions: ', len(base_pos), base_pos)

cache = {}

def neighbours(pos):
    result = []
    for v in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nb = (pos[0] + v[0], pos[1] + v[1])
        if nb in base_pos:
            result.append(nb)
    return result

def keys_in_range(pos, collected_keys):
    nodes = [pos]
    visited = {pos: 0}
    keys_found = {}
    while nodes:
        pos = nodes.pop(0)
        distance = visited[pos]
        for nb in neighbours(pos):
            if nb in visited:
                continue
            visited[nb] = distance + 1
            if base_pos[nb].isupper() and base_pos[nb].lower() not in collected_keys:
                    continue
            if base_pos[nb].islower() and base_pos[nb] not in collected_keys:
                keys_found[base_pos[nb]] = distance + 1
            else:
                nodes.append(nb)
    return keys_found

def choose_robot(positions, collected_keys):
    keys_found = {}
    for i, pos in enumerate(positions):
        keysinrange = keys_in_range(pos, collected_keys)
        for key, keydist in keysinrange.items():
            keys_found[key] = (keydist, i)
    return keys_found

def shortest_path(poss, collected_keys):
    cache_key = (tuple(poss), ''.join(sorted(collected_keys)))
    if cache_key in cache:
        return cache[cache_key]
    keysinrange = choose_robot(poss, collected_keys)
    if not keysinrange:
        result = 0
    else:
        distances = []
        for key, (keydist, robot) in keysinrange.items():
            newpos = []
            for i, pos in enumerate(poss):
                if i == robot:
                    newpos.append(keys[key])
                else:
                    newpos.append(pos)
            distances.append(keydist + shortest_path(newpos, collected_keys + [key]))
        result = min(distances)
    cache[cache_key] = result
    return result

now = time.time()
print('PART 02: ', shortest_path(positions, []))
print(time.time()-now)

# PART 02:  1222
# 7.1796112060546875


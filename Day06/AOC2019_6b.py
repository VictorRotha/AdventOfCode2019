directs = {}
neighbours = {}

with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        value, key = line.split(')')
        directs[key] = value
        if key not in neighbours:
            neighbours[key] = [value]
        elif value not in neighbours[key]:
            neighbours[key].append(value)
        if value not in neighbours:
            neighbours[value] = [key]
        elif key not in neighbours[value]:
            neighbours[value].append(key)

me = directs['YOU']
santa = directs['SAN']

def find_path(start, last, n):
    for neighbour in neighbours[start]:
        if neighbour == last:
            continue
        if neighbour == santa:
            print('SANTA', n)
            return n
        else:
            find_path(neighbour, start, n+1)

find_path(me, 'YOU', 1)

# part2: 433







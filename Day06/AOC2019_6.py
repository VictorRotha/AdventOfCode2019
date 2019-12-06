directs = {}
with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        key = line[4:]
        value = line[:3]
        directs[key] = value

print(directs)
total_orbits = 0
for direct in directs:
    orbits = 0
    thing = direct
    while True:
        if thing in directs:
            orbits += 1
            thing = directs[thing]
        else:
            break
    total_orbits += orbits

print(total_orbits)

# part1: 292387






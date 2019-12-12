import math

base_positions = []
with open('input.txt', 'r') as f:
    for line in f:
        pos = line.strip()[:-1].split(',')
        base_positions.append([int(ax.split('=')[1]) for ax in pos])

positions = base_positions.copy()
velocities = [(0,)*3]*4
steps = 1000

def apply_gravity(planet):
    gravity = [0,0,0]
    for ax in range(3):
        for pl in range(4):
            distance = positions[planet][ax] - positions[pl][ax]
            dg = 1 if distance < 0 else -1 if distance > 0 else 0
            gravity[ax] += dg
    velocities[planet] = [(v+g) for v, g in zip(velocities[planet], gravity)]

seen = {k : set() for k in range(3)}
count = {k: 0 for k in range(3)}
timestep = 0
first = []
while True:
    keys = {k: [] for k in range(3)}
    for i in range(3):
        for j in range(4):
            keys[i].append(positions[j][i])
            keys[i].append(velocities[j][i])
    keys = {k: tuple(i) for k, i in keys.items()}

    if timestep % 50000 == 0:
        print(timestep)

    for k in range(3):
        if count[k] == 0:
            if keys[k] in seen[k]:
                print (k, count[k], timestep)
                first.append(timestep)
                count[k] += 1
        seen[k].add(keys[k])

    if len(first) == 3:
        print ('FIRST', first)
        for n in range(2):
            first[n+1] = first[n]*first[n+1]//math.gcd(first[n], first[n+1])
        print (first[2])
        break

    for planet in range(4):
        apply_gravity(planet)
    for planet in range(4):
        positions[planet] = [(pos + vel) for pos, vel in zip(positions[planet], velocities[planet])]
    timestep += 1


# 325433763467176


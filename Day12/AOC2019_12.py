positions = []
with open('input.txt', 'r') as f:
    for line in f:
        pos = line.strip()[:-1].split(',')
        positions.append([int(ax.split('=')[1]) for ax in pos])

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

for timestep in range(steps):
    for planet in range(4):
        apply_gravity(planet)
    for planet in range(4):
        positions[planet] = [(pos + vel) for pos, vel in zip(positions[planet], velocities[planet])]

kinetics = []
potentials = []
for planet in range(4):
    potentials.append(sum([abs(p) for p in positions[planet]]))
    kinetics.append(sum([abs(v) for v in velocities[planet]]))
total_energy = sum([p*k for p, k in zip(potentials, kinetics)])

print (f'TOTAL ENERGY ({steps}): {total_energy}')

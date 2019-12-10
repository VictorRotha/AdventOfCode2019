
asteroid_map = []
with open('input.txt', 'r') as f:
    for line in f:
        asteroid_map.append(line.strip())

asteroids = []
station = None
for i, row in enumerate(asteroid_map):
    for j, col in enumerate(row):
        if col == '#':
            asteroids.append((j, i))

current = (14,17)

print('STATION: ', current)
print ('ASTEROIDS ', len(asteroids))

numbers = {}
right_ratios = {}
left_ratios = {}
distance = {}

for asteroid in asteroids:
    dx =  asteroid[0]- current[0]
    dy =  asteroid[1]-current[1]
    distance[asteroid] = abs(dx) + abs(dy)
    if dx != 0:
        ratio = dy/dx
        if dx > 0:
            right_ratios[asteroid] = ratio
        elif dx < 0 :
            left_ratios[asteroid] = ratio
    elif dx == 0:
        if dy > 0:
            left_ratios[asteroid] = 'bottom'
        elif dy < 0:
            right_ratios[asteroid] = 'top'

def destroy_nearest(ratios, counter):
    checked_ratios = []
    while True:
        values = [val for val in list(ratios.values()) if val not in checked_ratios]
        if not values:
            break
        if 'top' in values:
            min_value = 'top'
        elif 'bottom' in values:
            min_value = 'bottom'
        else:
            min_value = min(values)
        min_keys = {}
        for asteroid in ratios:
            if ratios[asteroid] == min_value:
                min_keys[asteroid] = distance[asteroid]

        min_dist = min(list(min_keys.values()))
        min_index = list(min_keys.values()).index(min_dist)
        min_asteroid = list(min_keys.keys())[min_index]
        del ratios[min_asteroid]
        checked_ratios.append(min_value)
        counter += 1
        if counter == 200:
            print ('COUNTER 200 ', min_asteroid[0]*100+min_asteroid[1])
    return counter

counter = 0
while right_ratios or left_ratios:
    counter = destroy_nearest(right_ratios, counter) if len(right_ratios) > 0 else counter
    counter = destroy_nearest(left_ratios, counter) if len(left_ratios) > 0 else counter

# STATION:  (14, 17)
# ASTEROIDS  356
# COUNTER 200  608




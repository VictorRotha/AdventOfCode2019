
asteroid_map = []
with open('input.txt', 'r') as f:
    for line in f:
        asteroid_map.append(line.strip())

asteroids = []
for i, row in enumerate(asteroid_map):
    for j, col in enumerate(row):
        if col == '#':
            asteroids.append((j, i))

numbers = {}
for current in asteroids:
    left_ratios = []
    right_ratios = []
    for asteroid in asteroids:
        if asteroid == current:
            continue
        dx = asteroid[0] - current[0]
        dy = asteroid[1] - current[1]
        if dx != 0 and dy != 0:
            ratio = dy/dx
            if ratio == 0:
                print (ratio, asteroid)
            if dx > 0 and not ratio in right_ratios:
                right_ratios.append(ratio)
            elif dx < 0 and not ratio in left_ratios:
                left_ratios.append(ratio)
        elif dx == 0:
            if dy > 0 and not 'samex' in right_ratios:
                right_ratios.append('samex')
            elif dy < 0 and not 'samex' in left_ratios:
                left_ratios.append('samex')
        elif dy == 0:
            if dx > 0 and not 'samey' in right_ratios:
                right_ratios.append('samey')
            elif dx < 0 and not 'samey' in left_ratios:
                left_ratios.append('samey')
    numbers[current] = len(left_ratios)+len(right_ratios)

key_numbers = list(numbers.keys())
val_numbers = list(numbers.values())

max_value = max(val_numbers)
max_index = val_numbers.index(max_value)
max_key = key_numbers[max_index]

print ('ALL  ', len(numbers))
print ('BEST ', max_key, max_value)

# ALL   356
# BEST  (14, 17) 260









total = 0
with open('input.txt', 'r') as f:
    for line in f:
        fuel_total, fuel_part = 0, 0
        mass = int(line)
        while mass > 0:
            fuel_part = mass // 3 - 2
            if fuel_part > 0:
                fuel_total += fuel_part
            mass = fuel_part
        total += fuel_total

print (total)
# 4973616 (part two)
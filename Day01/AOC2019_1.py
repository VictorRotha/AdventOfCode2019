# 3317659 (part one)

total = 0
with open('input.txt', 'r') as f:
    for line in f:
        mass = int(line)
        fuel = mass // 3 - 2
        total += fuel

print (total)
# 3317659 (part one)






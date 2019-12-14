import re
from collections import defaultdict

recipe_in = {}
recipe_out = {}
leftover = defaultdict(int)
with open('input.txt', 'r') as f:
    for line in f:
        p = line.strip().split('=>')
        product = re.search('([0-9]+) ([A-Z]+)', p[1]).group(1,2)
        recipe_out[product[1]] = int(product[0])
        recipe_in[product[1]] = {k: int(v) for v, k in re.findall('([0-9]+) ([A-Z]+)', p[0])}

def produce(substance, amount):
    amount = amount - leftover[substance]
    leftover[substance] = 0
    ore = 0
    m = amount / recipe_out[substance]
    m = m if m == int(m) else (m // 1) + 1
    leftover[substance] += m*recipe_out[substance]-amount
    for ingred, value in recipe_in[substance].items():
        if ingred == 'ORE':
            return m*value
        ore += produce(ingred, m*value)
    return int(ore)

total = produce('FUEL', 1)
print ('ORE NEEDED FOR 1 FUEL: ', total)

def produce_fl(substance, amount):
    ore = 0
    m = amount / recipe_out[substance]
    for ingred, value in recipe_in[substance].items():
        if ingred == 'ORE':
            return m*value
        ore += produce_fl(ingred, m*value)
    return ore

total = produce_fl('FUEL', 1)
print ('FUEL FROM 1 TILLION ORE: ', int(1_000_000_000_000/total))

# ORE NEEDED FOR 1 FUEL:  168046
# FUEL FROM 1 TILLION ORE:  6972986

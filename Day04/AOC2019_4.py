# input range: 136760-595730
# 6 digits
# 2 adjacents are the same
# never deacrease

counter = 0
for number in range(136760, 595731):
    ispassword = True
    increased = True
    hasdouble = False
    for i, char in enumerate(str(number)):
        last = int(str(number)[i-1]) if i > 0 else None
        if i > 0 and int(char) < last:
            increased = False
            break
        if i > 0 and int(char) == last:
            hasdouble = True
    if not increased or not hasdouble:
        continue
    counter += 1

print(f'Possible Passwords: {counter}')

# part 1: 1873








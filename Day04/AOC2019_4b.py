# input range: 136760-595730
# 6 digits
# 2 adjacents are the same
# never deacrease
# part 2: doubles not part of a larger group

counter = 0
for number in range(136760, 595731):
    doubles = [1]
    decrease = False
    for i in range(1, len(str(number))):
        if str(number)[i] < str(number)[i - 1]:
            decrease = True
            break
        if str(number)[i] == str(number)[i - 1]:
            doubles[-1] += 1
        else:
            doubles.append(1)
    if not decrease and 2 in doubles:
        counter += 1

print(f'Possible Passwords: {counter}')

# part 2: 1264







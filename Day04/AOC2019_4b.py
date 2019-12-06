# input range: 136760-595730
# 6 digits
# 2 adjacents are the same
# never deacrease
# part 2: doubles not part of a larger group

counter = 0

for number in range(136760, 595731):
    ispassword = True
    increased = True
    hasdouble = False
    for i, char in enumerate(str(number)):
        last = int(str(number)[i-1]) if i > 0 else None
        lastlast = int(str(number)[i-2]) if i > 1 else None
        nxt = int(str(number)[i+1]) if i < 5 else None
        if i > 0 and int(char) < last:
            increased = False
            break
        if i > 0 and int(char) == last and hasdouble == False:
            hasdouble = True
            if int(char) == lastlast or int(char) == nxt:
                hasdouble = False

    if not increased or not hasdouble:
        continue
    counter += 1

print(f'Possible Passwords: {counter}')

# part 2: 1264 RICHTIG







from collections import defaultdict
from Intcode import Computer

base_program = defaultdict(int)
with open('input.txt', 'r') as f:
    for n, x in enumerate(f.readline().strip().split(',')):
        base_program[n] = int(x)

computer = Computer(base_program)

# PART 01
springscript = '''NOT A J
NOT B T
AND D T
OR T J
NOT C T
AND D T
OR T J
WALK
'''
script_ascii = [ord(char) for char in springscript]
out_ascii = computer.run(script_ascii)

for asc in out_ascii:
    try:
        print(chr(asc), end='')
    except ValueError:
        print('PART 01: ', asc)

# PART 01:  19349939

# PART 02
springscript = '''NOT A J
NOT B T
AND D T
AND H T
OR T J
NOT C T
AND D T
AND H T
OR T J
RUN
'''
script_ascii = [ord(char) for char in springscript]
computer.reset()
out_ascii = computer.run(script_ascii)

for asc in out_ascii:
    try:
        print(chr(asc), end='')
    except ValueError:
        print('PART 02: ', asc)

# PART 02:  1142412777
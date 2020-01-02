from collections import defaultdict
from Intcode import Computer

base_program = defaultdict(int)
with open('input.txt', 'r') as f:
    for n, x in enumerate(f.readline().strip().split(',')):
        base_program[n] = int(x)

computer = Computer(base_program)

while True:
    input_chars = input('Command: ')
    if input_chars == 'EXIT':
        break
    input_ascii = [ord(char) for char in input_chars] + [10]
    answer_ascii = computer.run(input_ascii)
    answer_chars = ''.join([chr(asc) for asc in answer_ascii])
    print (answer_chars)

# north south, west, east
# take, drop, inv


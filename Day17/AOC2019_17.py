from collections import defaultdict

class Computer:
    def __init__(self, program):
        self.program = program.copy()
        self.position = 0
        self.base = 0

    def run(self, in_value=None):
        output_values = []
        in_pos = 0
        param_1, param_2 = None, None
        param_3_pos, param_1_pos, param_2_pos = None, None, None
        while True:
            instruction = self.program[self.position]
            opcode = instruction % 100
            modus = [((instruction // 10 ** i) % 10) for i in range(2,5)]
            if opcode == 99:
                print(f'HALT at Position {self.position}, OUT {len(output_values)}')
                return output_values
            step = (0, 4, 4, 2, 2, 0, 0, 4, 4, 2)[opcode]
            positions = (self.program[self.position + 1], self.position + 1, self.base + self.program[self.position + 1])
            param_1_pos = positions[modus[0]]
            param_1 = self.program[param_1_pos]
            if opcode in (1, 2, 5, 6, 7, 8):
                positions = (self.program[self.position + 2], self.position + 2, self.base + self.program[self.position + 2])
                param_2_pos = positions[modus[1]]
                param_2 = self.program[param_2_pos]
            if opcode in (1, 2, 7, 8):
                positions = (self.program[self.position + 3], None, self.base + self.program[self.position + 3])
                param_3_pos = positions[modus[2]]

            if opcode == 1:
                self.program[param_3_pos] = param_1 + param_2
            elif opcode == 2:
                self.program[param_3_pos] = param_1 * param_2
            elif opcode == 3:
                value = in_value[in_pos]
                self.program[param_1_pos] = value
                in_pos += 1
            elif opcode == 4:
                output_value = self.program[param_1_pos]
                output_values.append(output_value)
            elif opcode == 5:
                self.position = param_2 if param_1 != 0 else self.position + 3
            elif opcode == 6:
                self.position = param_2 if param_1 == 0 else self.position + 3
            elif opcode == 7:
                self.program[param_3_pos] = 1 if param_1 < param_2 else 0
            elif opcode == 8:
                self.program[param_3_pos] = 1 if param_1 == param_2 else 0
            elif opcode == 9:
                self.base += param_1
            self.position += step

base_program = defaultdict(int)
with open('input.txt', 'r') as f:
    for n, x in enumerate(f.readline().strip().split(',')):
        base_program[n] = int(x)

computer = Computer(base_program)

scaffold = computer.run()
scaffold = ''.join([chr(i) for i in scaffold])
chr_scaff = scaffold.split()
# print(scaffold)
intersects = []
inter_sum = 0
for row in range(1, len(chr_scaff)-1):
    for col in range(1, len(chr_scaff[row])-1):
        if chr_scaff[row][col] == '.':
            continue
        if chr_scaff[row][col-1] == '#' and chr_scaff[row][col+1] == '#':
            if chr_scaff[row-1][col] == '#' and chr_scaff[row+1][col] == '#':
                intersects.append((col, row))
                inter_sum += col*row

print ('Intersections: ', len(intersects), intersects)
print ('Solution Part 01: ', inter_sum)

# Solution Part 01:  7328

base_program[0] = 2
computer = Computer(base_program)

# L 10 R 8 R 6 R 10  L 12 R 8 L 12  L 10 R 8 R 6 R 10  L 12 R 8 L 12  L 10 R 8 R 8
# L 10 R 8 R 8  L 12 R 8 L 12  L 10 R 8 R 6 R 10  L 10 R 8 R 8  L 10 R 8 R 6 R 10
A = 'L,10,R,8,R,6,R,10'
B = 'L,12,R,8,L,12'
C = 'L,10,R,8,R,8'
MAIN = 'A,B,A,B,C,C,B,A,C,A'
input_chars = MAIN + '\n' + A + '\n' + B + '\n' + C + '\n' + 'n\n'
input_ascii = [ord(char) for char in input_chars]

dust = computer.run(input_ascii)[-1]

print('Dust: ', dust)

# Solution Part 02: 1289413





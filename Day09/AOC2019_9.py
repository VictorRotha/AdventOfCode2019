
class Computer:
    def __init__(self, program):
        self.base_program = program.copy()
        self.program = program.copy()
        self.position = 0
        self.base = 0

    def reset(self):
        self.program = self.base_program.copy()
        self.position = 0

    def check_exists(self, pos):
        if pos >= len(self.program):
            self.program.extend([0]*(pos - len(self.program) + 1))

    def run(self, in_value):
        output_value = None
        param_1, param_2 = None, None
        param_3_pos, param_1_pos, param_2_pos = None, None, None
        while True:
            instruction = self.program[self.position]
            opcode = instruction % 100
            modus = [instruction // 10000, (instruction % 10000) // 1000, (instruction % 1000) // 100]
            if opcode == 99:
                print(f'HALT {output_value} at Position {self.position}')
                break

            if modus[2] == 0:
                param_1_pos = self.program[self.position + 1]
            elif modus[2] == 1:
                param_1_pos = self.position + 1
            elif modus[2] == 2:
                param_1_pos = self.base + self.program[self.position + 1]
            self.check_exists(param_1_pos)
            param_1 = self.program[param_1_pos]

            if opcode in (1, 2, 5, 6, 7, 8):
                if modus[1] == 0:
                    param_2_pos = self.program[self.position + 2]
                elif modus[1] == 1:
                    param_2_pos = self.position + 2
                elif modus[1] == 2:
                    param_2_pos = self.base + self.program[self.position + 2]
                self.check_exists(param_2_pos)
                param_2 = self.program[param_2_pos]

            if opcode in (1, 2, 7, 8):
                if modus[0] == 0:
                    param_3_pos = self.program[self.position + 3]
                elif modus[0] == 2:
                    param_3_pos = self.base + self.program[self.position + 3]
                self.check_exists(param_3_pos)

            if opcode == 1:
                self.program[param_3_pos] = param_1 + param_2
                self.position += 4
            elif opcode == 2:
                self.program[param_3_pos] = param_1 * param_2
                self.position += 4
            elif opcode == 3:
                self.program[param_1_pos] = in_value
                self.position += 2
            elif opcode == 4:
                output_value = self.program[param_1_pos]
                print(f'OUTPUT {output_value} at Position {self.position}')
                self.position += 2
                # break
            elif opcode == 5:
                self.position = param_2 if param_1 != 0 else self.position + 3
            elif opcode == 6:
                self.position = param_2 if param_1 == 0 else self.position + 3
            elif opcode == 7:
                self.program[param_3_pos] = 1 if param_1 < param_2 else 0
                self.position += 4
            elif opcode == 8:
                self.program[param_3_pos] = 1 if param_1 == param_2 else 0
                self.position += 4
            elif opcode == 9:
                self.base += param_1
                self.position += 2

with open('input.txt', 'r') as f:
    base_program = [int(n) for n in f.readline().split(',')]

input_value = 2

computer = Computer(base_program)
computer.run(input_value)

# PART 01 (input_value 1) OUTPUT 2662308295 at Position 901
# PART 02 (input_value 2) OUTPUT 63441 at Position 919









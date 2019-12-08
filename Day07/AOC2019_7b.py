import itertools

class Amplifier:
    def __init__(self, program):
        self.base_program = program.copy()
        self.program = program.copy()
        self.position = 0
        self.initialized = True
        self.phase = 0
        self.running = True

    def reset(self):
        self.program = self.base_program.copy()
        self.position = 0
        self.initialized = True

    def change_phase(self, phase):
        self.phase = phase

    def run(self, in_value):
        output_value = None
        while True:
            instruction = self.program[self.position]
            opcode = instruction % 100
            modus = [instruction // 10000, (instruction % 10000) // 1000, (instruction % 1000) // 100]
            if opcode == 99:
                self.running = False
                return output_value
            param_1 = self.program[self.program[self.position + 1]] if modus[2] == 0 else self.program[self.position + 1]
            if opcode in (1, 2, 5, 6, 7, 8):
                param_2 = self.program[self.program[self.position + 2]] if modus[1] == 0 else self.program[self.position + 2]

            if opcode == 1:
                self.program[self.program[self.position + 3]] = param_1 + param_2
                self.position += 4
            elif opcode == 2:
                self.program[self.program[self.position + 3]] = param_1 * param_2
                self.position += 4
            elif opcode == 3:
                if self.initialized:
                    self.program[self.program[self.position + 1]] = self.phase
                    self.initialized = False
                else:
                    self.program[self.program[self.position + 1]] = in_value
                self.position += 2
            elif opcode == 4:
                output_value = self.program[self.program[self.position + 1]] if modus[2] == 0 else self.program[self.position + 1]
                self.position += 2
                return output_value

            elif opcode == 5:
                self.position = param_2 if param_1 != 0 else self.position + 3
            elif opcode == 6:
                self.position = param_2 if param_1 == 0 else self.position + 3
            elif opcode == 7:
                self.program[self.program[self.position + 3]] = 1 if param_1 < param_2 else 0
                self.position += 4
            elif opcode == 8:
                self.program[self.program[self.position + 3]] = 1 if param_1 == param_2 else 0
                self.position += 4

with open('input.txt', 'r') as f:
    base_program = [int(n) for n in f.readline().split(',')]

# PART 1
# perms = itertools.permutations(range(5), 5)

perms = itertools.permutations(range(5,10), 5)
outputs = []
amps = []
for n in range(5):
    amps.append(Amplifier(base_program.copy()))

# PART 1
# for perm in perms:
#     input_value = 0
#     for n, ph in enumerate(perm):
#         amps[n].change_phase(ph)
#         amps[n].reset()
#         input_value = amps[n].run(input_value)
#     outputs.append(input_value)
#
# print ('PART 01 MAX OUTPUT: ', max(outputs))

for perm in perms:
    for n, amp in enumerate(amps):
        amp.change_phase(perm[n])
        amp.reset()
    input_value = 0
    while True:
        for n, amp in enumerate(amps):
            output_value = amp.run(input_value)
            if output_value is None:
                break
            input_value = output_value
        if output_value is None:
            break
    outputs.append(input_value)

print ('PART 02 MAX OUTPUT: ', max(outputs))

# part 2: 7818398


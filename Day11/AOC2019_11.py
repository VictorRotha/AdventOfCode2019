from collections import defaultdict

class Computer:
    def __init__(self, program):
        self.base_program = program.copy()
        self.program = program.copy()
        self.position = 0
        self.base = 0

    def check_exists(self, pos):
        if pos >= len(self.program):
            self.program.extend([0]*(pos - len(self.program) + 1))

    def run(self, in_value):
        output_values = []
        param_1, param_2 = None, None
        param_3_pos, param_1_pos, param_2_pos = None, None, None
        while True:
            instruction = self.program[self.position]
            opcode = instruction % 100
            modus = [((instruction // 10 ** i) % 10) for i in range(2,5)]
            if opcode == 99:
                # print(f'HALT {output_values} at Position {self.position}')
                return 'HALT', 'HALT'
            step = (0, 4, 4, 2, 2, 0, 0, 4, 4, 2)[opcode]
            positions = (self.program[self.position + 1], self.position + 1, self.base + self.program[self.position + 1])
            param_1_pos = positions[modus[0]]
            self.check_exists(param_1_pos)
            param_1 = self.program[param_1_pos]
            if opcode in (1, 2, 5, 6, 7, 8):
                positions = (self.program[self.position + 2], self.position + 2, self.base + self.program[self.position + 2])
                param_2_pos = positions[modus[1]]
                self.check_exists(param_2_pos)
                param_2 = self.program[param_2_pos]
            if opcode in (1, 2, 7, 8):
                positions = (self.program[self.position + 3], None, self.base + self.program[self.position + 3])
                param_3_pos = positions[modus[2]]
                self.check_exists(param_3_pos)

            if opcode == 1:
                self.program[param_3_pos] = param_1 + param_2
            elif opcode == 2:
                self.program[param_3_pos] = param_1 * param_2
            elif opcode == 3:
                self.program[param_1_pos] = in_value
            elif opcode == 4:
                output_values.append(self.program[param_1_pos])
                # print(f'OUTPUT {output_values[-1]} at Position {self.position}')
                if len(output_values) == 2:
                    self.position += step
                    return output_values
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

with open('input.txt', 'r') as f:
    base_program = [int(n) for n in f.readline().split(',')]

def turn(face, direction, pos):
    directions = {0: (0, -1), 1: (1,0), 2: (0, 1), 3: (-1, 0)}
    turns = {0: -1, 1: 1}
    newface = (face + turns[direction]) % 4
    newx = pos[0] + directions[newface][0]
    newy = pos[1] + directions[newface][1]
    new_pos = (newx, newy)
    return newface, new_pos

computer = Computer(base_program)
panel = defaultdict(int)

robot_face = 0
robot_pos = (0,0)
panel[robot_pos] = 1

while True:
    new_color, direction = computer.run(panel[robot_pos])
    if new_color == 'HALT':
        break
    panel[robot_pos] = new_color
    robot_face, robot_pos = turn(robot_face, direction, robot_pos)

print ('PAINTED PANELS: ', len(panel))
# PAINTED PANELS:  2720

xvalues = [x for (x,y) in panel.keys()]
xmin, xmax = min(xvalues), max(xvalues)
yvalues = [y for (x,y) in panel.keys()]
ymin, ymax = min(yvalues), max(yvalues)

print(f'X {xmin}-{xmax}, Y {ymin}-{ymax}')

for row in range(ymax+1):
    for col in range(xmax+1):
        char = '*' if panel[col, row] == 1 else ' '
        print(char, ' ', end='')
    print()

# JZPJRAGJ

#          *  *     *  *  *  *     *  *  *              *  *     *  *  *           *  *           *  *              *  *
#             *              *     *        *              *     *        *     *        *     *        *              *
#             *           *        *        *              *     *        *     *        *     *                       *
#             *        *           *  *  *                 *     *  *  *        *  *  *  *     *     *  *              *
#    *        *     *              *              *        *     *     *        *        *     *        *     *        *
#       *  *        *  *  *  *     *                 *  *        *        *     *        *        *  *  *        *  *

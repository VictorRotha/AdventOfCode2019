from collections import defaultdict

class Computer:
    def __init__(self, program, panel):
        self.program = program.copy()
        self.panel = panel
        self.position = 0
        self.base = 0

    def run(self):
        output_values = []
        ticks = 0
        param_1, param_2 = None, None
        param_3_pos, param_1_pos, param_2_pos = None, None, None
        while True:
            instruction = self.program[self.position]
            opcode = instruction % 100
            modus = [((instruction // 10 ** i) % 10) for i in range(2,5)]
            if opcode == 99:
                print(f'HALT at Position {self.position}')
                _, _, score = self.apply_outputs(output_values)
                # self.panel_print()
                print(f'GAME OVER! \nTOTAL SCORE: {score}\nTICKS: {ticks}')
                return
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
                playerx, ballx, _ = self.apply_outputs(output_values)
                output_values = []

                # choice = input('JOYSTICK: ')
                # choices = {'1':-1, '3':1}
                # if choice in choices:
                #     in_value = choices[choice]
                # else:
                #     in_value = 0

                # time.sleep(0.1)
                # self.panel_print()

                if playerx < ballx:
                    in_value = 1
                elif playerx > ballx:
                    in_value = -1
                else:
                    in_value = 0

                self.program[param_1_pos] = in_value
                ticks += 1

            elif opcode == 4:
                output_values.append(self.program[param_1_pos])
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

    def panel_print(self):
        for row in self.panel:
            for column in row:
                char = '.' if column == 0 else column
                print (char, end=' ')
            print()

    def apply_outputs(self, output):
        play_x, ball_x, score = 0, 0, 0
        for n in range(0, len(output), 3):
            x, y, tile = output[n:n+3]
            if (x, y) == (-1,0):
                score = tile
            else:
                if tile == 3:
                    play_x = x
                if tile == 4:
                    ball_x = x
                self.panel[y][x] = tile
        return play_x, ball_x, score

base_program = defaultdict(int)
with open('input.txt', 'r') as f:
    for k, n in enumerate(f.readline().split(',')):
        base_program[k] = int(n)

base_program[0] = 2

xmax, ymax = 38, 22
panel = [[0]*xmax for _ in range(ymax)]

computer = Computer(base_program, panel)
computer.run()

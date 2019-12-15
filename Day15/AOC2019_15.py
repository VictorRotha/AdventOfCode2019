from collections import defaultdict
import networkx as nx

class Computer:
    def __init__(self, program):
        self.program = program.copy()
        self.position = 0
        self.base = 0

    def run(self, in_value):
        output_value = None
        param_1, param_2 = None, None
        param_3_pos, param_1_pos, param_2_pos = None, None, None
        while True:
            instruction = self.program[self.position]
            opcode = instruction % 100
            modus = [((instruction // 10 ** i) % 10) for i in range(2,5)]
            if opcode == 99:
                print(f'HALT at Position {self.position}')
                return output_value
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
                self.program[param_1_pos] = in_value
            elif opcode == 4:
                output_value = self.program[param_1_pos]
                self.position += step
                return output_value
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
    for k, n in enumerate(f.readline().split(',')):
        base_program[k] = int(n)

computer = Computer(base_program)

directions = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}
backwards = {1: 2, 2: 1, 3: 4, 4: 3}

seen = set()
pos = (0, 0)
target = None
seen.add(pos)

way = set()
way.add(pos)

def makemap(last=0):
    global pos, target
    for direction in range(1,5):
        x, y = pos
        dx, dy = directions[direction]
        new_pos = (x+dx, y+dy)
        if new_pos not in seen:
            output = computer.run(direction)
            if output == 0:
                seen.add(new_pos)
                continue
            else:
                seen.add(new_pos)
                way.add(new_pos)
                if output == 2:
                    target = new_pos
                pos = new_pos
                makemap(direction)
    if pos != (0,0):
        computer.run(backwards[last])
        x, y = pos
        dx, dy = directions[backwards[last]]
        pos = (x+dx, y+dy)

makemap()

print ('TARGET: ', target)

graph = nx.Graph()

for (x, y) in way:
    graph.add_node((x,y))
    for direction in range(1,5):
        dx, dy = directions[direction]
        neighbour = (x+dx, y+dy)
        if neighbour in way:
            graph.add_edge((x,y), neighbour)

dijkstra = nx.shortest_path_length(graph, (0,0), target)
oxy = nx.eccentricity(graph, target)

print ('Shortest Path: ', dijkstra)
print ('OXY TIME', oxy)

# TARGET:  (14, -20)
# Shortest Path:  282
# OXY TIME 286

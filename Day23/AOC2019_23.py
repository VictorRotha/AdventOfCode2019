from Intcode import Computer
from collections import defaultdict

def computers_init():
    computers = []
    for i in range(50):
        computer = Computer(base_program, i)
        computer.input_queue.append(i)
        computers.append(computer)
    return computers

base_program = defaultdict(int)
with open('input.txt', 'r') as f:
    for n, x in enumerate(f.readline().strip().split(',')):
        base_program[n] = int(x)

# PART 01
computers = computers_init()

twofivefive = False
while not twofivefive:
    for computer in computers:
        packet = computer.run()
        if packet is None:
            continue
        target, x, y = packet
        if target == 255:
            print('PART 01 ADDRESS 255', packet)
            twofivefive = True
            break
        computers[target].input_queue.extend([x, y])
# PART 01 ADDRESS 255 [255, 14593, 18966]

# PART 02
computers = computers_init()

NAT = []
NATY = []

loop = True
while loop:
    all_idle = True
    for computer in computers:
        if computer.input_queue:
            all_idle = False
        packet = computer.run()
        if packet is not None:
            all_idle = False
            target, x, y = packet
            if target == 255:
                NAT = [x, y]
            else:
                computers[target].input_queue.extend([x, y])

    if all_idle:
        # print('IDLE', NAT, len(NATY))
        computers[0].input_queue.extend(NAT)
        NATY.append(NAT[1])
        if len(NATY) >= 2 and NATY[-1] == NATY[-2]:
            print('PART 02 DOUBLE Y', NATY[-2:])
            loop = False

# PART 02 DOUBLE Y [14370, 14370]

import itertools


with open('input.txt', 'r') as f:
    base_program = [int(n) for n in f.readline().split(',')]

def intcode(phase, in_value):
    position = 0
    output_value = None
    program = base_program.copy()
    while True:
        instruction = program[position]
        opcode = instruction % 100
        modus = [instruction//10000, (instruction%10000)//1000, (instruction%1000)//100]
        if opcode not in (1,2,3,4,5,6,7,8,99):
            print (f'ERROR: Opcode {opcode} at Position {position}')
            break
        if opcode == 99:
            print ('Position: ', position, 'HALT', 'output', output_value)
            return output_value
            # break
        param_1 = program[program[position + 1]] if modus[2] == 0 else program[position + 1]
        # print('Position ', position, 'opcode ', opcode, output_value)
        if opcode in (1, 2, 5, 6, 7, 8):
            param_2 = program[program[position + 2]] if modus[1] == 0 else program[position + 2]
        if opcode == 1:
            program[program[position + 3]] = param_1 + param_2
            position += 4
        elif opcode == 2:
            program[program[position + 3]] = param_1 * param_2
            position += 4
        elif opcode == 3:
            if position == 0:
                program[program[position + 1]] = phase
            else:
                program[program[position + 1]] = in_value
            # print ('Position ', position, 'opcode ', opcode)
            position += 2
        elif opcode == 4:
            output_value = program[program[position+1]] if modus[2] == 0 else program[position+1]
            return output_value
            # print('Position: ', position, 'Output:',  output_value)
            position += 2
        elif opcode == 5:
            position = param_2 if param_1 != 0 else position + 3
        elif opcode == 6:
            position = param_2 if param_1 == 0 else position + 3
        elif opcode == 7:
            program[program[position + 3]] = 1 if param_1 < param_2 else 0
            position += 4
        elif opcode == 8:
            program[program[position + 3]] = 1 if param_1 == param_2 else 0
            position += 4



perms = itertools.permutations(range(5), 5)
outputs = []
for perm in perms:
    input_value = 0
    for ph in perm:
        input_value = intcode(ph, input_value)
    outputs.append(input_value)

print ('MAX OUTPUT: ', max(outputs))





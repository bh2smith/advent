from utils.op_codes import ops


if __name__ == '__main__':
    calls, codes = [], []
    with open('data/day19') as text_file:
        lines = text_file.readlines()
        ip = int(lines[0].strip()[-1])
        for line in lines[1:]:
            line = line.strip().split()
            calls.append(line[0])
            codes.append(list(map(int, line[1:])))

    # Part 1
    registers = [0, 0, 0, 0, 0, 0]
    cmds = list(zip(calls, codes))
    c = 0
    while registers[ip] < len(cmds):
        op = cmds[registers[ip]][0]
        x, y, z = cmds[registers[ip]][1]
        registers = ops[op](x, y, z, registers)
        registers[ip] = registers[ip] + 1

    print(registers[0])

    # Part 2
    registers = [1, 0, 0, 0, 0, 0]
    while registers[ip] != 1:
        op = cmds[registers[ip]][0]
        x, y, z = cmds[registers[ip]][1]
        registers = ops[op](x, y, z, registers)
        registers[ip] = registers[ip] + 1

    # Once registers[ip] == 1 register[0] will eventually be
    # the sum of divisors of register[-1]
    n = registers[-1]
    print(sum([i for i in range(1, n + 1) if n % i == 0]))

from utils.op_codes import ops


def print_stuff():
    print(
        op,
        str(x).ljust(3, ' '),
        str(y).ljust(9, ' '),
        str(z).ljust(3, ' '),
        '|',
        ', '.join(map(lambda t: str(t).ljust(13, ' '), registers)),
        registers
    )


if __name__ == '__main__':
    calls, codes = [], []
    with open('data/day21') as text_file:
        lines = text_file.readlines()
        ip = int(lines[0].strip()[-1])
        for line in lines[1:]:
            line = line.strip().split()
            calls.append(line[0])
            codes.append(list(map(int, line[1:])))

    cmds = list(zip(calls, codes))
    for i in range(1, 2):
        registers = [11827870, 0, 0, 0, 0, 0]
        too_low = 10839268
        too_high = 12816351
        Wrong = [12546350, 12816238, 12802212]
        c = 0
        L = [
            11385447, # NO
            11385544, # NO
            11827753, # NO11827870, 11861344, 11861583, 11959551, 11959626,
            12372919,
         12373162, 12546350, 12587510, 12763252, 12763297, 12802212, 12816238]
        s = set()
        while registers[ip] < len(cmds) and c < 10000000:

            op = cmds[registers[ip]][0]
            x, y, z = cmds[registers[ip]][1]
            # print_stuff()
            temp = registers[1]
            registers = ops[op](x, y, z, registers)
            if registers[1] != temp:
                # print("registers changed", temp, registers[1])
                s.add(registers[1])
            registers[ip] = registers[ip] + 1
            c += 1
        print(sorted([x for x in s if 10839268 < x < 12816351]))
        print(c)
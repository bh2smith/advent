from collections import defaultdict

m = 65536
ops = {
    'AND': lambda x, y: (x & y) % m,
    'OR': lambda x, y: (x | y) % m,
    'LSHIFT': lambda x, y: (x << y) % m,
    'RSHIFT': lambda x, y: (x >> y) % m
}


def parse(line):
    if len(line) == 3:
        try:
            wires[line[-1]] = int(line[0])
        except ValueError:
            if line[0] in wires:
                wires[line[-1]] = wires[line[0]]
    elif len(line) == 5:
        if 'SHIFT' in line[1]:
            if line[0] in wires:
                a, b = wires[line[0]], int(line[2])
                wires[line[-1]] = ops[line[1]](a, b)
        else:
            try:
                a = int(line[0])
                if line[2] in wires:
                    wires[line[-1]] = ops[line[1]](a, wires[line[2]])
            except ValueError:
                if line[0] in wires and line[2] in wires:
                    a, b = wires[line[0]], wires[line[2]]
                    wires[line[-1]] = ops[line[1]](a, b)
    else:
        if line[1] in wires:
            wires[line[-1]] = ~wires[line[1]] % m


if __name__ == '__main__':
    unused = []
    with open('input') as file:
        lines = file.readlines()
        for li in lines:
            li = li.strip().split()
            unused.append(tuple(li))

    wires = defaultdict(int)
    while 'a' not in wires:
        for u in unused:
            parse(u)

    print("part 1:", wires['a'])

    temp = wires['a']
    wires = defaultdict(int)
    while 'a' not in wires:
        for u in unused:
            # Force b to have value of result from part a
            wires['b'] = temp
            parse(u)

    print("part 2:", wires['a'])

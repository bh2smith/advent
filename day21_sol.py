from utils.op_codes import ops


def print_stuff(op, x, y, z, r):
    print(
        op,
        str(x).ljust(9, ' '),
        str(y).ljust(9, ' '),
        str(z).ljust(3, ' '),
        '|',
        ', '.join(map(lambda t: str(t).ljust(13, ' '), r)),
        r
    )


def do_it_slow(r, upper_bound=10**8):
    c = 0
    while r[ip] < len(cmds) and c < upper_bound:
        op = cmds[r[ip]][0]
        x, y, z = cmds[r[ip]][1]
        r = ops[op](x, y, z, r)
        r[ip] = r[ip] + 1
        c += 1
    return c if c < upper_bound else None


def do_it(r, upper_bound=10**10):
    first, last, c, s = 0, 0, 0, set()
    while r[ip] < len(cmds) and c < upper_bound:
        if r[ip] == 25:
            d = r[2] // 256
            r = r[:3] + [d + 1, 19, d]
            c += (d - 1) * 7 + 2
        else:
            op = cmds[r[ip]][0]
            x, y, z = cmds[r[ip]][1]
            r = ops[op](x, y, z, r)
            r[ip] = r[ip] + 1
            c += 1
        if r[ip] == 28:
            if not s:
                first = r[1]
            if r[1] not in s:
                last = r[1]
                s.add(r[1])

    return s, first, last


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

    candidates, part1, part2 = do_it([1, 0, 0, 0, 0, 0])
    print("part 1:", part1)
    print("part 2:", part2)

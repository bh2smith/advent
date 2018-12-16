def addr(a, b, c, reg):
    res = [r for r in reg]
    res[c] = res[a] + res[b]
    return res


def addi(a, b, c, reg):
    res = [r for r in reg]
    res[c] = res[a] + b
    return res


def mulr(a, b, c, reg):
    res = [r for r in reg]
    res[c] = res[a] * res[b]
    return res


def muli(a, b, c, reg):
    res = [r for r in reg]
    res[c] = res[a] * b
    return res


def banr(a, b, c, reg):
    res = [r for r in reg]
    res[c] = res[a] & res[b]
    return res


def bani(a, b, c, reg):
    res = [r for r in reg]
    res[c] = res[a] & b
    return res


def borr(a, b, c, reg):
    res = [r for r in reg]
    res[c] = res[a] | res[b]
    return res


def bori(a, b, c, reg):
    res = [r for r in reg]
    res[c] = res[a] | b
    return res


def setr(a, b, c, reg):
    res = [r for r in reg]
    res[c] = res[a]
    return res


def seti(a, b, c, reg):
    res = [r for r in reg]
    res[c] = a
    return res


def gtir(a, b, c, reg):
    res = [r for r in reg]
    res[c] = 1 if a > res[b] else 0
    return res


def gtri(a, b, c, reg):
    res = [r for r in reg]
    res[c] = 1 if res[a] > b else 0
    return res


def gtrr(a, b, c, reg):
    res = [r for r in reg]
    res[c] = 1 if res[a] > res[b] else 0
    return res


def eqir(a, b, c, reg):
    res = [r for r in reg]
    res[c] = 1 if a == res[b] else 0
    return res


def eqri(a, b, c, reg):
    res = [r for r in reg]
    res[c] = 1 if res[a] == b else 0
    return res


def eqrr(a, b, c, reg):
    res = [r for r in reg]
    res[c] = 1 if res[a] == res[b] else 0
    return res


ops = {
    'addr': addr,
    'addi': addi,
    'mulr': mulr,
    'muli': muli,
    'banr': banr,
    'bani': bani,
    'borr': borr,
    'bori': bori,
    'setr': setr,
    'seti': seti,
    'gtir': gtir,
    'gtri': gtri,
    'gtrr': gtrr,
    'eqir': eqir,
    'eqri': eqri,
    'eqrr': eqrr,
}


def load_part2():
    op_calls = []
    with open('data/day16part2') as text_file:
        lines = text_file.readlines()
        for line in lines:
            op_calls.append(list(map(int, line.strip().split())))

    return op_calls


def part1():
    transitions, codes = [], []
    with open('data/day16') as text_file:
        lines = text_file.readlines()
        for i in range(0, len(lines), 4):
            b = list(map(int, lines[i].strip()[9:-1].split(',')))
            a = list(map(int, lines[i+2].strip()[9:-1].split(',')))
            transitions.append((b, a))
            codes.append(list(map(int, lines[i + 1].strip().split())))

    possibilities = {op: set() for op in ops}
    ans = 0
    for transition, code in zip(transitions, codes):
        before = transition[0]
        after = transition[1]
        count = 0
        for s in ops:
            if ops[s](code[1], code[2], code[3], before) == after:
                possibilities[s].add(code[0])
                count += 1

        if count >= 3:
            ans += 1

    return ans, possibilities


if __name__ == '__main__':
    part1_answer, poss = part1()
    print(part1_answer)

    reduced_possibilities = {}
    while len(reduced_possibilities.keys()) < 16:
        for p in poss:
            if len(poss[p]) == 1:
                found = poss[p].pop()
                reduced_possibilities[found] = p
                for op in poss:
                    if found in poss[op]:
                        poss[op].remove(found)

    data = load_part2()
    register = [0, 0, 0, 0]
    for op_call in data:
        function = reduced_possibilities[op_call[0]]
        x, y, z = op_call[1:]

        register = ops[function](x, y, z, register)

    print(register[0])

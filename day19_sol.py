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


def factors(n):
    if n == 1:
        return [1]
    for i in range(2, n):
        if n % i == 0:
            return [i] + factors(n//i)
    return [n]


def divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]


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
    n = 10551276
    print(sum(divisors(n)))






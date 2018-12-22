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
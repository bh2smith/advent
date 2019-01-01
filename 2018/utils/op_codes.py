def addr(a, b, c, r):
    r[c] = r[a] + r[b]
    return r


def addi(a, b, c, r):
    r[c] = r[a] + b
    return r


def mulr(a, b, c, r):
    r[c] = r[a] * r[b]
    return r


def muli(a, b, c, r):
    r[c] = r[a] * b
    return r


def banr(a, b, c, r):
    r[c] = r[a] & r[b]
    return r


def bani(a, b, c, r):
    r[c] = r[a] & b
    return r


def borr(a, b, c, r):
    r[c] = r[a] | r[b]
    return r


def bori(a, b, c, r):
    r[c] = r[a] | b
    return r


def setr(a, b, c, r):
    r[c] = r[a]
    return r


def seti(a, b, c, r):
    r[c] = a
    return r


def gtir(a, b, c, r):
    r[c] = 1 * (a > r[b])
    return r


def gtri(a, b, c, r):
    r[c] = 1 * (r[a] > b)
    return r


def gtrr(a, b, c, r):
    r[c] = 1 if r[a] > r[b] else 0
    return r


def eqir(a, b, c, r):
    r[c] = 1 * (a == r[b])
    return r


def eqri(a, b, c, r):
    r[c] = 1 * (r[a] == b)
    return r


def eqrr(a, b, c, r):
    r[c] = 1 * (r[a] == r[b])
    return r


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
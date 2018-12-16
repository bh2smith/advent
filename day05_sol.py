
def s_reduce(st):
    for i in range(len(st) - 1):
        if (st[i] != st[i+1]) and (st[i].lower() == st[i+1].lower()):
            return st[:i] + st[i+2:]
    return st


def part1():
    while len(s) != len(s_reduce(s)):
        s = s_reduce(s)

    return len(s)


def part2():
    letters = set(l.lower() for l in s)

    mn = len(s) + 1
    for letter in letters:
        l, u = letter.lower(), letter.upper()
        new_s = s.replace(l, '').replace(u, '')
        while len(new_s) != len(s_reduce(new_s)):
            new_s = s_reduce(new_s)
        if len(new_s) < mn:
            mn = len(new_s)
            ans = len(new_s)
    return ans


if __name__ == '__main__':
    s = ''
    with open('data/day05') as f:
        s += f.readlines()[0]

    print(part1())
    print(part2())

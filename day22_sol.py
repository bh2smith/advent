types = {
    'rocky': 0,
    'narrow': 1,
    'wet': 2
}

pic = {
    0: '.',
    1: '=',
    2: '|'
}

depth = 4848
target = (15, 700)

m = 20183


def index(x, y, memo={(0, 0): 0, (15, 700): 0}):
    if (x, y) in memo:
        return memo[(x, y)]
    if y == 0:
        memo[(x, 0)] = x * 16807
    elif x == 0:
        memo[(0, y)] = y * 48271
    else:
        memo[(x, y)] = erosion_level(x - 1, y) * erosion_level(x, y - 1)
    return memo[(x, y)]


def erosion_level(x, y):
    return (depth + index(x, y)) % m


if __name__ == '__main__':
    risk = []
    for i in range(target[0] + 1):
        new = []
        for j in range(target[1] + 1):
            new.append(erosion_level(i, j) % 3)
        risk.append(new)

    print(sum(sum(r) for r in risk))



def load_data():
    with open('data/day18') as tf:
        grid = []
        for line in tf.readlines():
            grid.append([ch for ch in line.strip()])
    return grid


def print_grid(grid):
    print('-'*len(grid[0]))
    for g in grid:
        print(''.join(g))
    print('-' * len(grid[0]))


def udlr(t, k, grid):
    res = []
    n, s, w, e = (t-1, k), (t+1, k), (t, k-1), (t, k+1)
    nw, ne, se, sw = (t-1, k-1), (t-1, k+1), (t+1, k+1), (t+1, k-1)
    for p in {n, s, w, e, nw, ne, se, sw}:
        if p[0] >= 0 and p[1] >= 0:
            try:
                res.append(grid[p[0]][p[1]])
            except IndexError:
                pass
    return res


def evolve(grid):
    new = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            surroundings = udlr(i, j, grid)
            if grid[i][j] == '#':
                if surroundings.count('#') >= 1 and surroundings.count('|') >= 1:
                    new[i][j] = '#'
                else:
                    new[i][j] = '.'
            elif grid[i][j] == '|' and surroundings.count('#') >= 3:
                new[i][j] = '#'
            elif grid[i][j] == '.' and surroundings.count('|') >= 3:
                new[i][j] = '|'
            else:
                new[i][j] = grid[i][j]
    return new


if __name__ == '__main__':
    gr = load_data()

    for i in range(10):
        # print_grid(gr)
        gr = evolve(gr)
        # print_grid(gr)

    lumberyards = trees = 0
    for g in gr:
        lumberyards += g.count('#')
        trees += g.count('|')
    print(lumberyards * trees)

    # Result of computing lumberyards * trees
    # for each i and recognizing the sequence repeats at 572 with
    r = [
        102850,
        105000,
        107068,
        108864,
        109152,
        110208,
        110396,
        109347,
        107912,
        106477,
        106134,
        103076,
        97578,
        95550,
        94656,
        93612,
        92649,
        92115,
        90816,
        89180,
        88400,
        86445,
        84500,
        83328,
        82992,
        83239,
        83415,
        82992,
        83824,
        84750,
        87032,
        87897,
        92160,
        95526,
        98580,
    ]

    print(r[(10**9 - 572) % len(r)])



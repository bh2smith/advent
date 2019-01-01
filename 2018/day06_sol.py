def dist(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def count_occurrences(v, arr):
    res = 0
    for a in arr:
        res += a.count(v)
    return res


def part1():
    for i in range(x_max):
        for j in range(y_max):
            d = []
            for c in coordinates:
                d.append(dist(c, (i, j)))
            m = min(d)
            if d.count(m) <= 1:
                grid[i][j] = d.index(m)
            else:
                grid[i][j] = 0

    infinite = set(grid[0]+grid[-1])
    for g in grid:
        infinite.add(g[0])
        infinite.add(g[-1])

    inner = [i for i in range(len(coordinates)) if i not in infinite]

    return max([count_occurrences(i, grid) for i in inner])


def part2():
    for i in range(x_max):
        for j in range(y_max):
            v = sum([dist(c, (i, j)) for c in coordinates])
            if v < 10000:
                grid[i][j] = -1
    return count_occurrences(-1, grid)


if __name__ == '__main__':
    coordinates = []
    with open('data/day06') as f:
        lines = f.readlines()
        for line in lines:
            coordinates.append(list(map(int, line.strip().split(', '))))

    x_max = max([point[0] for point in coordinates])
    y_max = max([point[1] for point in coordinates])

    grid = [[0 for _ in range(y_max)] for _ in range(x_max)]

    print(part1())
    print(part2())

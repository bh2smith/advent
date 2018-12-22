from collections import defaultdict
import sys

sys.setrecursionlimit(2900)


def load_data():
    with open('data/day17') as text_file:
        dx, dy = defaultdict(list), defaultdict(list)
        m_x, m_y = -1, -1
        offset_x, offset_y = 10 ** 5, 10 ** 5

        lines = text_file.readlines()
        for line in lines:
            a, b = line.strip().split(', ')
            v = int(a[2:])
            l, r = list(map(int, (b[2:].split('..'))))
            if a[0] == 'x':
                dx[v].append((l, r))
                if r > m_y:
                    m_y = r
                if v > m_x:
                    m_x = v
                if v < offset_x:
                    offset_x = v

            else:
                dy[v].append((l, r))
                if r > m_x:
                    m_x = r
                if v > m_y:
                    m_y = v
                if l < offset_x:
                    offset_x = l

    grid = [['.' for _ in range(m_x + 1)] for _ in range(m_y + 1)]
    for x in dx:
        for (l, r) in dx[x]:
            for t in range(l, r + 1):
                grid[t][x] = '#'

    for y in dy:
        for (l, r) in dy[y]:
            for t in range(l, r + 1):
                grid[y][t] = '#'

    return grid, offset_x, m_y


def print_grid(grid, offset_x=0):
    print('-' * (len(grid[0]) - offset_x))
    for row in grid:
        print(''.join(row[offset_x:]))
    print('-' * (len(grid[0]) - offset_x))


def has_wall(grid, point, x_off=1):
    x, y = point
    curr_x = x
    while 1:
        if grid[y][curr_x] == '.':
            return False
        if grid[y][curr_x] == '#':
            return True
        curr_x += x_off


def has_both_walls(grid, point):
    return has_wall(grid, point, 1) and has_wall(grid, point, -1)


def fill_side(grid, point, x_off=1):
    x, y = point
    curr_x = x
    while 1:
        if grid[y][curr_x] == '#':
            return
        grid[y][curr_x] = '~'
        curr_x += x_off


def fill(grid, point):
    fill_side(grid, point, 1), fill_side(grid, point, -1)


def drip(grid, point, m_y):
    x, y = point
    if y >= m_y:
        return
    if grid[y + 1][x] == '.':
        grid[y + 1][x] = '|'
        drip(grid, [x, y + 1], m_y)

    if grid[y + 1][x] in '#~' and grid[y][x + 1] == '.':
        grid[y][x + 1] = '|'
        drip(grid, [x + 1, y], m_y)

    if grid[y + 1][x] in '#~' and grid[y][x - 1] == '.':
        grid[y][x - 1] = '|'
        drip(grid, [x - 1, y], m_y)

    if has_both_walls(grid, [x, y]):
        fill(grid, [x, y])


if __name__ == '__main__':
    gr, off_x, max_y = load_data()

    # print_grid(gr, off_x - 1)
    drip(gr, [500, 0], max_y)
    # print_grid(gr, off_x - 1)

    print(sum([g.count('~') + g.count('|') for g in gr]) - 4)  # There were 4 above the last #

    print(sum([g.count('~') for g in gr]))

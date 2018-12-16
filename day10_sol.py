import sys


def area(a, b):
    return abs(b[0] - a[0]) * abs(b[1] - a[1])


def get_bounds(arr):
    slices = [a[0] for a in arr], [a[1] for a in arr]
    return min(slices[0]), min(slices[1]), max(slices[0]), max(slices[1])


def move(k):
    new_points = []
    for p, v in zip(points, speeds):
        new_p = [p[0] + (k * v[0]), p[1] + (k * v[1])]
        new_points.append(new_p)
    return new_points


if __name__ == '__main__':
    points = []
    speeds = []
    max_x = max_y = -1
    min_x = min_y = sys.maxsize

    with open('data/day10') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().replace('position', '').replace('velocity', '')
            line = line.split('=')
            points.append(list(map(int, line[1].strip()[1:-1].split(','))))
            speeds.append(list(map(int, line[-1][1:-1].strip().split(','))))

    # Number of moves resulting in smallest square area
    bounds = get_bounds(points)
    init_area = area(bounds[:2], bounds[2:])
    prev_a = init_area
    count = 0
    while 1:
        prev_points = points
        points = move(1)
        bounds = get_bounds(points)
        next_a = area(bounds[:2], bounds[2:])
        if next_a > prev_a:
            break
        prev_a = next_a
        count += 1

    points = prev_points

    min_x, min_y, max_x, max_y = map(abs, get_bounds(points))

    board = [['.' for _ in range(min_x + max_x + 1)] for _ in range(min_y + max_y + 1)]
    for p in points:
        board[p[1]][p[0]] = '#'

    # Part 1
    for row in board[382:]:
        print(' '.join(row[286:]))

    # Part 2
    print(count)


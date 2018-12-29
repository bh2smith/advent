def dist(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1]) + abs(p[2] - q[2])


def range_overlap(x, y):
    return dist(x, y) <= pts[x] + pts[y]


def furthest(point_set):
    m = -1
    res = None
    for p in point_set:
        for q in point_set:
            if dist(p, q) > m:
                m = dist(p, q)
                res = (p, q)
    return res


if __name__ == '__main__':
    pts = {}
    max_r, best_bot = -1, None
    with open('data/day23test2') as f:
        for line in f.readlines():
            line = line.strip().replace('position', '').replace('radius', '')
            line = line.split('=')
            pt = tuple(map(int, line[1].strip()[1:-4].split(',')))
            r = int(line[-1])
            pts[pt] = r
            if r > max_r:
                max_r = r
                best_bot = pt

    print(len(set([q for q in pts.keys() if dist(best_bot, q) <= max_r])))

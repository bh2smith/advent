from collections import defaultdict


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
    max_r = -1
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

    intersections = defaultdict(set)
    points = list(pts.keys())
    unseen = set(points)
    lp = len(points)
    M = -1
    for i in range(len(points)-1):
        print(i, "-------------------------")
        p = points[i]
        for j in range(i+1, len(points)):
            q = points[j]
            if range_overlap(p, q):
                unseen = set(points) - {p, q}
                no_good = 0
                for z in unseen:
                    if range_overlap(p, z) and range_overlap(q, z):
                        intersections[(p, q)].add(z)
                    else:
                        no_good += 1
                    if no_good > lp - M:
                        break

            s = intersections[(p, q)]
            if len(s) >= M:
                M = len(s)
                print(M, p, q)
            else:
                del(intersections[(p, q)])

    # x = [
    #         [(-47975327, 6802988, 36544806), (-47629510, 2074458, 32801724)],
    #         [(-47975327, 6802988, 36544806), (-40802673, 7607684, 37116431)],
    #         [(-47975327, 6802988, 36544806), (-40099260, -1453200, 32884885)],
    #         [(-47975327, 6802988, 36544806), (-44206028, 8175853, 41925243)],
    #         [(-47629510, 2074458, 32801724), (-40802673, 7607684, 37116431)],
    #         [(-47629510, 2074458, 32801724), (-40099260, -1453200, 32884885)],
    #         [(-47629510, 2074458, 32801724), (-44206028, 8175853, 41925243)],
    #         [(-40802673, 7607684, 37116431), (-40099260, -1453200, 32884885)],
    #         [(-40802673, 7607684, 37116431), (-44206028, 8175853, 41925243)],
    #         [(-40099260, -1453200, 32884885), (-44206028, 8175853, 41925243)],
    #     ]

    x = [(p, q) for p, q in intersections if len(intersections[(p, q)]) == M]
    intersections = defaultdict(set)
    for p, q in x:
        unseen = set(points) - {p, q}
        for z in unseen:
            if range_overlap(p, z) and range_overlap(q, z):
                intersections[(p, q)].add(z)

    s = []
    for p, q in x:
        new_set = {p, q}.union(intersections[(p, q)])
        if new_set not in s:
            s.append(new_set)

    assert(len(s) == 1)
    s = s.pop()
    print(s)
    # want = complete_intersection(s)

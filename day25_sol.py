from utils.norms import manhattan


class Community:
    def __init__(self, first_member):
        self.members = {first_member}

    def merge(self, other):
        self.members |= other.members


if __name__ == '__main__':
    points = [
        tuple(map(int, l.strip().split(','))) for l in open('data/day25').readlines()
    ]
    num_points = len(points)
    constellations = {points[i]: Community(points[i]) for i in range(len(points))}
    i = 0
    while i < len(points) - 1:
        p = points[i]
        j = i + 1
        while j < len(points):
            q = points[j]
            if manhattan(p, q) <= 3:
                constellations[p].merge(constellations[q])
                constellations[q].merge(constellations[p])
            j += 1
        i += 1

    while 1:
        changed, i = 0, 0
        while i < len(points) - 1:
            p = points[i]
            j = i + 1
            while j < len(points):
                q = points[j]
                if constellations[q].members & constellations[p].members:
                    constellations[p].merge(constellations[q])
                    del constellations[q]
                    points.remove(q)
                    changed += 1
                j += 1
            i += 1
        if not changed:
            break

    disjoint_sets = []
    for p, com in constellations.items():
        if com.members not in disjoint_sets:
            disjoint_sets.append(com.members)

    assert (sum(len(s) for s in disjoint_sets) == num_points)
    print(len(disjoint_sets))

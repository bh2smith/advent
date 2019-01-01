# Solution inspired by:
# https://github.com/ypsu/experiments/tree/master/aoc2018day23
from sys import maxsize


class Sphere:
    def __init__(self, _x, _y, _z, _r):
        self.x = _x
        self.y = _y
        self.z = _z
        self.r = _r

    def __str__(self):
        s = "({x}, {y}, {z}) - {r}"
        return s.format(**self.__dict__)


class SearchBox:
    def __init__(self, _covered=0, _origin=0, _side=0, _x=0, _y=0, _z=0):
        self.covered = _covered
        self.origin = _origin
        self.side = _side
        self.x = _x
        self.y = _y
        self.z = _z

    def __str__(self):
        s = "({x}, {y}, {z}); {covered}, {origin}, {side}"
        return s.format(**self.__dict__)


def heap_entry(pa, pb):
    box_a, box_b = search_boxes[heap[pa]], search_boxes[heap[pb]]
    if box_a.covered != box_b.covered:
        return box_a.covered > box_b.covered
    if box_a.origin != box_b.origin:
        return box_a.origin < box_b.origin
    return box_a.side < box_b.side


def bubble_up():
    pos = heap_count
    while pos > 1 and heap_entry(pos, pos // 2):
        # swap
        temp = heap[pos // 2]
        heap[pos // 2] = heap[pos]
        heap[pos] = temp

        pos //= 2


def bubble_down():
    pos = 1
    while 2 * pos <= heap_count:
        swapos = 2 * pos
        if swapos + 1 <= heap_count and heap_entry(swapos + 1, swapos):
            swapos += 1
        if heap_entry(swapos, pos):
            # swap
            temp = heap[swapos]
            heap[swapos] = heap[pos]
            heap[pos] = temp

            pos = swapos
        else:
            break


def range_dist(p, lo, hi):
    if p < lo:
        return lo - p
    if p > hi:
        return p - hi
    return 0


def count_boxes(bx):
    assert (isinstance(bx, SearchBox))
    x1, x2 = bx.x, bx.x + bx.side - 1
    y1, y2 = bx.y, bx.y + bx.side - 1
    z1, z2 = bx.z, bx.z + bx.side - 1
    cnt = 0
    for bt in nano_bots:
        d = 0
        d += range_dist(bt.x, x1, x2)
        d += range_dist(bt.y, y1, y2)
        d += range_dist(bt.z, z1, z2)
        if d <= bt.r:
            cnt += 1
    box.covered = cnt


def dist(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1]) + abs(p[2] - q[2])


if __name__ == '__main__':
    pts = {}
    max_r, best_bot = -1, None
    nano_bots = []
    with open('data/day23') as f:
        for line in f.readlines():
            line = line.strip().replace('position', '').replace('radius', '')
            line = line.split('=')
            _x, _y, _z = tuple(map(int, line[1].strip()[1:-4].split(',')))
            r = int(line[-1])
            pts[(_x, _y, _z)] = r
            nano_bots.append(Sphere(_x, _y, _z, r))

            if r > max_r:
                max_r = r
                best_bot = (_x, _y, _z)

    print("part 1:", len(set([q for q in pts.keys() if dist(best_bot, q) <= max_r])))

    inf = maxsize
    min_x = min_y = min_z = inf
    max_x = max_y = max_z = -inf

    for bot in nano_bots:
        if bot.x - bot.r < min_x:
            min_x = bot.x - bot.r
        if bot.x + bot.r > max_x:
            max_x = bot.x + bot.r

        if bot.y - bot.r < min_y:
            min_y = bot.y - bot.r
        if bot.y + bot.r > max_y:
            max_y = bot.y + bot.r

        if bot.z - bot.r < min_z:
            min_z = bot.z - bot.r
        if bot.z + bot.r > max_z:
            max_z = bot.z + bot.r
    limit = 1020
    heap = [None] * limit**2
    search_boxes = [SearchBox() for _ in range(limit**2)]
    box_count = 1
    box = search_boxes[box_count]

    box.x = min_x
    box.y = min_y
    box.z = min_z
    box.origin = abs(box.x) + abs(box.y) + abs(box.z)
    le = 1
    while box.x + le < max_x or box.y + le < max_y or box.z + le < max_z:
        le *= 2
    box.side = le
    count_boxes(box)

    heap[1] = 1
    heap_count, processed = 1, 0
    while heap_count:
        processed += 1
        qbox = search_boxes[heap[1]]
        heap_count -= 1
        heap[1] = heap[heap_count]
        bubble_down()
        if qbox.side == 1:
            print("part 2:", qbox.origin)
            break

        new_side = qbox.side // 2

        x = qbox.x
        for a in range(2):
            y = qbox.y
            for b in range(2):
                z = qbox.z
                for c in range(2):
                    heap[heap_count + 1] = box_count
                    box = search_boxes[box_count]

                    box.x, box.y, box.z = x, y, z
                    box.side = new_side
                    box.origin = abs(box.x) + abs(box.y) + abs(box.z)
                    count_boxes(box)

                    if box.covered:
                        heap_count += 1
                        box_count += 1
                        bubble_up()

                    z += new_side
                y += new_side
            x += new_side

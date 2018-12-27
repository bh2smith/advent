import sys
from collections import defaultdict

types = {0: 'rocky', 1: 'wet', 2: 'narrow', }
items = {0: {'torch', 'climbing'}, 1: {'neither', 'climbing'}, 2: {'torch', 'neither'}}
pic = {0: '.', 1: '=', 2: '|'}

depth = 4848
target = (15, 700)


def index(x, y, memo={(0, 0): 0, target: 0}):
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
    return (depth + index(x, y)) % 20183


class Node:
    def __init__(self, _val, _x, _y, _tool):
        self.value = _val
        self.tool = _tool
        self.location = _x + _y * 1j

    def __str__(self):
        return "{location}: {value}-{tool}".format(**self.__dict__)

    def is_adjacent(self, other):
        if self.location == other.location:
            return True
        if other.tool != self.tool:
            return False
        loc = self.location
        return other.location in {loc + 1j, loc - 1j, loc + 1, loc - 1}

    def length(self, other):
        assert (self.is_adjacent(other))
        if self.location == other.location:
            return 7
        return 1


class Graph:
    def __init__(self):
        self.vertices = set()
        self.v_map = defaultdict(set)

    def add_node(self, x):
        self.v_map[x.location].add(x)
        self.vertices.add(x)

    def neighbours(self, x):
        adjacent = set()
        for v in self.v_map[x.location]:
            if v != x:
                adjacent.add(v)

        loc = x.location
        for a in {loc + 1j, loc - 1j, loc + 1, loc - 1}:
            for v in self.v_map[a]:
                if v.tool == x.tool:
                    adjacent.add(v)
        return adjacent


def dijkstra(graph, source):
    unseen = set()
    dist, prev = {}, {}
    for v in graph.vertices:
        dist[v] = sys.maxsize
        prev[v] = None
        unseen.add(v)
    dist[source] = 0

    while unseen:
        u = min(unseen, key=lambda w: dist[w])
        unseen.remove(u)
        for n in graph.neighbours(u) & unseen:
            alt = dist[u] + u.length(n)
            if alt < dist[n]:
                dist[n] = alt
                prev[n] = u
    return dist, prev


def get_path(prev, finish):
    res, curr = [], finish
    while prev[curr]:
        res.append(curr)
        curr = prev[curr]
    if res:
        res.append(curr)
    return res[::-1]


if __name__ == '__main__':
    risk = 0
    for i in range(target[0] + 1):
        risk += sum([erosion_level(i, j) % 3 for j in range(target[1] + 1)])
    print("part1:", risk)

    g = Graph()
    start, end = None, None
    for i in range(target[0] + 5):
        for j in range(target[1] + 5):
            value = erosion_level(i, j) % 3
            for item in items[value]:
                node = Node(value, i, j, item)
                if (i, j) == (0, 0) and item == 'torch':
                    start = node
                elif (i, j) == target and item == 'torch':
                    end = node
                g.add_node(node)

    print("part2:", dijkstra(g, start)[0][end])

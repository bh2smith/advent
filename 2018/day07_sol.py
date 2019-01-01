from collections import defaultdict

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def part1():
    # Nodes (sorted) with no incoming edges
    s = set([x[0] for x in edges]).difference(set([x[1] for x in edges]))
    s = sorted(list(s))

    graph = defaultdict(list)
    for e in edges:
        graph[e[0]].append(e[1])
    # (ordered) Topological sort
    res = []
    while s:
        n = s.pop(0)
        res.append(n)
        while graph[n]:
            m = graph[n].pop()
            remaining = []
            for x in graph:
                if x != n:
                    remaining += graph[x]
            if m not in set(remaining):
                s.append(m)
                s.sort()
    return res


def part2(task_order, offset, num_workers):
    inv_g = defaultdict(list)
    for e in edges:
        inv_g[e[1]].append(e[0])

    times = {a: offset + (i + 1) for i, a in enumerate(alphabet)}
    remaining = task_order
    in_progress = defaultdict(int)
    done, time = set(), 0

    while remaining:
        next_candidates = [
            r for r in remaining if set(inv_g[r]).issubset(done) or not set(inv_g[r])]
        while len(in_progress.keys()) < num_workers and next_candidates:
            next_c = next_candidates.pop(0)
            in_progress[next_c] = times[next_c]
            remaining.remove(next_c)

        # fast-forward
        increase = min(in_progress.values())
        time += increase
        for task in in_progress:
            in_progress[task] -= increase

        completed = set([t for t in in_progress if in_progress[t] == 0])
        done |= completed
        for c in completed:
            del (in_progress[c])

    return time


if __name__ == '__main__':
    edges = []
    with open('data/day07') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split()
            edges.append((line[1], line[-3]))

    ans = part1()
    print(''.join(ans))
    print(part2(ans, 60, 5))

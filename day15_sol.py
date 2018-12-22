from collections import defaultdict


def udlr(player):
    x, y = player[:2]
    up, down, left, right = (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)

    return {up, down, left, right}.intersection(free)


def dist(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def opponents(player):
    pt = player[2]
    return [
        p for p in players
        if p[2] == 'E' * (pt == 'G') + 'G' * (pt == 'E') and p[3] > 0
    ]


def adjacent_opponents(player):
    return [
        o for o in opponents(player) if tuple(o[:2]) in udlr(player)
    ]


def can_move(player):
    aopps = adjacent_opponents(player)
    return udlr(player).intersection(free.difference(set(map(lambda x: x[:2], aopps))))


def adjacent_points(point):
    return udlr(point).difference(player_locations())


def get_path(player, point):
    queue = []
    visited = set()
    queue.append([player[:2]])
    while queue:
        path = queue.pop(0)

        current_point = path[-1]

        if current_point == point:
            return path

        for adjacent_point in sorted(list(adjacent_points(current_point))):
            if adjacent_point not in visited:
                visited.add(adjacent_point)

                new_path = list(path)
                new_path.append(adjacent_point)
                queue.append(new_path)
    return []


def player_locations():
    return set([tuple(p[:2]) for p in players if p[3] > 0])


def reachable_points(player):
    temp = udlr(player).intersection(free).difference(player_locations())
    res = set()
    while temp:
        res |= temp
        nxt = set()
        for t in temp:
            nxt |= udlr(t).intersection(free).difference(player_locations())
        temp = nxt.difference(res)
    return res


def reachable_opponents(player):
    in_range = set()
    legit_players = [tuple(p[:2]) for p in players if p[3] > 0]
    for op in opponents(player):
        in_range |= udlr(op).intersection(free).difference(set(legit_players))

    return reachable_points(player).intersection(in_range)


def nearest_opponent(player):
    paths = []
    for op in reachable_opponents(player):
        paths.append([op, get_path(player, op)])
    m = min([len(p[1]) for p in paths])
    shortest_paths = sorted([p for p in paths if len(p[1]) == m], key=lambda x: x[0])

    return shortest_paths[0]


def move(player):
    curr_pos, path = nearest_opponent(player)
    assert (player[:2] == path[0])
    next_point = list(path[1])
    players[players.index(player)] = next_point + player[2:]
    return next_point + player[2:]


def attack(player, k):
    opponent = sorted(adjacent_opponents(player), key=lambda x: (x[3], x[:2]))[0]

    if player[2] == 'E':
        players[players.index(opponent)] = opponent[:3] + [opponent[3] - k]
    else:
        players[players.index(opponent)] = opponent[:3] + [opponent[3] - 3]


def turn(player, k):
    if player[3] <= 0:
        return
    if not adjacent_opponents(player) and can_move(player) and reachable_opponents(player):
        # print("Moving player", player)
        player = move(player)
        if adjacent_opponents(player):
            attack(player, k)

    elif adjacent_opponents(player):
        # print("Player", player, "Attacking!")
        attack(player, k)


def load_data():
    m, p, w, f = [], [], set(), set()
    board_map = {
        '#': '#',
        'G': '.',
        'E': '.',
        '.': '.'
    }
    with open('data/day15') as text_file:
        lines = text_file.readlines()
        x = 0
        for line in lines:
            line = line.strip()
            p += [[x, j, q, 200] for j, q in enumerate(line) if q in {'G', 'E'}]
            w |= set([(x, j) for j, q in enumerate(line) if q == '#'])
            f |= set([(x, j) for j, q in enumerate(line) if q != '#'])
            m.append([board_map[l] for l in line])
            x += 1
    return m, p, w, f


def exists_gremlins():
    return len([p for p in players if p[3] > 0 and p[2] == 'G'])


def exists_elves():
    return len([p for p in players if p[3] > 0 and p[2] == 'E'])


def print_board():
    live = [[x for x in board[_]] for _ in range(len(board))]
    rows = defaultdict(list)
    for p in players:
        if p[3] > 0:
            rows[p[0]].append("%s(%d)" % (p[2], p[3]))
            live[p[0]][p[1]] = p[2]

    print('-'*len(board[0]))
    for r, b in enumerate(live):
        print(''.join(b) + '   ' + ', '.join(rows[r]))
    print('-' * len(board[0]))


if __name__ == '__main__':
    board, players, walls, free = load_data()

    # Part 1
    i, rounds = 0, 0
    while exists_elves() and exists_gremlins():
        turn(players[i], 3)
        i += 1
        if i == len(players):
            players = sorted(players, key=lambda x: x[:2])
            i = 0
            rounds += 1

    print(rounds * sum(p[3] for p in players if p[3] > 0))

    board, players, walls, free = load_data()

    # Part 2
    i, rounds = 0, 0
    while exists_elves() and exists_gremlins():
        turn(players[i], 34)  # TODO - make this more general.
        i += 1
        if i == len(players):
            players = sorted(players, key=lambda x: x[:2])
            i = 0
            rounds += 1

    print(rounds * sum(p[3] for p in players if p[3] > 0))

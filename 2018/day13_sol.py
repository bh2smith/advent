delta = {
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
    'v': (1, 0)
}

spot_pairs = {
    ('-', 'v'): -1,
    ('-', '>'): '>',
    ('-', '<'): '<',
    ('-', '^'): -1,
    ('|', 'v'): 'v',
    ('|', '>'): -1,
    ('|', '<'): -1,
    ('|', '^'): '^',
    ('/', 'v'): '<',
    ('/', '>'): '^',
    ('/', '<'): 'v',
    ('/', '^'): '>',
    ('\\', 'v'): '>',
    ('\\', '>'): 'v',
    ('\\', '<'): '^',
    ('\\', '^'): '<',
    ('+', 'v'): '+',
    ('+', '>'): '+',
    ('+', '<'): '+',
    ('+', '^'): '+',
}

turn_map = {
    0: 'l',
    1: 's',
    2: 'r'
}

rotate = {
    '<': {
        'l': 'v',
        's': '<',
        'r': '^',
    },
    '>': {
        'l': '^',
        's': '>',
        'r': 'v',
    },
    '^': {
        'l': '<',
        's': '^',
        'r': '>',
    },
    'v': {
        'l': '>',
        's': 'v',
        'r': '<',
    },
}


def intersection(t, s):
    return t['at'] == s['at']


def part1(arr):
    while 1:
        for t in arr:
            move(t)
            if any([intersection(t, s) for s in arr if s != t]):
                return t['at'][::-1]
        arr = sorted(arr, key=lambda k: k['at'])


def part2(arr):
    while len(arr) > 1:
        to_remove = []
        for t in arr:
            move(t)
            if any([intersection(t, s) for s in arr if s != t]):
                to_remove += [i for i, s in enumerate(arr) if s['at'] == t['at']]
        arr = [t for i, t in enumerate(arr) if i not in to_remove]
        arr = sorted(arr, key=lambda k: k['at'])

    return arr[0]['at'][::-1]


def intersections(arr):
    res = []
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[i]['at'] == arr[j]['at']:
                res.append(arr[i]['at'][::-1])
    return res


def add_vec(x, y):
    assert(len(x) == len(y))
    return list([x[_] + y[_] for _ in range(len(x))])


def move(t):
    nxt = add_vec(t['at'], delta[t['facing']])
    spot = track_data[nxt[0]][nxt[1]]
    if spot in {'<': '-', '>': '-', '^': '|', 'v': '|'}.keys():
        spot = {'<': '-', '>': '-', '^': '|', 'v': '|'}[spot]

    new_face = spot_pairs[(spot, t['facing'])]

    if new_face == '+':
        to_turn = turn_map[t['intersections'] % 3]
        new_face = rotate[t['facing']][to_turn]
        t['intersections'] += 1
    t['facing'] = new_face
    t['at'] = nxt


def move_all(arr):
    for k, a in enumerate(arr):
        move(a)


def load_data():
    with open('data/day13') as f:
        track = []
        trains = []
        lines = f.readlines()
        for i, line in enumerate(lines):
            track.append(line[:-1])
            train_count = line.count('<') + line.count('>') + line.count('^') + line.count('v')
            if train_count:
                for j, c in enumerate(track[-1]):
                    if c in {'<', '>', '^', 'v'}:
                        trains.append({
                            'at': [i, j],
                            'facing': c,
                            'intersections': 0
                        })
    return track, sorted(trains, key=lambda k: k['at'])


if __name__ == '__main__':

    track_data, train_data = load_data()
    print(part1(train_data))

    track_data, train_data = load_data()
    print(part2(train_data))

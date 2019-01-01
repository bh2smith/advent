
INITIAL_STATE = '##....#.#.#...#.#..#.#####.#.#.##.#.#.#######...#.##....#..##....#.#..##.####.#..........#..#...#'

MOVES = {
    '..#.#': '#',
    '.####': '#',
    '#....': '.',
    '####.': '#',
    '...##': '.',
    '.#.#.': '.',
    '..#..': '.',
    '##.#.': '.',
    '#.#.#': '#',
    '.....': '.',
    '#.#..': '.',
    '....#': '.',
    '.#..#': '.',
    '###.#': '#',
    '#..#.': '.',
    '#####': '.',
    '...#.': '#',
    '#.##.': '#',
    '.#.##': '#',
    '#..##': '#',
    '.##..': '#',
    '##.##': '.',
    '..###': '.',
    '###..': '.',
    '##..#': '#',
    '.#...': '#',
    '.###.': '#',
    '#.###': '.',
    '.##.#': '.',
    '#...#': '#',
    '##...': '.',
    '..##.': '.',
}


def apply_moves(state, moves):
    res = ['.' for _ in range(len(state))]
    for i in range(len(state) - 5):
        res[i+2] = moves[state[i:i+5]]
    return ''.join(res)


def part1():
    pad = '.' * (20 + 3)
    nxt = pad + INITIAL_STATE + pad
    for _ in range(20):
        nxt = apply_moves(nxt, MOVES)
    nxt = nxt[len(pad):]

    res = 0
    for i, c in enumerate(nxt):
        if c == '#':
            res += i
    return res  # 2349


def part2():
    # This solution requires finding the place where motion becomes consistent (i.e. at 185)
    pad = '.' * (185 + 3)
    nxt = pad + INITIAL_STATE + pad
    for _ in range(185):
        nxt = apply_moves(nxt, MOVES)
    nxt = nxt[len(pad):]

    res = count = 0
    for i, c in enumerate(nxt):
        if c == '#':
            count += 1
            res += i

    num_moves = 50000000000
    already_moved = 185
    return count * (num_moves - already_moved) + res  # 2100000001168


if __name__ == '__main__':
    print(part1())
    print(part2())

INPUT = 380621


def combine(arr, x, y):
    v = arr[x] + arr[y]
    if v > 9:
        s, t = map(int, [str(v)[0], str(v)[1]])
        arr += [s, t]
    else:
        arr.append(v)
    return arr


def move(arr, x):
    to_move = arr[x] + 1
    return (x + to_move) % len(arr)


def part1(arr, x, y):
    while len(arr) < INPUT + 11:
        arr = combine(arr, x, y)
        x = move(arr, x)
        y = move(arr, y)

    return arr, x, y


def part2(arr, x, y):
    in_s = str(INPUT)
    while 1:
        arr = combine(arr, x, y)
        x = move(arr, x)
        y = move(arr, y)

        if len(arr) % 1000000 == 0:
            checker = ''.join(map(str, arr))
            if in_s in checker:
                return checker.index(in_s)


if __name__ == '__main__':
    res, l_at, r_at = part1([3, 7], 0, 1)
    print(''.join(map(str, res[INPUT:-1])))

    res = part2(res, l_at, r_at)
    print(res)

def parse(data):
    if not data:
        return 0, []
    children, meta = data[0], data[1]
    data = data[2:]
    tally, scores = 0, []

    for i in range(children):
        tot, score, data = parse(data)
        tally += tot
        scores.append(score)

    tally += sum(data[:meta])

    if children == 0:
        ret_score = sum(data[:meta])
    else:
        ret_score = sum(scores[k - 1] for k in data[:meta] if 0 < k <= len(scores))

    return tally, ret_score, data[meta:]


def part1():
    return parse(arr)[0]


def part2():
    return parse(arr)[1]


if __name__ == '__main__':
    with open('data/day08') as f:
        lines = f.readlines()
        for line in lines:
            arr = map(int, line.strip().split())

    # print(parse(map(int, '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split())))
    print(part1())
    print(part2())

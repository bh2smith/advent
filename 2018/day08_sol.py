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


if __name__ == '__main__':
    arr = list(map(int, open('data/day08').read().strip().split()))

    print(parse(arr)[0])
    print(parse(arr)[1])

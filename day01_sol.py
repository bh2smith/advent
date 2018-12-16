from collections import defaultdict


def part1(arr):
    return sum(arr)


def part2(arr):
    freq, at = 0, 0
    seen = defaultdict(int)
    while 2 not in seen.values():
        if at == len(arr):
            at = 0
        freq += arr[at]
        seen[freq] += 1
        at += 1

    return freq


if __name__ == '__main__':
    with open('data/day01') as f:
        frequencies = []
        t = f.readlines()
        for line in t:
            frequencies.append(int(line.strip()))

    print(part1(frequencies))
    print(part2(frequencies))

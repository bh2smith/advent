if __name__ == '__main__':
    with open('data/day01') as f:
        frequencies = []
        t = f.readlines()
        for line in t:
            frequencies.append(int(line.strip()))

    # Part 1
    print(sum(frequencies))

    # Part 2
    f, i = 0, 0
    seen = set()
    while f not in seen:
        seen.add(f)
        f += frequencies[i]
        i += 1
        i %= len(frequencies)
    print(f)

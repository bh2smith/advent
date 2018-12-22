if __name__ == '__main__':
    freaks = list(map(lambda l: int(l.strip()), open('data/day01').readlines()))

    print("Part1:", sum(freaks))

    f, i, seen = 0, 0, set()
    while f not in seen:
        seen.add(f)
        f += freaks[i]
        i += 1
        i %= len(freaks)
    print("Part2:", f)

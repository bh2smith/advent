if __name__ == '__main__':
    s = open('input').read().strip()
    print("part 1:", s.count('(') - s.count(')'))

    floor, i = 0, 0
    while i < len(s) and floor != -1:
        floor += 1 * (s[i] == '(') - 1 * (s[i] == ')')
        i += 1

    assert (floor == -1)
    print("part 2:", i + 1)

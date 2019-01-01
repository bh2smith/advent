def vowel_count(st):
    return sum([st.count(x) for x in 'aeiou'])


def no_subs(st, arr):
    return not any([a in st for a in arr])


def two_in_row(st):
    for i in range(len(st) - 1):
        if st[i] == st[i + 1]:
            return True
    return False


def nice1(st):
    bad_subs = ['ab', 'cd', 'pq', 'xy']
    return vowel_count(st) >= 3 and two_in_row(st) and no_subs(st, bad_subs)


def nice2(st):
    pairs = [st[i:i + 2] for i in range(len(st) - 1)]

    return any(st.count(p) > 1 for p in pairs) and any(
        [st[i] == st[i + 2] for i in range(len(st) - 2)])


if __name__ == '__main__':
    strings = list(map(lambda t: t.strip(), open('input').readlines()))
    print("part 1:", sum(1 * nice1(x) for x in strings))

    # strings = ['qjhvhtzxzqqjkmpb', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']
    print("part 2:", sum(1 * nice2(x) for x in strings))
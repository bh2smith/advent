from collections import defaultdict


def part1(arr):
    d = {}
    for st in arr:
        d[st] = defaultdict(int)
        for c in st:
            d[st][c] += 1

    two, three = 0, 0
    for k in d:
        if 2 in d[k].values():
            two += 1
        if 3 in d[k].values():
            three += 1
    return two * three


def part2(arr):

    def differ_length(x, y):
        cnt = 0
        for c, d in zip(x, y):
            if c != d:
                cnt += 1
        return cnt

    found = 0
    for i in range(len(arr)-1):
        if found:
            break
        for j in range(i+1, len(arr)):
            a, b = arr[i], arr[j]
            if differ_length(a, b) == 1:
                found = 1
                break

    def diff_index(x, y):
        ind = 0
        for c, d in zip(x, y):
            if c != d:
                return ind
            ind += 1

    i = diff_index(a, b)

    return a[:i] + a[i+1:]


if __name__ == '__main__':
    with open('data/day02') as f:
        in_list = []
        lines = f.readlines()
        for line in lines:
            in_list.append(line.strip())

    print(part1(in_list))
    print(part2(in_list))

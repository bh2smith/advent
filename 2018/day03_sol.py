
def part1(claims):
    for c in claims:
        i, j = c[0]
        I, J = c[1]
        for x in range(i, i+I):
            for y in range(j, j+J):
                board[x][y] += 1

    r = 0
    for i in range(1000):
        for j in range(1000):
            if board[i][j] > 1:
                r += 1
    return r


def part2(claims):
    for claim in claims:
        i, j = claim[0]
        I, J = claim[1]
        if all([board[x][y] == 1 for x in range(i, i+I) for y in range(j, j+J)]):
            return claims.index(claim) + 1


if __name__ == '__main__':

    with open('data/day03') as f:
        arr = []
        lines = f.readlines()
        for line in lines:
            x, y = line.strip().split(' ')[2:]
            x = list(map(int, x[:-1].split(',')))
            y = list(map(int, y.split('x')))
            arr.append([x, y])

    board = [[0 for _ in range(1000)] for _ in range(1000)]

    print(part1(arr))
    print(part2(arr))

def part1(commands):
    res = [[0 for _ in range(1000)] for _ in range(1000)]
    for command in commands:
        c, x, y = command
        for i in range(x[0], y[0] + 1):
            for j in range(x[1], y[1] + 1):
                if c == 'on':
                    res[i][j] = 1
                elif c == 'off':
                    res[i][j] = 0
                else:
                    res[i][j] = (1 + res[i][j]) % 2
    return sum(sum(r) for r in res)


def part2(commands):
    res = [[0 for _ in range(1000)] for _ in range(1000)]
    for command in commands:
        c, x, y = command
        for i in range(x[0], y[0] + 1):
            for j in range(x[1], y[1] + 1):
                if c == 'on':
                    res[i][j] += 1
                elif c == 'off':
                    res[i][j] -= 1 * (res[i][j] > 0)
                else:
                    res[i][j] += 2
    return sum(sum(r) for r in res)


if __name__ == '__main__':
    instructions = []
    with open('input') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip().split()
            to = list(map(int, line[-1].split(',')))
            if line[1] in {'on', 'off'}:
                fr = list(map(int, line[2].split(',')))
                do = line[1]
            else:
                fr = list(map(int, line[1].split(',')))
                do = line[0]
            instructions.append((do, fr, to))

    print("part 1:", part1(instructions))
    print("part 2:", part2(instructions))

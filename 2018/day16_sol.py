from utils.op_codes import ops


def load_part2():
    op_calls = []
    with open('data/day16part2') as text_file:
        lines = text_file.readlines()
        for line in lines:
            op_calls.append(list(map(int, line.strip().split())))

    return op_calls


def part1():
    transitions, codes = [], []
    with open('data/day16') as text_file:
        lines = text_file.readlines()
        for i in range(0, len(lines), 4):
            b = list(map(int, lines[i].strip()[9:-1].split(',')))
            a = list(map(int, lines[i+2].strip()[9:-1].split(',')))
            transitions.append((b, a))
            codes.append(list(map(int, lines[i + 1].strip().split())))

    possibilities = {o: set() for o in ops}
    ans = 0
    for transition, code in zip(transitions, codes):
        before = transition[0]
        after = transition[1]
        count = 0
        for s in ops:
            if ops[s](code[1], code[2], code[3], before) == after:
                possibilities[s].add(code[0])
                count += 1

        if count >= 3:
            ans += 1

    return ans, possibilities


if __name__ == '__main__':
    part1_answer, poss = part1()
    print(part1_answer)

    reduced_possibilities = {}
    while len(reduced_possibilities.keys()) < 16:
        for p in poss:
            if len(poss[p]) == 1:
                found = poss[p].pop()
                reduced_possibilities[found] = p
                for op in poss:
                    if found in poss[op]:
                        poss[op].remove(found)

    data = load_part2()
    register = [0, 0, 0, 0]
    for op_call in data:
        function = reduced_possibilities[op_call[0]]
        x, y, z = op_call[1:]

        register = ops[function](x, y, z, register)

    print(register[0])

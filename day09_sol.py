from collections import deque, defaultdict


def play_game(max_players, last_marble):
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % max_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0


def part1():
    return play_game(np, last)


def part2():
    return play_game(np, last*100)


if __name__ == '__main__':
    with open('data/day09') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split()

    np, last = map(int, [line[0], line[-2]])

    print(part1())
    print(part2())


# DEAD CODE
# def place_marble(turn, marbles, cmi):
#     curr_m = marbles[cmi]
#     next_m = curr_m + 1 if (turn - 1) % 23 != 0 else turn
#     points = 0
#     if len(marbles) < 2:
#         marbles.append(next_m)
#         cmi += 1
#     elif next_m % 23 != 0:
#         next_ind = (cmi + 1) % len(marbles)
#         marbles.insert(next_ind + 1, next_m)
#         cmi = next_ind + 1
#     else:
#         next_ind = (cmi - 7) % len(marbles)
#         points = next_m + marbles.pop(next_ind)
#         cmi = next_ind
#     return cmi, points
#
#
# def high_score(num_players, last_marble):
#     player_scores = [0 for _ in range(num_players)]
#     marble_index, player_index, marbles = 0, 0, [0]
#     turn = 1
#     while 1:
#         marble_index, points = place_marble(turn, marbles, marble_index)
#         if points:
#             player_scores[player_index] += points
#
#         if last_marble in set(marbles):
#             return max(player_scores)
#
#         turn += 1
#         player_index += 1
#         player_index %= num_players
#
# print(high_score(9, 32))
# print(high_score(10, 1618))
# print(high_score(13, 7999))

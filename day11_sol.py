def power_level(i, j):
    rack_id = i + 10
    p_lev = rack_id * j
    p_lev += SERIAL_NUMBER
    p_lev *= rack_id
    p_lev %= 1000
    p_lev //= 100
    p_lev -= 5
    return p_lev


if __name__ == '__main__':
    SERIAL_NUMBER = 7857
    grid = [[power_level(i, j) for j in range(300)] for i in range(300)]

    max_a = 0
    # Only need to go to 15 (cuz answer is there)
    for k in range(1, 15):
        for x in range(300-k):
            for y in range(300-k):
                new_a = sum([sum(g[y:y+k]) for g in grid[x:x+k]])
                if new_a > max_a:
                    max_a = new_a
                    ans = (x, y, k)

                    print(max_a, ans)


def manhattan(x, y):
    return sum(abs(x[i] - y[i]) for i in range(min(len(x), len(y))))

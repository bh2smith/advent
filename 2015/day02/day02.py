def surface_area(dimensions):
    l, w, h = dimensions
    return 2 * (l * w + w * h + h * l)


def slack(dimensions):
    l, w, h = dimensions
    return min([l * w, l * h, h * w])


def smallest_perimeter(dimensions):
    l, w, h = dimensions
    return 2 * min([l + w, l + h, h + w])


def volume(dimensions):
    l, w, h = dimensions
    return l * w * h


if __name__ == '__main__':
    presents = list(map(lambda t: list(map(int, t.strip().split('x'))), open('input').readlines()))

    print("part 1:", sum([surface_area(p) + slack(p) for p in presents]))

    print("part 2:", sum([smallest_perimeter(p) + volume(p) for p in presents]))

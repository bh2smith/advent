import codecs

if __name__ == '__main__':
    strings = list(map(lambda t: t.strip(), open('input').readlines()))
    l, r, q = 0, 0, 0
    for s in strings:
        l += len(s)
        t = codecs.getdecoder("unicode_escape")(s)[0]
        r += len(t) - 2
        m = s.encode("UTF-8")
        q += len(str(m)) + s.count('"') - 1

    print("part 1:", l - r)
    print("part 2:", q - l)

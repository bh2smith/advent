import hashlib

if __name__ == '__main__':
    key = open('input').read().strip()
    i = 0
    while 1:
        m = hashlib.md5()
        m.update((key + str(i)).encode('utf-8'))
        if m.hexdigest()[:5] == '00000':
            break
        i += 1
    print("part 1:", i)

    while 1:
        m = hashlib.md5()
        m.update((key + str(i)).encode('utf-8'))
        if m.hexdigest()[:6] == '000000':
            break
        i += 1
    print("part 2:", i)
